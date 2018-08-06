package com.company.encryption;

import java.security.SecureRandom;
import java.util.Base64;

@SuppressWarnings("WeakerAccess")
public class RandomKey {

    private RandomKey(){}

    public static byte[] randomKey(int length){

        SecureRandom random = new SecureRandom();
        byte[] bytes = new byte[length];
        random.nextBytes(bytes);

        return bytes;
    }

    public static String randomKeyAsString(int length){
        return Base64.getEncoder().encodeToString(randomKey(length));
    }
}
