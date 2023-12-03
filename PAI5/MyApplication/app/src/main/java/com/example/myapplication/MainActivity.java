package com.example.myapplication;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.res.Resources;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.*;
import java.net.*;

import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Base64;

import android.os.AsyncTask;

public class MainActivity extends AppCompatActivity {

    // Setup Server information
    protected static String server = "10.0.2.2";
    protected static int port = 7070;

    private String privKeyString =
            "MIIEogIBAAKCAQBh8jFNbxObv/N07An2LJnI1TEwpKrPog3qQJQ4UgIY2n5Jes1S" +
            "l/VUDAdyrx85a8mZjkwLYBO6aL1tniIRtSikZl7CdKOhFs4HJ4yuExYMGmqBate9" +
            "vIapi5OiTjE0mSRg/mwdYhSWJyozmET9gRlrBoSyuEPCzRQeb7YrQv/6TjTKA8ON" +
            "eCDrnWIpg3EHU/EYLSZN5AUxYG1IPGTU4WzXKk0w2N7cmMeBgNoOGADjFYipwgv4" +
            "d3nITdjRvoLeyrCXhWJH+M8xm69mP4UJK3t223gGRR4VViszS1FnLudT3SMUnDSI" +
            "zibW0PRbIpv6YHMH/VQRgFb26uNSTLHnb5ojAgMBAAECggEATfgIO0Xy7AcvfKHx" +
            "hCAZA4CCueA7gTHVteZWl0bhGHvGECRLkjYZOyCgRTEWwBUH1M8rxdpjmf6K3NoG" +
            "8OWvRr+fK1jCcRfARn27RU84O8ZDhmZQ+186K3lKuudX0DEgfn3J/tH25VikBZJv" +
            "SQYd/86ej86TUl0CaQAwmdup/cyG60UD/4rsh7d7SU0G2MP2bgGAVsrVKgjNBpOV" +
            "6XqSAnnRTaUrw6Y6WCxPicjc8J3Px0Q7M4NpjPt6vmvyefBbk0o8OPxWgStReeQJ" +
            "n20Uvlj2eBX0XJWOuYhvdIWXjO2y1e47heWAEP2djUu7cOF2Zuw8gKktGQdwn/3J" +
            "p/1cwQKBgQDAMgk8HVCr+sGiiVVthKTGbhH+Fgc2FmO0OcN7CgI/y4WtVa86KykX" +
            "/9TyceEqvzk60NclT0cEagEn2C+Hjn00dktz7aMbOAAwR4VmTUWQHPpVJo+Ueh0p" +
            "ooqEe6QBWsoDUrX78QoWkKN2hFmbnzDcve+9EVJ+k2DVNqCwm8nB8QKBgQCCdkH/" +
            "quMF3zPsS6ZN1V0iglb95gRrNqxAivX2M7kSCDL9CJRxZBTx2QDx7yQgl5gdLxND" +
            "lO4XK8WNi+mPp2YAuDd4WjHTRkaaCLntGNf+CjXT4BH22BcF/Hn6MAyo27HvvS7t" +
            "JsV/Iaa7XmZEqz6gMJUa91GMz0aGtMd3cDhJUwKBgF47KhPzO45Wj4GlW+EqW69+" +
            "YAv3uOln6NKAT7uPmLK2kn/9tsAKUUeXA00rUH6o6uJPamy8hdFAN/jVIdiQoAqM" +
            "xUm9hW7e8hi5uEoEMMsLqiD9mv/tL0cujkOOa0bOwKUIdHlmINAXck21bknCry5L" +
            "YbONPqkYkS14byin+S/BAoGAKIqza84hCpwYOKAxqBJcBPNYMUKfsOmmkdAdK0tb" +
            "gd0Ga1eVOb+OOrHi90wHgBFb9gXBCMlpS84QcDJAfKHasvKMWlw9C5jVK9z2WlXU" +
            "GV/25kbFjl4MmZGiHjt8U6UiIIw73vqjeSRt+eAWC9Tje0hdramZsBZhpk7bhaRb" +
            "+X0CgYEAl4QrSnx/owY8CSSEesvJRwlpWfoJV3QhZ1fdbterfGYNYlWPZfadGuCZ" +
            "dYLt1zglaIu6igFbPl4Ty8RGW7UljQ5LxtZntSkSo32xEUedxw0WTb2+vQMAwUzy" +
            "RFYb0TKbuj/qtBStjcSzwPUClt72UNhhxXySofwi5rAAVPAI7ps=";
    private PrivateKey privateKey;
    private PublicKey publicKey;

    private PrintWriter toServer;

    private String finalMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        System.out.println("Test");
        Log.i("Test", "Test");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Generar llaves
        generateKeyPair();

        // Capturamos el boton de Enviar
        View button = findViewById(R.id.button_send);

