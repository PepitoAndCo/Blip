package fr.extragornax.drunktest;

import android.content.Intent;
import android.os.Bundle;
public class ServerSend extends MainClass {

    public static int Pass = 0;
    //set to 0 then, to make the APP do the initial setup before booting
    private int InitialSetup = 0;

    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.boot);

        System.out.println("in ServerSend");
        Test();

    }


    public void Test()
    {
        //Test if initial setupt is done

        if(InitialSetup == 0){
            //Initial setup
            Pass = 0;
            SendToServer();

        }else{
            Pass = 1;
        }

        System.out.println("THE VALUE OF PASS IS " + Pass);
        System.out.println("THE VALUE OF PASS IS " + Pass);
        System.out.println("THE VALUE OF PASS IS " + Pass);
        System.out.println("THE VALUE OF PASS IS " + Pass);
        System.out.println("THE VALUE OF PASS IS " + Pass);
        System.out.println("THE VALUE OF PASS IS " + Pass);
        System.out.println("THE VALUE OF PASS IS " + Pass);
        System.out.println("THE VALUE OF PASS IS " + Pass);
    }

    public void SendToServer()
    {
        System.out.println("In the sender to server");
        //Send data to the server
        Pass = 1;

        //script to send to the server


    }

}
