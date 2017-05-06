package fr.extragornax.drunktest;

import android.content.Context;
import android.os.AsyncTask;
import android.util.Log;
import android.widget.Toast;

import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

/**
 * Created by Ari on 3/10/2016.
 */
public class APICall extends AsyncTask<String, String, String> {
    String URL_ADR;
    String BODY;

    public static int postCode;

    private void verbose(String msg){
        Log.v("API_Call->",msg);
    }

    // TODO, add GET method
    public void options(String addr, String dt) {
        BODY = dt;
        URL_ADR = addr;
    }

    @Override
    protected String doInBackground(String... params) {
        verbose("Making Call to " + URL_ADR);
        StringBuilder responseOutput = new StringBuilder();
        try {
            // Open Connection
            verbose("Making Call to " + URL_ADR);
            URL url = new URL(URL_ADR);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Set headers
            verbose("Setting headers...");
            connection.setRequestMethod("POST");
            connection.setRequestProperty("USER-AGENT", "Mozilla/5.0");
            connection.setRequestProperty("ACCEPT-LANGUAGE", "en-US,en;0.5");
            connection.setRequestProperty("Content-Type","text/plain");
            connection.setDoOutput(true);

            // Send data
            verbose("Sending data....");
            DataOutputStream dStream = new DataOutputStream(connection.getOutputStream());
            dStream.writeBytes(BODY);
            dStream.flush();
            dStream.close();

            // Handle response
            verbose("Handling response...");
            int responseCode = connection.getResponseCode();
            final StringBuilder output = new StringBuilder("Request URL " + url);
            output.append(System.getProperty("line.separator")  + "Response Code " + responseCode);
            postCode = responseCode;
            BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String line = "";
            while((line = br.readLine()) != null ) {
                responseOutput.append(line+'\n');
            }
            br.close();
            verbose(output.toString());
            verbose(responseOutput.toString());

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (ProtocolException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return responseOutput.toString();


    }
}
