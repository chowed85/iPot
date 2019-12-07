package com.example.ipot;

import android.os.Build;

import androidx.annotation.RequiresApi;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

//Code Author: Zubaer Ahmed

public class PacketReceiver implements Runnable{
    int port;
    DatagramSocket socket2 = null;

    public PacketReceiver (){
    }
    /**
     * Constructor Sender class.
     *
     *
     * @param port
     *
     */
    public PacketReceiver(int port){
        this.port=port;

    }

    @RequiresApi(api = Build.VERSION_CODES.N)
    @Override
    public void run() {

        try
        {

            socket2 = new DatagramSocket(port) ; //socket
        System.out.println("socket has been created RECEIVE");
            // Construct the socket

            DatagramPacket packet = new DatagramPacket( new byte[1000], 1000 ) ;   //initialize packet of data to be received

            System.out.println("Packet has been created RECEIVE");
            while( true )
            {
                System.out.println("waiting to receive from Front End");
                socket2.receive(packet) ;     //receive data
               System.out.println("We have received" + packet.getData());

            }

        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        socket2.close();

    }//end run

}//end the nested class Senderackag



