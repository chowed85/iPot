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


public class RetrievePotData extends AppCompatActivity {

    String name, moisture, interval;
    EditText plantName;
    DatagramSocket socket = null;
    DatagramSocket socket2 = null;


    int portnum = 1006;
    InetAddress IPADDRESS;
    //    String myIP = "192.168.43.77";
    //String myIP = "192.168.43.32";
    String myIP = "192.168.43.77";


    Button REQUEST;
    JSONObject POT;//Packet sent to create new pot

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_retrieve_pot_data);

        plantName = (EditText) findViewById(R.id.qryPot);
        REQUEST = (Button) findViewById(R.id.plantNamereq);

        name = plantName.getText().toString();


        REQUEST.setOnClickListener(buttonConnectOnClick);
        //udpClientHandler = new UdpClientHandler(this);
    }


    View.OnClickListener buttonConnectOnClick = new View.OnClickListener() {
        @Override
        public void onClick(View v) {

            DataSender datarequest = new DataSender();
            datarequest.execute();

        }
    };

    class DataSender extends AsyncTask<Void, Void, Void> {

        @SuppressLint("WrongThread")
        @Override
        protected Void doInBackground(Void... voids) {

            //Create an IPAddress of the Front end RPi
            try {
                IPADDRESS = InetAddress.getByName(myIP);

            } catch (UnknownHostException e) {
                e.printStackTrace();
            }

            POT = new JSONObject();
            name = plantName.getText().toString();

            try {
                POT.put("type", 2);
                POT.put("humidity", 10);
                POT.put("temp", 10);
                POT.put("time", 10);
                POT.put("name", name);
                String NewPot2 = POT.toString();
                System.out.println("The message sent is:" + NewPot2);
                byte[] data = NewPot2.getBytes();
                System.out.println("The data byte array is created");

                try {
                    socket = new DatagramSocket();
                    //socket2 = new DatagramSocket(8008);
                    System.out.println("socket has been created");

                } catch (SocketException e) {
                    e.printStackTrace();
                    System.out.println("failed to create socket");
                }

                try {
                    socket2 = new DatagramSocket(8008);
                    System.out.println("socket2 has been created");

                } catch (SocketException e) {
                    e.printStackTrace();
                    System.out.println("failed to create socket");
                }

                DatagramPacket packet = new DatagramPacket(data, data.length, IPADDRESS, portnum);
                System.out.println("dpacket SETUP for sending has been created");
                try {
                    System.out.println("we have entered in the send packet trycatch");
                    socket.send(packet);
                    System.out.println("send done");
                } catch (IOException e) {
                    e.printStackTrace();
                }
                DatagramPacket packet1 = new DatagramPacket(new byte[100], 100);
                while(true) {


                    System.out.println("Waiting for data from receiver");
                    socket2.receive(packet1);
                    System.out.println("Packt receiv");

                    String data2 = "ACK: " + new String(packet.getData()).trim();
                    System.out.println("The data received from the Front End Pi is" + data2);
                    socket.close();
                    socket2.close();

                }

                //  }//end while(true)
            } catch (JSONException e) {
                e.printStackTrace();
            }// socket.close();
            catch (IOException e) {
                e.printStackTrace();
            }
            return null;
        }

    }//end setPointPot class
}
