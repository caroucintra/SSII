package com.example.myapplication;

import java.security.PublicKey;
import java.security.Signature;

public class tmpConfirmSignature {

    // devuelve si la firma es valida
    public static boolean verifySignature(byte[] data, byte[] signature, PublicKey publicKey) {
        try {
            Signature sg = Signature.getInstance("SHA256withRSA");
            sg.initVerify(publicKey);
            sg.update(data);
            return sg.verify(signature);
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}