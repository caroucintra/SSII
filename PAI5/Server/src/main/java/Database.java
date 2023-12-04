import java.sql.*;
import java.util.ArrayList;
import java.util.Collections;

public class Database{
    private Connection conn;
    public void connect() {
        conn = null;
        try {
            Class.forName("org.sqlite.JDBC");

            // db parameters
            String url = "jdbc:sqlite:data.db";
            // create a connection to the database
            conn = DriverManager.getConnection(url);
            System.out.println("Connection to SQLite has been established.");

        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public String getPublicKeyForUser(int user) {
        String sql = "SELECT clave_publica FROM Empleado WHERE id_empleado = ?;";
        try (PreparedStatement pstmt = this.conn.prepareStatement(sql);){
            pstmt.setInt(1, user);
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                String publicKey = rs.getString("clave_publica");
                System.out.println(publicKey);
                rs.close();
                return publicKey;
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return "";
    }

    public boolean insertPetition(String petition, int user, boolean verification) {
        String sql = "INSERT INTO Peticion(datos_peticion, verificacion, empleado_id) VALUES(?, ?, ?)";
        try (PreparedStatement pstmt = this.conn.prepareStatement(sql);) {
            pstmt.setString(1, petition);
            pstmt.setInt(2, verification ? 1 : 0);
            pstmt.setInt(3, user);
            pstmt.executeUpdate();
            return true;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public double[] getAllPetitions() {
        String sql = "SELECT * FROM Peticion";
        try (Statement pstmt = this.conn.createStatement();){
            ResultSet rs = pstmt.executeQuery(sql);
            ArrayList<Integer> month_one = new ArrayList<>();
            ArrayList<Integer> month_two = new ArrayList<>();
            ArrayList<Integer> month_three = new ArrayList<>();
            long now = System.currentTimeMillis();
            while (rs.next()) {
                int verification = rs.getInt("verificacion");
                Timestamp ts = rs.getTimestamp("fecha");
                long then = ts.getTime();
                double minutes = (now - then) / 1000 / 60;
                if (minutes < 1) {
                    month_one.add(verification);
                } else if (minutes >= 1 && minutes < 2) {
                    month_two.add(verification);
                } else if (minutes >= 2 && minutes < 3) {
                    month_three.add(verification);
                }
            }
            rs.close();
            System.out.println(month_one);
            System.out.println(month_two);
            System.out.println(month_three);

            double ratio_one = (month_one.size() == 0) ? 0 : Collections.frequency(month_one, 1) / month_one.size();
            double ratio_two = (month_two.size() == 0) ? 0 : Collections.frequency(month_two, 1) / month_two.size();
            double ratio_three = (month_three.size() == 0) ? 0 : Collections.frequency(month_three, 1) / month_three.size();

            return new double[]{ratio_one, ratio_two, ratio_three};
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        Database db = new Database();
        db.connect();
        db.insertPetition("1,1,1,1,1", 111, true);
        db.getPublicKeyForUser(111);
        db.getAllPetitions();
    }
}