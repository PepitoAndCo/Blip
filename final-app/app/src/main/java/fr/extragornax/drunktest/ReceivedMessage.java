package fr.extragornax.drunktest;

import java.util.Date;

import android.annotation.TargetApi;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;


public class ReceivedMessage extends Activity {

    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.received);
        textView = (TextView) findViewById(R.id.textview);
        //getSMSDetails();
        //ServerSend();

    }

    @TargetApi(Build.VERSION_CODES.M)
    private void getSMSDetails() {
        StringBuffer stringBuffer = new StringBuffer();
        stringBuffer.append("*********SMS History*************** :");
        Uri uri = Uri.parse("content://sms/sent");
        if(checkSelfPermission(android.Manifest.permission.READ_SMS) != PackageManager.PERMISSION_GRANTED){
            requestPermissions(new String[] {android.Manifest.permission.READ_SMS}, 123);
            return;
        }
        Cursor cursor = getContentResolver().query(uri, null, null, null, null);

        if (cursor.moveToFirst()) {
            for (int i = 0; i < cursor.getCount(); i++) {
                String body = cursor.getString(cursor.getColumnIndexOrThrow("body"));
                String number = cursor.getString(cursor.getColumnIndexOrThrow("address"));
                String date = cursor.getString(cursor.getColumnIndexOrThrow("date"));

                stringBuffer.append("\nPhone Number:--- " + number + " \nMessage Date:--- " + date + " \nMessage Body:--- " + body);
                cursor.moveToNext();
            }
            textView.setText(stringBuffer);
        }
        cursor.close();
    }



    public void NewText(View view){
        startActivity(new Intent("fr.extragornax.drunktest.TextPage"));
    }



}