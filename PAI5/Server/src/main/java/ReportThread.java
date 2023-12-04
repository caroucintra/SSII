import java.io.*;

public class ReportThread implements Runnable {
    private Thread t;
    private String threadName;

    private static int month = 1;
    private static int year = 1;
    private Database db;

    ReportThread( String name, Database database) {
        threadName = name;
        this.db = database;
        System.out.println("Creating " +  threadName);
    }

    public void run() {
        try {
            PrintWriter out = new PrintWriter("report.txt");
            while (true) {
                Thread.sleep(1 * 1000 * 60);

                double[] ratios = db.getAllPetitions();
                char tend;
                if ((ratios[0] == ratios[1]) && (ratios[0] == ratios[2])) {
                    tend = '0';
                } else if ((ratios[1] > ratios[0]) || (ratios[2] > ratios[0])) {
                    tend = '-';
                } else {
                    tend = '+';
                }

                if (year == 1 && (month == 1 || month == 2)) {
                    tend = '0';
                }

                out.println("Month: " + month + " | Year: " + year + " | Ratio current month: " + String.format("%.3f", ratios[0]) + " | Tendency: " + tend);
                out.flush();
                month++;
                if (month == 13) {
                    year++;
                    month = 1;
                }
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

    }


    public void start () {
        System.out.println("Starting " +  threadName );
        if (t == null) {
            t = new Thread (this, threadName);
            t.start();
        }
    }
}