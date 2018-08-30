package aiocrypto;

import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.util.Arrays;

@SuppressWarnings({"WeakerAccess", "unused"})
public interface BlockEncryption {

    Integer BUFFER_SIZE = 16;

    static Key createKey(String key){
        byte[] keyBytes = Hash.sha256(key);
        keyBytes = Arrays.copyOf(keyBytes, BUFFER_SIZE*2);
        return new SecretKeySpec(keyBytes, "AES");
    }

    static int createCounter(int i){
        return i;
    }

    static void createIV(){
        createIV(0);
    }

    static void createIV(int i ){

    }

    static String pad(String text) {
        return pad(text, BUFFER_SIZE);
    }

    static String pad(String text, Integer bufferSize){

        int numberOfBlankSpaces = bufferSize - text.length() % bufferSize;
        StringBuilder filler = new StringBuilder();
        for ( int i = 0; i < numberOfBlankSpaces; i++)
            filler.append(Character.toString((char) numberOfBlankSpaces));
        return text + filler;
    }

    static String removePadding(String text){
        return removePadding(text, BUFFER_SIZE);
    }

    static String removePadding(String text, Integer bufferSize){
        char lastChar = text.charAt(text.length() - 1);
        int numberOfBlankSpace = (int) lastChar;
        int lengthOfText = bufferSize - numberOfBlankSpace;
        return text.substring(0, lengthOfText);
    }

}
