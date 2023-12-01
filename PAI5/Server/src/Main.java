import java.io.DataInputStream;
import java.net.*;

public class Main {
    private static String clientIpAddress = "127.0.0.1";
    private static ObjectInputStream fromClient; 

    public static void main(String[] args) {

        System.out.println("Server started...\nWaiting for connection...");
        try{
            InetSocketAddress serverAddress = new InetSocketAddress(clientIpAddress, 3030);
            ServerSocket ss = new ServerSocket();
            ss.bind(serverAddress);
            Socket s=ss.accept();//establishes connection
            fromClient = new ObjectInputStream(s.getInputStream());
            Message message = (Message) fromClient.readObject();
            System.out.println("message= "+message.print());
            ss.close();
        }catch(Exception e){System.out.println(e);}
    }
}