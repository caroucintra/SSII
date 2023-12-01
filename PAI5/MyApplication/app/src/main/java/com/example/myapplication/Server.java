package com.example.myapplication;

import java.net.*;
import java.io.*;

public class Server {
    private static String clientIpAddress = "127.0.0.1";
    private static ObjectInputStream fromClient;

    public static void startServer() {

        System.out.println("Server started...\nWaiting for connection...");
        try{
            InetSocketAddress serverAddress = new InetSocketAddress(clientIpAddress, 3030);
            ServerSocket ss = new ServerSocket();
            ss.bind(serverAddress);
            Socket s=ss.accept();//establishes connection
            System.out.println("Connection established!");
            fromClient = new ObjectInputStream(s.getInputStream());
            Message message = (Message) fromClient.readObject();
            message.print();
            ss.close();
        }catch(Exception e){System.out.println(e);}
    }
}