package com.metadreams.blip;

import android.app.Activity;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.telephony.SmsManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import android.support.v7.widget.Toolbar;
import android.support.v7.app.WindowDecorActionBar;

import com.metadreams.blip.APICall;
import com.metadreams.blip.R;

import java.io.FileOutputStream;

public class TextPage extends AppCompatActivity {

    int PassFilter = 1;
    Button Sendbutton;
    EditText PhoneNumber;
    EditText Message;
    String Status;
    String statusSend = "Waiting";
    long Userid = 12345;
    String Acctype = "generic";
    String LaPOSTString = "12345";
    long latestPOST = Long.parseLong(LaPOSTString);
    public long curentdate = System.currentTimeMillis(); // = curent time / date
    long newertext = 2; // = find the latest text date
    private final String USER_AGENT = "Mozilla/5.0";
    private String webAdress = "http://drunk.extragornax.fr:2222/send_text?id"+ Userid + "&type=" + Acctype;

    public static String LatestsPostFile = "LatestPOSTDate";
    SharedPreferences PostDate;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.text);

        Sendbutton = (Button) findViewById(R.id.Sendbutton);
        PhoneNumber = (EditText) findViewById(R.id.PhoneNumber);
        Message = (EditText) findViewById(R.id.Message);

        Sendbutton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String phoneNo = PhoneNumber.getText().toString();
                String message = Message.getText().toString();

                FilterTheMessage();

                if (phoneNo.length() > 0 && message.length() > 0) {
                    if (PassFilter == 1) {
                        System.out.println("Filter passed, Sending Message");
                        message = message + "\n\nMessage send with Drunk Test";
                        sendSMS(phoneNo, message);

                        Status = "Sending";

                        Toast.makeText(getBaseContext(),
                                "Sending the message to " + phoneNo + ".",
                                Toast.LENGTH_SHORT).show();

                    } else {
                        //POPUP
                        System.out.println("Didn't pass the filter");
                    }
                } else {
                    Toast.makeText(getBaseContext(),
                            "Please enter both phone number and message.",
                            Toast.LENGTH_SHORT).show();
                    Status = "Failed";

                }

                sendSMS(phoneNo, message);
            }
        });

        PostDate = getSharedPreferences(LatestsPostFile, 0);
    }

    private void FilterTheMessage() {
        int NeedRevision = 0;
        //FILTER HERE

        //NeedRevison = 1;
        //if something is filtered

        //NeedRevison = 0;
        //if nothing filtered, ready to send

        if(NeedRevision == 1){
            PassFilter = 0;
        }else{
            PassFilter = 1;
        }

    }

    //---sends an SMS message to another device---
    private void sendSMS(String phoneNumber, String message) {

        String SENT = "SMS_SENT";
        String DELIVERED = "SMS_DELIVERED";

        //PendingIntent pi = PendingIntent.getActivity(this, 0, new Intent(this, SMS.class), 0);
        SmsManager sms = SmsManager.getDefault();
        sms.sendTextMessage(phoneNumber, null, message, null, null);


        PendingIntent sentPI = PendingIntent.getBroadcast(this, 0,
                new Intent(SENT), 0);

        PendingIntent deliveredPI = PendingIntent.getBroadcast(this, 0,
                new Intent(DELIVERED), 0);

        //---when the SMS has been sent---
        registerReceiver(new BroadcastReceiver(){
            @Override
            public void onReceive(Context arg0, Intent arg1) {
                switch (getResultCode())
                {
                    case Activity.RESULT_OK:
                        Toast.makeText(getBaseContext(), "SMS sent",
                                Toast.LENGTH_SHORT).show();
                        statusSend = "SMS sent";
                        break;
                    case SmsManager.RESULT_ERROR_GENERIC_FAILURE:
                        Toast.makeText(getBaseContext(), "Generic failure",
                                Toast.LENGTH_SHORT).show();
                        statusSend = "Generic failure";
                        break;
                    case SmsManager.RESULT_ERROR_NO_SERVICE:
                        Toast.makeText(getBaseContext(), "No service",
                                Toast.LENGTH_SHORT).show();
                        statusSend = "No service";
                        break;
                    case SmsManager.RESULT_ERROR_NULL_PDU:
                        Toast.makeText(getBaseContext(), "Null PDU",
                                Toast.LENGTH_SHORT).show();
                        statusSend = "Null PDU";
                        break;
                    case SmsManager.RESULT_ERROR_RADIO_OFF:
                        Toast.makeText(getBaseContext(), "Radio off",
                                Toast.LENGTH_SHORT).show();
                        statusSend = "Radio off";
                        break;
                }
            }
        }, new IntentFilter(SENT));

//---when the SMS has been delivered---
        registerReceiver(new BroadcastReceiver(){
            @Override
            public void onReceive(Context arg0, Intent arg1) {
                switch (getResultCode())
                {
                    case Activity.RESULT_OK:
                        Toast.makeText(getBaseContext(), "SMS delivered",
                                Toast.LENGTH_SHORT).show();
                        statusSend = "SMS delivered";
                        break;
                    case Activity.RESULT_CANCELED:
                        Toast.makeText(getBaseContext(), "SMS not delivered",
                                Toast.LENGTH_SHORT).show();
                        statusSend = "SMS not delivered";
                        break;
                }
            }
        }, new IntentFilter(DELIVERED));

        System.out.println(statusSend);

    }


    public void endActivity(View view){
        finish();
    }

    public void TestHTTP(View view){

        Userid = 12345;
        Acctype = "generic";

        String s = getSMScsv();
        APICall call = new APICall();
        call.options(webAdress, s);
        AsyncTask<String, String, String> response = call.execute();
        Log.v("TESTHTTP(View view)->", response.toString());
        SetLatestPostDate();
    }


    public void TestHTTPLatest(View view){

        if(latestPOST < newertext){
            //post latest text and everything that is after the latestPOST date
            // or maybe post everything ?

            System.out.println("====================================");
            System.out.println("There is a new message, POST sending");
            System.out.println("====================================");

            String s = getSMScsv();
            APICall call = new APICall();
            call.options(webAdress, s);
            AsyncTask<String, String, String> response = call.execute();
            Log.v("TESTHTTP(View view)->", response.toString());


            SetLatestPostDate();

        } else {
            System.out.println("====================================");
            System.out.println("No new message");
            System.out.println("====================================");
        }
        System.out.println("curentdate: " + curentdate);
    }

    // Will depreciate later ~ Ari
    private String getSMScsv() {
        StringBuilder sbuffer = new StringBuilder();
        sbuffer.append("number,time,body");

        //need to catch if empty or not ~ Extra
        Cursor c = getContentResolver().query(Uri.parse("content://sms/sent"), null, null, null, null);
        /*int isnull = 0;
        isnull = c.getCount();
*/

        if (c.moveToFirst()) {
            Integer limit = Math.min(c.getCount(), 1000);
            Log.v("SMSCSV->", "Text Message Retreived = " + Integer.toString(limit));
            for (int i = 0; i < limit; i++) {
                String body = "," + c.getString(c.getColumnIndex("body"));
                String number = "\n" + c.getString(c.getColumnIndexOrThrow("address"));
                String date = "," + c.getString(c.getColumnIndexOrThrow("date"));

                sbuffer.append(number).append(date).append(body);
                c.moveToNext();
            }
        } else
            sbuffer.append(' ');
        c.close();
        return sbuffer.toString();

    }

    private void SetLatestPostDate(){
        String date2bstored = "";
        date2bstored = date2bstored.valueOf(curentdate);

        SharedPreferences.Editor editor = PostDate.edit();
        editor.putString("date2bstored", date2bstored);
        editor.commit();
    }
}