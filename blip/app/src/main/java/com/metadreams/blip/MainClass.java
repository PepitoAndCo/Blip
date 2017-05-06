package com.metadreams.blip;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.Toast;

import com.metadreams.blip.R;

public class MainClass extends AppCompatActivity {

    public int Passed;


    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.boot);

        System.out.println("OnCreate of Mainclass");
        ServerSendFunction();
    }

    public void ServerSendFunction() {
        // startActivity(new Intent("fr.extragornax.drunktest.ServerSend"));

        //Wait 1second for ServerSend to fully terminate

        try {

            Thread.sleep(1000);                 //1000 milliseconds is one second.
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        // Passed = ServerSend.Pass;

        System.out.println("Passed value : " + Passed);
        Boot();
    }

    public void Boot() {

        //Passed = ServerSend.Pass;
        Passed = 1;

        if(Passed == 1){
            System.out.println("SERVERSEND Passed");
            startActivity(new Intent("fr.extragornax.drunktest.ReceivedMessage"));

        } else if(Passed == 0) {
            System.out.println("SERVERSEND Failed");

            //Toast message
            Context context = getApplicationContext();
            CharSequence text = "The application didn't boot properly!";
            int duration = Toast.LENGTH_SHORT;
            Toast toast = Toast.makeText(context, text, duration);
            toast.show();

            //Close the app
            finish();
        }
    }
}