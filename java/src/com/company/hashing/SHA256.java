package com.company.hashing;

import java.nio.charset.Charset;

import static com.company.hashing.Hash.CharacterSet.UTF8;

public class SHA256 implements Hash{

    public String getAlgorithm() {
        return "SHA-256";
    }

    public Charset getCharacterSet() {
        return UTF8;
    }
}
