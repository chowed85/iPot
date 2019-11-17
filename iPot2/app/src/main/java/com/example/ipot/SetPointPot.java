package com.example.ipot;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.Socket;
import java.net.SocketException;
import java.net.UnknownHostException;

public class SetPointPot extends AppCompatActivity {

    String name,moisture,interval;
    EditText plantName,Sens,Tint;
    Socket socket;

    int portnum = 8018;
    InetAddress IPADDRESS;
    String myIP = "192.168.0.21";
    Button CREATE;
    String NEWPOT;//Packet sent to create new pot

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_point_pot);

        plantName = (EditText) findViewById(R.id.plantName) ;
        Sens = (EditText) findViewById(R.id.setMoist);
        Tint = (EditText) findViewById(R.id.setTint);
        CREATE = (Button) findViewById(R.id.createPot);

        name = plantName.getText().toString();
        moisture = Sens.getText().toString();
        interval = Tint.getText().toString();

        //Create an IPAddress of the Front end RPi
        try{
            IPADDRESS = InetAddress.getByName(myIP);

        }catch(UnknownHostException e){
            e.printStackTrace();
        }

        CREATE.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
              NEWPOT = "Message start:" + name + " " + moisture + " " + interval;

              Thread potSender = new Thread(new Sender(IPADDRESS,portnum, NEWPOT));
            }
        });

    }

    private class Sender implements Runnable {
        int port;
        String message;
        InetAddress ip;
        String messageReceived;

        /**
         * Construct
         *
         * @param ip;
         * @param port;
         * @param message;
         */

        public Sender(InetAddress ip, int port, String message) {
            this.port = port;
            this.ip = ip;
            this.message = message;
        }

        @Override
        public void run() {
            try {

                try{socket = new Socket(ip, port);
            } catch (SocketException e) {
                e.printStackTrace();
            }
//initiate output stream
            DataOutputStream cmdOut = new DataOutputStream(socket.getOutputStream());

            while (true) {
                cmdOut.writeBytes(message); //Convert the command to bytes.
                System.out.println("Packet sent:   " + message);

                //Receiving ACK from the input stream
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                messageReceived = in.readLine();

                socket.close();
            }//end while(true)
        }catch(Exception e){
                e.printStackTrace();
            }//end catch

        }//end run
    }//end Sender class

}//end setPointPot class
