package com.example.ipot;

import android.annotation.SuppressLint;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;


public class SetPointPot extends AppCompatActivity {

    String name, moisture, interval;
    EditText plantName, Sens, Tint;
    DatagramSocket socket = null;


    int portnum = 1006;
    InetAddress IPADDRESS;
    //    String myIP = "192.168.43.77";
    //String myIP = "192.168.43.32";
    String myIP = "192.168.43.77";


    Button CREATE;
    JSONObject NEWPOT;//Packet sent to create new pot

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_point_pot);

        plantName = (EditText) findViewById(R.id.plantName);
        Sens = (EditText) findViewById(R.id.setMoist);
        Tint = (EditText) findViewById(R.id.setTint);
        CREATE = (Button) findViewById(R.id.createPot);

        name = plantName.getText().toString();
        moisture = Sens.getText().toString();
        interval = Tint.getText().toString();

        CREATE.setOnClickListener(buttonConnectOnClick);
        //udpClientHandler = new UdpClientHandler(this);
    }
/*
        //Create an IPAddress of the Front end RPi
        try{
            IPADDRESS = InetAddress.getByName(myIP);

        }catch(UnknownHostException e){
            e.printStackTrace();
        }
        */

    View.OnClickListener buttonConnectOnClick = new View.OnClickListener() {
        @Override
        public void onClick(View v) {

            Sender setpointsend = new Sender();
            setpointsend.execute();

        }
    };

    class Sender extends AsyncTask<Void, Void, Void> {

        @SuppressLint("WrongThread")
        @Override
        protected Void doInBackground(Void... voids) {

            //Create an IPAddress of the Front end RPi
            try {
                IPADDRESS = InetAddress.getByName(myIP);

            } catch (UnknownHostException e) {
                e.printStackTrace();
            }

            NEWPOT = new JSONObject();
            name = plantName.getText().toString();
            moisture = Sens.getText().toString();
            interval = Tint.getText().toString();
            try {
                NEWPOT.put("type", 1);
                NEWPOT.put("humidity", moisture);
                NEWPOT.put("temp", 40);
                NEWPOT.put("time", interval);
                NEWPOT.put("name", name);
                String NewPot1 = NEWPOT.toString();
                System.out.println("The message sent is:" + NewPot1);
                byte[] data = NewPot1.getBytes();
                System.out.println("The data byte array is created");

                //while (true) {

                    //DatagramSocket socket = null;
                    try {
                        socket = new DatagramSocket(8008);
                        System.out.println("socket has been created");

                    } catch (SocketException e) {
                        e.printStackTrace();
                        System.out.println("failed to create socket");
                    }

                    DatagramPacket packet = new DatagramPacket(data, data.length, IPADDRESS, portnum);
                System.out.println("dpacket has been created");
                    try {
                        System.out.println("we have entered in the send packet trycatch");
                        socket.send(packet);
                        System.out.println("send done");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
            socket.close();

              //  }//end while(true)
            } catch (JSONException e) {
                e.printStackTrace();
            }
           // socket.close();
            return null;
        }

    }//end setPointPot class
}
