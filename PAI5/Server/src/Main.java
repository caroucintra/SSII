import java.io.DataInputStream;
import java.net.*;

public class Main {
    public static void main(String[] args) {

        System.out.println("Server started...\nWaiting for connection...");
        try{
            ServerSocket ss=new ServerSocket(6666);
            Socket s=ss.accept();//establishes connection
            DataInputStream dis=new DataInputStream(s.getInputStream());
            String  str=(String)dis.readUTF();
            System.out.println("message= "+str);
            ss.close();
        }catch(Exception e){System.out.println(e);}
    }
}