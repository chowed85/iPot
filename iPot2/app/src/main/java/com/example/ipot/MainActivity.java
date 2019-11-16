package com.example.ipot;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private Button initPot;
    Button fetchData;

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
    }

    public void openSetPointActivity(){
        Intent intent = new Intent(this, SetPointPot.class);
        startActivity(intent);
    }
}
