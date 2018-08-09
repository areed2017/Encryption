package com.company.encryption;

import com.company.hashing.SHA256;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.Charset;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.util.Arrays;
import java.util.Base64;
import java.util.Scanner;
import java.util.logging.Logger;

import static com.company.encryption.Encryption.getBytes;
import static com.company.encryption.Encryption.getString;
import static java.lang.System.out;
import static java.util.logging.Level.SEVERE;

public class MethodAES {

    private static final Logger LOGGER = Logger.getLogger(MethodAES.class.getSimpleName());

    private static Cipher ecb;
    private static Cipher cbc;
    static{
        try {
            ecb = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cbc = Cipher.getInstance("AES/CBC/PKCS5Padding");
        } catch (NoSuchAlgorithmException  | NoSuchPaddingException e) {
            LOGGER.log(SEVERE, "", e);
        }
    }


    private SecretKeySpec key;

    private String iv;

    private static final int BUFFER_SIZE = 16;

    private static final Charset CHARACTER_SET = Charset.forName("UTF-8");


    MethodAES(String key, String iv){
        this.iv = pad(iv);
        byte[] keyBytes = new SHA256().hash(key);
        keyBytes = Arrays.copyOf(keyBytes, BUFFER_SIZE*2);
        this.key = new SecretKeySpec(keyBytes, "AES");
    }

    MethodAES(String key){
        this.iv = null;
        byte[] keyBytes = new SHA256().hash(key);
        keyBytes = Arrays.copyOf(keyBytes, BUFFER_SIZE*2);
        this.key = new SecretKeySpec(keyBytes, "AES");
    }


    public String encryptECB(String text){
        try {
            ecb.init(Cipher.ENCRYPT_MODE, key);

            byte[] message = getBytes(text);
            message = ecb.doFinal(message);
            return Base64.getEncoder().encodeToString(message);
        } catch (InvalidKeyException | BadPaddingException | IllegalBlockSizeException e) {
            LOGGER.log(SEVERE, "", e);
        }
        return null;
    }

    public String decryptECB(String text){
        try {
            ecb.init(Cipher.DECRYPT_MODE, key);

            byte[] message = Base64.getDecoder().decode(getBytes(text));

            message = ecb.doFinal(message);
            return new String( message, CHARACTER_SET);
        } catch (InvalidKeyException | BadPaddingException | IllegalBlockSizeException e) {
            LOGGER.log(SEVERE, "", e);
        }
        return null;
    }


    private static String pad(String text){
        int numberOfBlankSpaces = BUFFER_SIZE - text.length() % BUFFER_SIZE;
        StringBuilder filler = new StringBuilder();
        for ( int i = 0; i < numberOfBlankSpaces; i++)
            filler.append(Character.toString((char) numberOfBlankSpaces));
        return text + filler;
    }

    public static String removePadding(String text ){
        char lastChar = text.charAt(text.length() - 1);
        int numberOfBlankSpace = (int) lastChar;
        int lengthOfText = BUFFER_SIZE - numberOfBlankSpace;
        return text.substring(0, lengthOfText);
    }


    public static void testAll(){
        Scanner scanner = new Scanner(System.in);
        out.print("Key to encrypt with: ");
        String key = scanner.nextLine();
        out.print("String to encrypt: ");
        String text = scanner.nextLine();
        out.print("Initial vector to encrypt: ");
        String iv = scanner.nextLine();

        MethodAES aes = new MethodAES(key, iv);
        StringBuilder output = new StringBuilder("Given;\n\t-key\t\t\t\t'" + key + "'\n\t-Text\t\t\t\t'" + text + "'\n\t-Initial Vector\t\t'" + iv + "'\n");

        for( int i = 0; i < 3; i++){
            String encrypted = aes.encryptECB(text);
            output.append("Encrypted: ");
            output.append(encrypted);
            output.append("\n");
            output.append("Encrypted length: ");
            output.append(encrypted.length());
            output.append("\n");
            output.append("Decrypted: ");
            output.append(aes.decryptECB(encrypted));
            output.append("\n\n");
        }

        out.print(output);

    }

    public static void main(String[] args) {
        MethodAES.testAll();
    }
}
