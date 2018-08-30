package aiocrypto;

import java.nio.charset.Charset;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.Base64.Encoder;

public interface Hash {

    Charset UTF8 = Charset.forName("utf-8");

    Encoder encoder = Base64.getEncoder();

    static byte[] hash(String str, String algorithm){
        try {
            MessageDigest messageDigest = MessageDigest.getInstance(algorithm);
            return messageDigest.digest(str.getBytes(UTF8));
        }
        catch (NoSuchAlgorithmException e) { /* ignore */ }
        return new byte[0];
    }


    static byte[] md2(String text){
        return encoder.encode(hash(text, "MD2"));
    }


    static String md2AsString(String text){
        return encoder.encodeToString(hash(text, "MD2"));
    }


    static byte[] md5(String text){
        return encoder.encode(hash(text, "MD5"));
    }


    static String md5AsString(String text){
        return encoder.encodeToString(hash(text, "MD5"));
    }



    static byte[] sha256(String text){
        return encoder.encode(hash(text, "SHA-256"));
    }


    static String sha256AsString(String text){
        return encoder.encodeToString(hash(text, "SHA-256"));
    }

}
