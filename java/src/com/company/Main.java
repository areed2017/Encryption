package com.company;

import com.company.hashing.MD5;
import com.company.encryption.AES;
import com.company.encryption.RSA;
import com.company.hashing.SHA1;
import com.company.hashing.SHA256;

import java.util.Scanner;

import static java.lang.System.out;

public class Main {

    private static final String ENCRYPTING = "Encrypted: ";
    private static final String DECRYPTING = "Decrypted: ";
    private static final String HASHING = "Hashed: " ;

    private static String type;

    private static String text;

    private static String key;

    private static boolean isEncrypting = false;

    private static boolean isDecrypting = false;

    static{
        RSA.setRSAPublicKeyFile("public_key.der");
        RSA.setRSAPrivateKeyFile("private_key.der");
    }

    public static void main(String[] args) {

        for ( int i = 0; i < args.length; i+=2){
            switch( args[i] ){
                case "-t":
                    type = args[i+1];
                    break;
                case "-c":
                    break;
                case "-ed":
                    isDecrypting = true;
                    isEncrypting = true;
                    text = args[i+1];
                    break;
                case "-e":
                    isEncrypting = true;
                    text = args[i+1];
                    break;
                case "-d":
                    isDecrypting = true;
                    text = args[i+1];
                    break;
                case "-k":
                    key = args[i+1];
                    break;
                case "-h":
                    text = args[i+1];
                    break;
                default:
                    out.println("Unknown argument " + args[i] + " " + args[i+1] );
            }
        }

        type = type.toLowerCase();
        switch (type){
            case "aes":
                if( isEncrypting && isDecrypting){
                    String encrypted =  AES.encrypt(text, key);
                    out.println( ENCRYPTING + encrypted);
                    out.println( DECRYPTING + AES.decrypt(encrypted, key));
                }
                else if(isEncrypting)
                    out.println( ENCRYPTING + AES.encrypt(text, key) );
                else if (isDecrypting)
                    out.println( DECRYPTING + AES.decrypt(text, key) );
                else
                    out.println( "Please specify if you want to decrypt or encrypt with the tag '-e' or '-d' followed by the string you want to act on ");
                break;

            case "rsa":
                if(isEncrypting)
                    out.println( ENCRYPTING + RSA.encrypt(text) );
                else if (isDecrypting)
                    out.println( DECRYPTING + RSA.decrypt(text) );
                else
                    out.println( "Please specify if you want to decrypt or encrypt with the tag '-e' or '-d' followed by the string you want to act on ");
                break;
            case "md2":
                out.println(HASHING + new MD5().hashToString(text));
                break;
            case "md5":
                out.println(HASHING + new MD5().hashToString(text));
                break;
            case "sha1":
                out.println(HASHING + new SHA1().hashToString(text));
                break;
            case "sha256":
                out.println(HASHING + new SHA256().hashToString(text));
                break;
            case "sha384":
                out.println(HASHING + new SHA256().hashToString(text));
                break;
            case "sha512":
                out.println(HASHING + new SHA256().hashToString(text));
                break;
            default:
                out.println("Please specify what type you would like to use with the tag '-t' followed by the type");
        }


        new Scanner(System.in).next();

    }
}
