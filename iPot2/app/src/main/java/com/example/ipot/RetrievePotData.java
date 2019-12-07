package com.example.ipot;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.JSONObject;

import java.net.InetAddress;
import java.net.UnknownHostException;

//Code Author: Zubaer Ahmed

public class RetrievePotData extends AppCompatActivity {

    String name;
    EditText plantName; //Edit text field to hold the Plant Name from the activity

    int portnum = 1006; //The port number from which the
    InetAddress IPADDRESS;
    String myIP = "192.168.43.77";


    Button REQUEST;
    JSONObject POT;//Packet sent to create new pot

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_retrieve_pot_data);

        plantName = (EditText) findViewById(R.id.qryPot); //Edit text field the plant name
        REQUEST = (Button) findViewById(R.id.plantNamereq); //Button for the request of data from the Front End Pi

        name = plantName.getText().toString();


        REQUEST.setOnClickListener(buttonConnectOnClick1);

    }


    View.OnClickListener buttonConnectOnClick1 = new View.OnClickListener() {
        @Override
        public void onClick(View v) {

            //Create an IPAddress of the Front end RPi
            try {
                IPADDRESS = InetAddress.getByName(myIP);

            } catch (UnknownHostException e) {
                e.printStackTrace();
            }

            POT = new JSONObject(); //Pack the entries into a JSON object first
            name = plantName.getText().toString(); //Convert the name of the plant into a String

            try {
                POT.put("type", 2);
                POT.put("humidity", 10);
                POT.put("temp", 10);
                POT.put("time", 10);
                POT.put("name", name);
                String NewPot2 = POT.toString();
                System.out.println("The message to be sent is:" + NewPot2); //Print statement showing the data being sent. Just for validation

                Thread testSender = new Thread(new Sender(IPADDRESS, 1006, NewPot2)); //Creation of a Sender thread
                testSender.start();// Begin the Sender thread

                Thread testRec = new Thread(new PacketReceiver(8008)); //Creation of a Receiver thread
                testRec.start(); //Begin the Thread

            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    };

    }

