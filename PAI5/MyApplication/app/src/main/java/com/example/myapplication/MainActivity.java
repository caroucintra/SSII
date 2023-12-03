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

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;
import java.util.Base64;

import android.os.AsyncTask;

public class MainActivity extends AppCompatActivity {

    // Setup Server information
    protected static String server = "10.0.2.2";
    protected static int port = 7070;
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
            KeyPairGenerator kgen = KeyPairGenerator.getInstance("RSA");
            kgen.initialize(2048);
            KeyPair keys = kgen.generateKeyPair();
            privateKey = keys.getPrivate();
            publicKey = keys.getPublic();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Creación de un cuadro de dialogo para confirmar pedido
    private void showDialog() throws Resources.NotFoundException {
        //CheckBox sabanas = (CheckBox) findViewById(R.id.checkBox_camas);

        //if (!sabanas.isChecked()) {
            // Mostramos un mensaje emergente;
            //Toast.makeText(getApplicationContext(), "Selecciona al menos un elemento", Toast.LENGTH_SHORT).show();}

        new AlertDialog.Builder(this)
                    .setTitle("Enviar")
                    .setMessage("Se va a proceder al envio")
                    .setIcon(android.R.drawable.ic_dialog_alert)
                    .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {

                                // Catch ok button and send information
                                public void onClick(DialogInterface dialog, int whichButton) {

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
                                            Toast.makeText(MainActivity.this, "Valor numérico no es válido", Toast.LENGTH_SHORT).show();
                                            return;
                                        }
                                        Log.i("2", "parsing ints");
                                    }
                                    catch (NumberFormatException n){
                                        Toast.makeText(MainActivity.this, "Valor numérico no es válido", Toast.LENGTH_SHORT).show();
                                        return;
                                    }


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


                                    Toast.makeText(MainActivity.this, "Petición enviada correctamente", Toast.LENGTH_SHORT).show();
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