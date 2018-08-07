package com.company.encryption;

import com.company.hashing.SHA256;

import javax.crypto.Cipher;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;
import java.util.logging.Logger;

import static com.company.encryption.Encryption.getBytes;
import static com.company.encryption.Encryption.getString;
import static java.util.logging.Level.SEVERE;

@SuppressWarnings({"unused", "SameParameterValue"})
public class AES {

    private static final Logger LOGGER = Logger.getLogger(AES.class.getSimpleName());

    private AES(){}

    private static Cipher cipher;
    static {
        try {
            //noinspection SpellCheckingInspection
            cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        } catch (NoSuchAlgorithmException | NoSuchPaddingException e) {
            LOGGER.log(SEVERE, "", e);
        }
    }

    private static final int BUFFER_SIZE = 16;

    //TODO: change the iv to be passed in through the begining of the string
    private static final IvParameterSpec IV = new IvParameterSpec(getBytes(pad("IV GOES HERE")));

    public static String encrypt(String text, String keyStr) {
        Key key = keyGen(keyStr);

        try {
            cipher.init(Cipher.ENCRYPT_MODE, key, IV);

            byte[] message = getBytes(text);
            message = cipher.doFinal(message);
            message = Base64.getEncoder().encode(message);
            return getString(message);
        }
        catch ( Exception e) {
            LOGGER.log(SEVERE, "", e);
        }
        return "";
    }

    public static String decrypt( String text, String keyStr){
        Key key = keyGen(keyStr);
        byte[] message = Base64.getDecoder().decode(getBytes(text));

        try {
            cipher.init(Cipher.DECRYPT_MODE, key, IV);
            message = cipher.doFinal(message);
            return getString(message);
        }
        catch ( Exception e) {
            LOGGER.log(SEVERE, "", e);
        }
        return "";
    }


    private static Key keyGen(String key){
        byte[] keyBytes = new SHA256().hash(key);
        keyBytes = Arrays.copyOf(keyBytes, BUFFER_SIZE*2);
        return new SecretKeySpec(keyBytes, "AES");
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

}
