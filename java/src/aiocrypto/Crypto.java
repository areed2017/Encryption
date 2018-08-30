package aiocrypto;

import java.nio.charset.Charset;
import java.util.Base64;

import static java.util.Base64.*;

public interface Crypto {

    Charset CHARACTER_SET = Charset.forName("UTF-8");

    Decoder decoder = getDecoder();

    String encrypt(String text);

    String decrypt(String text);


    static String encodeUTF8(byte[] text){
        return new String(text, CHARACTER_SET);
    }

    static byte[] decode(String text){
        return decoder.decode(text);
    }

    static String encrypt(Crypto cipher, String text){
        return cipher.encrypt(text);
    }

    static String decrypt(Crypto cipher, String text){
        return cipher.decrypt(text);
    }
}
