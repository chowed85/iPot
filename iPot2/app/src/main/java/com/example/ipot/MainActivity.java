package com.example.ipot;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private Button initPot;
    private Button fetchData;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle("Main Page");

        initPot = (Button)findViewById(R.id.setPoint);

        initPot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSetPointActivity();
            }
        });

        fetchData = (Button) findViewById(R.id.plantData);

        fetchData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRetrieveActivity();
            }
        });
    }

    public void openSetPointActivity(){
        Intent intentsetpot = new Intent(this, SetPointPot.class);
        intentsetpot.putExtra("message","This is here because new pot.");
        startActivity(intentsetpot);
    }

    public void openRetrieveActivity(){
        Intent intentretdata = new Intent(this, RetrievePotData.class);
        intentretdata.putExtra("message","This is here because data is requested.");
        startActivity(intentretdata);
    }
}