        // Llama al listener del boton Enviar
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                showDialog();
            }
        });

        new StartClientTask().execute();


    }

    private class StartClientTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... voids) {
            startClient();
            return null;
        }
    }
    private class StartMessageTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... voids) {
            sendStringToServer();
            return null;
        }
    }

    private void sendStringToServer(){
        Log.i("6","sending string");
        MainActivity.this.toServer.print(this.finalMessage);
        MainActivity.this.toServer.flush();
        Log.i("7","sent string");

        //MainActivity.this.toServer.close();
    }

    protected void startClient() {
        Log.i("1","Client started...");
        try {
            Socket s = new Socket("10.0.2.2", 3030);
            this.toServer = new PrintWriter(s.getOutputStream());

        } catch(Exception e) {
            System.out.println(e);
        }
    }

    private void generateKeyPair() {
        try {
            /*
            KeyPairGenerator kgen = KeyPairGenerator.getInstance("RSA");
            kgen.initialize(2048);
            KeyPair keys = kgen.generateKeyPair();
            byte[] keyBytes = new byte[0];
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                keyBytes = Base64.getDecoder().decode(privKeyString.getBytes(StandardCharsets.UTF_8));
            }
            PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(keyBytes);
            KeyFactory fact = KeyFactory.getInstance("RSA");
            PrivateKey privateKey = fact.generatePrivate(keySpec);
            */

            StringBuilder pkcs8Lines = new StringBuilder();
            BufferedReader rdr = new BufferedReader(new StringReader(privKeyString));
            String line;
            while ((line = rdr.readLine()) != null) {
                pkcs8Lines.append(line);
            }

            // Base64 decode the result
            String pkcs8String = pkcs8Lines.toString();
            byte [] pkcs8Pem = pkcs8String.getBytes();


            byte [] pkcs8EncodedBytes = new byte[0];
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                pkcs8EncodedBytes = Base64.getDecoder().decode(pkcs8Pem);
            }

            // extract the private key

            PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(pkcs8EncodedBytes);

            KeyFactory kf = KeyFactory.getInstance("RSA");

            privateKey = kf.generatePrivate(keySpec);

            //privateKey = keys.getPrivate();
            //publicKey = keys.getPublic();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Creación de un cuadro de dialogo para confirmar pedido
    private void showDialog() throws Resources.NotFoundException {
        boolean flag = false;

        // 1. Extraer los datos de la vista
        String camasCantidad = extractDataFromEditText(R.id.box_camas);
        String mesasCantidad = extractDataFromEditText(R.id.box_mesas);
        String sillasCantidad = extractDataFromEditText(R.id.box_sillas);
        String sillonesCantidad = extractDataFromEditText(R.id.box_sillones);
        String clientId = extractDataFromEditText(R.id.box_nr_cliente);

        // Comprobar las entradas
        try {
            int camasInt = Integer.parseInt(camasCantidad);
            int mesasInt = Integer.parseInt(mesasCantidad);
            int sillasInt = Integer.parseInt(sillasCantidad);
            int sillonesInt = Integer.parseInt(sillonesCantidad);
            Integer.parseInt(clientId);
            if (camasInt > 300 || camasInt < 0 ||
                    mesasInt > 300 || mesasInt < 0 ||
                    sillasInt > 300 || sillasInt < 0 ||
                    sillonesInt > 300 || sillonesInt < 0
            ) {
                flag = true;
                new AlertDialog.Builder(this)
                        .setIcon(android.R.drawable.ic_dialog_alert)
                        .setTitle("Error")
                        .setMessage("Valor numérico no es válido")
                        .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int whichButton) {
                            }
                        })
                        .show();
            }
            Log.i("2", "parsing ints");
        }
        catch (NumberFormatException n){
            flag = true;
            new AlertDialog.Builder(this)
                .setIcon(android.R.drawable.ic_dialog_alert)
                .setTitle("Error")
                .setMessage("Valor numérico no es válido")
                .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int whichButton) {
                    }
            })
                .show();
        }
        if (flag) return;

        new AlertDialog.Builder(this)
                    .setTitle("Enviar")
                    .setMessage("Se va a proceder al envio")
                    .setIcon(android.R.drawable.checkbox_on_background)
                    .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {

                                // Catch ok button and send information
                                public void onClick(DialogInterface dialog, int whichButton) {

                                    // Crea objeto de Message con los informaciones
                                    Message message = new Message(
                                            Integer.parseInt(camasCantidad),
                                            Integer.parseInt(mesasCantidad),
                                            Integer.parseInt(sillasCantidad),
                                            Integer.parseInt(sillonesCantidad),
                                            Integer.parseInt(clientId)
                                    );
                                    Log.i("3", "creates messages");

                                    // 2. Firmar los datos
                                    String rawMessage = message.getMessage();
                                    String encodedSignedMessage = signData(message);
                                    finalMessage = rawMessage + ";" + encodedSignedMessage + "\n";

                                    Log.i("4", "signs messages");


                                    // 3. Enviar los datos

                                    //finalMessage = "helloooo\n";
                                    new StartMessageTask().execute();

                                    Log.i("5", "sends hello");


                                    Toast.makeText(MainActivity.this, "Petición enviada correctamente", Toast.LENGTH_LONG).show();
                                        }
                            })
                    .setNegativeButton(android.R.string.no, null)
                    .show();
        }

    // Función para extraer los datos de la vista
    private String extractDataFromEditText(int editTextId) {
        EditText editText = findViewById(editTextId);
        return editText.getText().toString();
    }

    private String signData(Message message) {
        try {
            Signature sg = Signature.getInstance("SHA256withRSA");
            sg.initSign(privateKey);

            // convertir los datos en  in bytes
            System.out.println(message.getMessage());
            byte[] dataBytes = message.getMessage().getBytes("UTF-8");

            sg.update(dataBytes);

            // generar firma
            byte[] firma = sg.sign();
            byte[] encodedBytes = new byte[0];
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                encodedBytes = Base64.getEncoder().encode(firma);
            }
            String encodedString = new String(encodedBytes);
            return encodedString;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}