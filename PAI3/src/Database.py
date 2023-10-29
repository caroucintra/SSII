import sqlite3

class Database():
    def __init__(self):
        self._conn = sqlite3.connect('cred.db')
        self._cursor = self._conn.cursor()
        print("Opened database successfully")
        self.create_tables()

    def close_cursorection(self):
        self._cursor.close()

    def create_tables(self):
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS User
         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
         name TEXT NOT NULL,
         password TEXT NOT NULL)''')
        
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS Message
         (messageId INTEGER PRIMARY KEY AUTOINCREMENT,
         message TEXT NOT NULL,
         userId INTEGER NOT NULL,
         FOREIGN KEY(userId) REFERENCES User(id))''')
        
        self._conn.commit()
        print("Tables created successfully")

    def check_credentials(self, username, password, message):
        credentials = self._cursor.execute("SELECT name, password from User WHERE name = ? AND password = ?", (username, password)).fetchone()
        insert_user = False
        if credentials == None:
            insert_user = True
        self.insert_user(username, password, message, insert_user)


    def insert_user(self, username, password, message, insert_user):
        if insert_user:
            self._cursor.execute("INSERT INTO User VALUES(NULL, ?, ?)", (username, password))
        user_id = self._cursor.execute(f"SELECT id from User WHERE (name = ? AND password = ?)", (username, password)).fetchone()
        self._cursor.execute("INSERT INTO Message VALUES (NULL, ?, ?)", (message, user_id[0]))
        self._conn.commit()


db= Database()

db.check_credentials("Hi", "pw", "this is message2")    
