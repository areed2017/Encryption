package com.company;

import com.company.encryption.RandomKey;
import com.company.hashing.*;
import com.company.encryption.AES;
import com.company.encryption.RSA;

import java.util.Scanner;

import static java.lang.System.out;

public class Main {

    private static final String ENCRYPTING = "Encrypted: ";
    private static final String DECRYPTING = "Decrypted: ";
    private static final String HASHING = "Hashed: " ;

    private static String type ="";

    private static String text;

    private static String key;

    private static boolean isEncrypting = false;

    private static boolean isDecrypting = false;

    private static boolean isSystemOut = false;

    static{
        RSA.setRSAPublicKeyFile("public_key.der");
        RSA.setRSAPrivateKeyFile("private_key.der");
    }

    public static void main(String[] args) {
        int i;
        StringBuilder output = new StringBuilder();
        for (i = 0; i < args.length; i+=2){
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
                case "-o":
                    isSystemOut = true;
                    i--;
                    break;
                case "-r":
                    int length = Integer.parseInt(args[i+1]);
                    for(int j = length; j < 40; j++)
                    {
                        String value = RandomKey.randomKeyAsString(j);
                        output.append("Random: ").append(value).append("\n");
                    }
                    type = "random";
                    break;
                default:
                    output.append("Unknown argument ").append(args[i]).append(" ").append(args[i + 1]).append("\n");
            }
        }

        type = type.toLowerCase();
        switch (type){
            case "aes":
                if( isEncrypting && isDecrypting){
                    String encrypted =  AES.encrypt(text, key);
                    output.append(ENCRYPTING).append(encrypted).append("\n");
                    output.append(DECRYPTING).append(AES.decrypt(encrypted, key)).append("\n");
                }
                else if(isEncrypting)
                    output.append(ENCRYPTING).append(AES.encrypt(text, key)).append("\n");
                else if (isDecrypting)
                    output.append(DECRYPTING).append(AES.decrypt(text, key)).append("\n");
                else
                    output.append("Please specify if you want to decrypt or encrypt with the tag '-e' or '-d' followed by the string you want to act on \n");
                break;

            case "rsa":
                if(isEncrypting)
                    output.append(ENCRYPTING).append(RSA.encrypt(text)).append("\n");
                else if (isDecrypting)
                    output.append(DECRYPTING).append(RSA.decrypt(text)).append("\n");
                else
                    output.append("Please specify if you want to decrypt or encrypt with the tag '-e' or '-d' followed by the string you want to act on \n");
                break;
            case "md2":
                output.append(HASHING).append(new MD5().hashToString(text)).append("\n");
                break;
            case "md5":
                output.append(HASHING).append(new MD5().hashToString(text)).append("\n");
                break;
            case "sha":
                output.append(HASHING.replace(":", "Secure Hash Algorithm 1 (SHA1):")).append(new SHA1().hashToString(text)).append("\n");
                output.append(HASHING.replace(":", "Secure Hash Algorithm 256 (SHA256):")).append(new SHA256().hashToString(text)).append("\n");
                output.append(HASHING.replace(":", "Secure Hash Algorithm 384 (SHA384):")).append(new SHA384().hashToString(text)).append("\n");
                output.append(HASHING.replace(":", "Secure Hash Algorithm 512 (SHA512):")).append(new SHA512().hashToString(text)).append("\n");
                break;
            case "sha1":
                output.append(HASHING).append(new SHA1().hashToString(text)).append("\n");
                break;
            case "sha256":
                output.append(HASHING).append(new SHA256().hashToString(text)).append("\n");
                break;
            case "sha384":
                output.append(HASHING).append(new SHA384().hashToString(text)).append("\n");
                break;
            case "sha512":
                output.append(HASHING).append(new SHA512().hashToString(text)).append("\n");
                break;
            case "random":
                break;
            default:
                output.append("Please specify what type you would like to use with the tag '-t' followed by the type\n");
        }

        if( isSystemOut )
            out.print(output);

        out.print("Exit...");
        new Scanner(System.in).nextLine();

    }
}
