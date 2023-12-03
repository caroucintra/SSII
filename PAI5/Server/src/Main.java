import java.net.*;
import java.io.*;

public class Main {
    private static String clientIpAddress = "127.0.0.1";
    private static BufferedReader fromClient;

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
                }
            }
            
            // ss.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}