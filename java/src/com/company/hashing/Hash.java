package com.company.hashing;

import java.nio.charset.Charset;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.logging.Level;
import java.util.logging.Logger;

public interface Hash {

    class CharacterSet{
        private CharacterSet(){}
        static final Charset UTF8 = Charset.forName("utf-8");
    }

    class Log{
        private Log(){}
        static final Logger LOGGER = Logger.getLogger(Hash.class.getSimpleName());
    }

    String getAlgorithm();

    Charset getCharacterSet();

    default String hashToString(String str){
        return Base64.getEncoder().encodeToString(hash(str));
    }

    default byte[] hash(String str){
        try {
            MessageDigest messageDigest = MessageDigest.getInstance(this.getAlgorithm());
            return messageDigest.digest(str.getBytes(getCharacterSet()));
        } catch (NoSuchAlgorithmException e) {
            Log.LOGGER.log(Level.SEVERE, "", e);
        }
        return new byte[0];
    }


}
