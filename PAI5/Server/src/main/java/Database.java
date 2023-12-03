import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Database{
    public static void connect() {
        Connection conn = null;
        try {
            Class.forName("org.sqlite.JDBC");

            // db parameters
            String url = "jdbc:sqlite:C:\\Scotti_Scholter_Marichal\\UniversityMannheim\\Wirtschaftsinformatik\\5_Sevilla Semester\\SSII\\PAIs\\SSII\\PAI5\\Server\\src\\main\\java\\data.db";
            // create a connection to the database
            conn = DriverManager.getConnection(url);

            System.out.println("Connection to SQLite has been established.");

        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException ex) {
                System.out.println(ex.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        connect();
    }
}