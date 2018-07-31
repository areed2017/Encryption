package com.company;

import com.company.encryption.aes.AES;
import com.company.encryption.rsa.RSA;

import static java.lang.System.out;

public class Main {

    private static String type;

    private static String text;

    private static String key;

    private static boolean encrypting = false;

    private static boolean decrypting = false;

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
                case "-e":
                    encrypting = true;
                    text = args[i+1];
                    break;
                case "-d":
                    decrypting = true;
                    text = args[i+1];
                    break;
                case "-k":
                    key = args[i+1];
                    break;
                default:
                    out.println("Unknown argument " + args[i] + " " + args[i+1] );
            }
        }

        if( type.equalsIgnoreCase("aes") ){
            if( encrypting )
                out.println( "Encrypted: " + AES.encrypt(text, key) );
            else if (decrypting)
                out.println( "Decrypted: " + AES.decrypt(text, key) );
            else
                out.println( "Please specify if you want to decrypt or encrypt with the tag '-e' or '-d' followed by the string you want to act on ");
        }
        else if( type.equalsIgnoreCase("rsa") ){
            if( encrypting )
                out.println( "Encrypted: " + RSA.encrypt(text) );
            else if (decrypting)
                out.println( "Decrypted: " + RSA.decrypt(text) );
            else
                out.println( "Please specify if you want to decrypt or encrypt with the tag '-e' or '-d' followed by the string you want to act on ");
        }
        else{
            out.println("Please specify what encryption type you would like to use with the tag '-t' followed by 'AES' or 'RSA'");
        }
    }
}
