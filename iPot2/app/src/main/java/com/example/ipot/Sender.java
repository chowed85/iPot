package com.example.ipot;

import android.os.Build;

import androidx.annotation.RequiresApi;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;

//Code Author: Zubaer Ahmed

public class Sender implements Runnable{
    int port;
    String message;
    InetAddress ip;
    DatagramSocket socket = null;

    /**
     * Constructor Sender class.
     *
     * @param ip
     * @param port
     * @param message
     */
    public Sender(InetAddress ip, int port, String message){
        this.port=port;
        this.ip=ip;
        this.message=message;
    }

    @RequiresApi(api = Build.VERSION_CODES.N)
    @Override
    public void run() {

        try {
            socket = new DatagramSocket();//Create a new socket in order to send
            System.out.println("Socket has been created SEND");

        } catch (SocketException e) {
            e.printStackTrace();
            System.out.println("Failed to create socket");
        }
        byte[] data = message.getBytes(); //Convert the data into a byte array
        DatagramPacket packet = new DatagramPacket(data, data.length, ip, port); //Create a Datagram packet with the appropriate data
        System.out.println("Packet has been created SEND");
        try {
            System.out.println("We have entered in the send packet try catch");
            socket.send(packet); // Send the packet
            System.out.println("SEND Complete");
        } catch (IOException e) {
            e.printStackTrace();
        }

        socket.close();//Close the Sender socket

    }//end run

}//end the nested class Sender
