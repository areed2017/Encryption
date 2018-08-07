package com.company.hashing;


import java.nio.charset.Charset;

import static com.company.hashing.Hash.CharacterSet.UTF8;

public class MD5 implements Hash{

    public String getAlgorithm() {
        return "MD5";
    }

    public Charset getCharacterSet() {
        return UTF8;
    }

}
