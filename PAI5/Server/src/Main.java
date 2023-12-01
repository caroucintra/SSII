import java.io.DataInputStream;
import java.net.*;

public class Main {
    private static String clientIpAddress = "127.0.0.1";
    public static void main(String[] args) {

        System.out.println("Server started...\nWaiting for connection...");
        try{
            InetSocketAddress serverAddress = new InetSocketAddress(clientIpAddress, 3030);
            ServerSocket ss = new ServerSocket();
            ss.bind(serverAddress);
            Socket s=ss.accept();//establishes connection
            DataInputStream dis=new DataInputStream(s.getInputStream());
            String  str=(String)dis.readUTF();
            System.out.println("message= "+str);
            ss.close();
        }catch(Exception e){System.out.println(e);}
    }
}