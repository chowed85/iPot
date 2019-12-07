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
public class SetPointPot extends AppCompatActivity {

    String name, moisture, interval;
    EditText plantName, Sens, Tint;


    InetAddress IPADDRESS;

    String myIP = "192.168.43.77"; //IP of the Pi being sent the set point

    Button CREATE; //iPot creation button
    JSONObject NEWPOT;//JSON object to hold the set point information

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

    }


    View.OnClickListener buttonConnectOnClick = new View.OnClickListener() {
        @Override
        public void onClick(View v) {

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
                String initPot = NEWPOT.toString();
                System.out.println("The message sent is:" + initPot);

                Thread testSender = new Thread(new Sender(IPADDRESS, 1006, initPot)); //Create a new thread to send a set point
                testSender.start();//Begin the Sender thread

            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    };
}
