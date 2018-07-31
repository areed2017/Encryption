package com.company.encryption.aes;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;
import java.util.logging.Logger;

import static com.company.encryption.Encryption.getBytes;
import static com.company.encryption.Encryption.getString;
import static java.util.logging.Level.SEVERE;

public class AES {

    private static final Logger LOGGER = Logger.getLogger(AES.class.getSimpleName());

    private AES(){}

    @SuppressWarnings("SpellCheckingInspection")
    private static final String ALGORITHM = "AES/CBC/PKCS5Padding";

    private static final String SECRET_KEY_ALGORITHM = "AES";

    private static final String SHA = "SHA-256";

    private static final int BUFFER_SIZE = 16;

    private static final IvParameterSpec IV = new IvParameterSpec(getBytes(pad("softgenetics")));

    public static String encrypt(String text, String keyStr) {
        Key key = keyGen(keyStr);

        Cipher cipher;
        try {
            cipher = Cipher.getInstance(ALGORITHM);
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

        Cipher cipher;
        try {
            cipher = Cipher.getInstance(ALGORITHM);
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
        MessageDigest messageDigest;
        try {
            messageDigest = MessageDigest.getInstance(SHA);
            byte[] keyBytes = getBytes(key);
            keyBytes = messageDigest.digest(keyBytes);
            keyBytes = Arrays.copyOf(keyBytes, BUFFER_SIZE*2);

            return new SecretKeySpec(keyBytes, SECRET_KEY_ALGORITHM);
        }
        catch (NoSuchAlgorithmException e) {
            LOGGER.log(SEVERE, "", e);
        }
        return null;
    }


    @SuppressWarnings("SameParameterValue")
    private static String pad(String text){
        int numberOfBlankSpaces = BUFFER_SIZE - text.length() % BUFFER_SIZE;
        StringBuilder filler = new StringBuilder();
        for ( int i = 0; i < numberOfBlankSpaces; i++)
            filler.append(Character.toString((char) numberOfBlankSpaces));
        return text + filler;
    }

    @SuppressWarnings("unused")
    public static String removePadding(String text ){
        char lastChar = text.charAt(text.length() - 1);
        int numberOfBlankSpace = (int) lastChar;
        int lengthOfText = BUFFER_SIZE - numberOfBlankSpace;
        return text.substring(0, lengthOfText);
    }

}
