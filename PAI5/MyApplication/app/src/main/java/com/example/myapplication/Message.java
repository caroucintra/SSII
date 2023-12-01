package com.example.myapplication;
import java.io.Serializable;

public class Message implements Serializable{
    private static final long serialVersionUID = 1L;
    private int camas;
    private int mesas;
    private int sillas;
    private int sillones;
    private int id;

    public Message(int camas, int mesas, int sillas, int sillones, int id) {
        this.camas = camas;
        this.mesas = mesas;
        this.sillas = sillas;
        this.sillones = sillones;
        this.id = id;
    }

    public int getCamas() {
        return camas;
    }

    public int getMesas() {
        return mesas;
    }

    public int getSillas() {
        return sillas;
    }

    public int getSillones() {
        return sillones;
    }

    public int getId() {
        return id;
    }

    public void print() {
        System.out.println("Petición de material: "
                + camas + " camas, "
                + mesas + " mesas, "
                + sillas + " sillas, "
                + sillones + " sillones "
                + "con el número del cliente: " + id);
    }
}
