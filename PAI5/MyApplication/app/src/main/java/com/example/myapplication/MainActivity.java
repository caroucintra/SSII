package com.example.myapplication;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.res.Resources;
import android.os.Bundle;
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

public class MainActivity extends AppCompatActivity {

    // Setup Server information
    protected static String server = "192.168.1.133";
    protected static int port = 7070;
    private PrivateKey privateKey;
    private PublicKey publicKey;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
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
        startClient();

    }

    protected void startClient() {
        System.out.println("Client started...");
        try {
            Socket s = new Socket("localhost", 6666);
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            dout.writeUTF("Hello Server");
            dout.flush();
            dout.close();
            s.close();
        } catch(Exception e){System.out.println(e);}
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

                                    // Crea objeto de Message con los informaciones
                                    Message message = new Message(
                                            Integer.parseInt(camasCantidad),
                                            Integer.parseInt(mesasCantidad),
                                            Integer.parseInt(sillasCantidad),
                                            Integer.parseInt(sillonesCantidad),
                                            Integer.parseInt(clientId)
                                    );


                                    // 2. Firmar los datos
                                    signData(message);


                                    // 3. Enviar los datos

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

    private void signData(Message message) {
        try {
            Signature sg = Signature.getInstance("SHA256withRSA");
            sg.initSign(privateKey);

            // convertir los datos en  in bytes
            byte[] dataBytes = message.toString().getBytes("UTF-8");

            sg.update(dataBytes);

            // generar firma
            byte[] firma = sg.sign();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}