package com.company.encryption;

import java.io.UnsupportedEncodingException;

public class Encryption {

    private static final String CHARACTER_SET = "UTF-8";

    public static byte[] getBytes( String text ){
        try {
            return text.getBytes(CHARACTER_SET);
        }
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return new byte[]{};
    }

    public static String getString( byte[] text ){
        try {
            return new String( text, CHARACTER_SET);
        }
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return "";
    }

}
