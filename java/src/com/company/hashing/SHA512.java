package com.company.hashing;

import java.nio.charset.Charset;

import static com.company.hashing.Hash.CharacterSet.UTF8;

public class SHA512 implements Hash {

    public String getAlgorithm() {
        return "SHA-512";
    }

    public Charset getCharacterSet() {
        return UTF8;
    }
}
