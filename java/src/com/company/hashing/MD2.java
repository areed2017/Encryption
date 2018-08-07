package com.company.hashing;


import java.nio.charset.Charset;

import static com.company.hashing.Hash.CharacterSet.UTF8;

public class MD2 implements Hash{

    public String getAlgorithm() {
        return "MD2";
    }

    public Charset getCharacterSet() {
        return UTF8;
    }

}
