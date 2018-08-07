package com.company.encryption;

import javax.crypto.Cipher;
import javax.crypto.NoSuchPaddingException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.Key;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;
import java.util.logging.Logger;

import static com.company.encryption.Encryption.getBytes;
import static com.company.encryption.Encryption.getString;
import static java.util.logging.Level.SEVERE;

@SuppressWarnings("UnusedReturnValue")
public class RSA {

    private static final Logger LOGGER = Logger.getLogger(RSA.class.getSimpleName());

    private RSA(){}

    /**
     * UnsetKeyLocationException
     *
     * Exception that is thrown when a key has not been initialized
     */
    static class UnsetKeyLocationException extends Exception{
        private static final String EXCEPTION_MESSAGE =
                "A null key has been set, be sure that you code contains," +
                        " setRsaPublicKeyFile and setRSAPrivateKeyFile methods..";
        UnsetKeyLocationException() {
            super(EXCEPTION_MESSAGE);
        }
    }


    /**
     * cipher
     *
     * the cipher being used here
     */
    private static Cipher cipher;
    static {
        try {
            //noinspection SpellCheckingInspection
            cipher = Cipher.getInstance("RSA");
        } catch (NoSuchAlgorithmException | NoSuchPaddingException e) {
            LOGGER.log(SEVERE, "", e);
        }
    }

    /**
     * rsaPublicKey
     *
     * rsa public key being used, must be set before use
     */
    private static Key rsaPublicKey = null;

    /**
     * rsaPrivateKey
     *
     * rsa private key being used, must be set before use
     */
    private static Key rsaPrivateKey = null;


    /**
     * setRSAPublicKeyFile
     *
     * @implNote File MUST be in the format of .der
     * @param filename file location of the public key being used
     * @return boolean status of the key being set
     */
    public static boolean setRSAPublicKeyFile(String filename){
        try {
            byte[] keyBytes = Files.readAllBytes(Paths.get(filename));

            X509EncodedKeySpec spec = new X509EncodedKeySpec(keyBytes);
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");
            rsaPublicKey = keyFactory.generatePublic(spec);
            return true;

        }
        catch (IOException | NoSuchAlgorithmException | InvalidKeySpecException e) {
            LOGGER.log(SEVERE, "", e);
        }
        return false;
    }

    /**
     * setRSAPrivateKeyFile
     *
     * @implNote File MUST be in the format of .der
     * @param filename file location of the private key being used
     * @return boolean status of the key being set
     */
    public static boolean setRSAPrivateKeyFile( String filename ){

        try {
            byte[] keyBytes = Files.readAllBytes(Paths.get(filename));

            PKCS8EncodedKeySpec spec = new PKCS8EncodedKeySpec(keyBytes);
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");
            rsaPrivateKey = keyFactory.generatePrivate(spec);
            return true;

        }
        catch (IOException | NoSuchAlgorithmException | InvalidKeySpecException e) {
            LOGGER.log(SEVERE, "", e);
        }
        return false;
    }

    /**
     * encrypt
     *
     * @param msg message to be encrypted
     * @return bytes of the encrypted message
     */
    public static String encrypt(String msg){
        byte[] message = getBytes(msg);

        try {
            if( rsaPublicKey == null )
                throw new UnsetKeyLocationException();

            cipher.init(Cipher.ENCRYPT_MODE, rsaPublicKey );
            byte[] encrypted = cipher.doFinal(message);
            encrypted = Base64.getEncoder().encode(encrypted);
            return getString(encrypted);
        }
        catch (Exception e) {
            LOGGER.log(SEVERE, "", e);
        }
        return "";
    }

    /**
     * decrypt
     *
     * @param message message to be decrypted
     * @return bytes of the decrypted message
     */
    public static String decrypt(String message){
        byte[] msg = Base64.getDecoder().decode(message);
        try {
            if( rsaPrivateKey == null )
                throw new UnsetKeyLocationException();

            cipher.init(Cipher.DECRYPT_MODE, rsaPrivateKey );
            byte[] decrypted = cipher.doFinal(msg);
            return getString(decrypted);

        }
        catch (Exception e) {
            LOGGER.log(SEVERE, "", e);
        }
        return "";
    }

}
