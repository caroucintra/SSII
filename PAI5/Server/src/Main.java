import java.net.*;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;
import java.io.*;

public class Main {
    private static String clientIpAddress = "127.0.0.1";
    private static BufferedReader fromClient;
    private static PublicKey publicKey;    
    private static byte[] signedMessage;
    private static byte[] rawMessage;


    private static String publicKeyString = "MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBh8jFNbxObv/N07An2LJnI\n" + 
            "1TEwpKrPog3qQJQ4UgIY2n5Jes1Sl/VUDAdyrx85a8mZjkwLYBO6aL1tniIRtSik\n" + 
            "Zl7CdKOhFs4HJ4yuExYMGmqBate9vIapi5OiTjE0mSRg/mwdYhSWJyozmET9gRlr\n" + 
            "BoSyuEPCzRQeb7YrQv/6TjTKA8ONeCDrnWIpg3EHU/EYLSZN5AUxYG1IPGTU4WzX\n" + 
            "Kk0w2N7cmMeBgNoOGADjFYipwgv4d3nITdjRvoLeyrCXhWJH+M8xm69mP4UJK3t2\n" + 
            "23gGRR4VViszS1FnLudT3SMUnDSIzibW0PRbIpv6YHMH/VQRgFb26uNSTLHnb5oj\n" + 
            "AgMBAAE=";

    public static void main(String[] args) {

        System.out.println("Server started...\nWaiting for connection...");
        try {
            InetSocketAddress serverAddress = new InetSocketAddress(clientIpAddress, 3030);
            ServerSocket ss = new ServerSocket();
            ss.bind(serverAddress);
            Socket s = ss.accept();// establishes connection
            System.out.println("Connection established!");

            fromClient = new BufferedReader(new InputStreamReader(s.getInputStream()));

            while (true){
                String message;
                while ((message = fromClient.readLine()) != null) {
                    System.out.println(message);
                    parseMessage(message);
                    generateKeyPair();
                    boolean verified = doVerify(publicKey,rawMessage,signedMessage);
                    System.out.println(verified);
                }
            }
            
            // ss.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    private static void parseMessage(String message){
        String[] parsed = message.split(";");
        rawMessage = parsed[0].getBytes();
        signedMessage = Base64.getDecoder().decode(parsed[1]);

    }



    private static void generateKeyPair() {
        try {

            StringBuilder pkcs8Lines = new StringBuilder();
            BufferedReader rdr = new BufferedReader(new StringReader(publicKeyString));
            String line;
            while ((line = rdr.readLine()) != null) {
                pkcs8Lines.append(line);
            }

            // Base64 decode the result
            String pkcs8String = pkcs8Lines.toString();
            byte [] pkcs8Pem = pkcs8String.getBytes();


            byte [] pkcs8EncodedBytes = new byte[0];
            pkcs8EncodedBytes = Base64.getDecoder().decode(pkcs8Pem);

            // extract the private key

            X509EncodedKeySpec keySpec = new X509EncodedKeySpec(pkcs8EncodedBytes);

            KeyFactory kf = KeyFactory.getInstance("RSA");

            Main.publicKey = kf.generatePublic(keySpec);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    protected static boolean doVerify(PublicKey publicKey, byte[] data, byte[] signature)
    throws InvalidKeyException, java.security.SignatureException {
        Signature sig;
        try {
            sig = Signature.getInstance("SHA256withRSA");
            sig.initVerify(publicKey);
            sig.update(data);
            return sig.verify(signature);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}