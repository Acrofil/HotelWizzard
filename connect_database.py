import sqlite3

# Connect to database and create tables if they dont exist already
class DatabaseConnection:
    def __init__(self):
        self.filename = "tables.sql"

        self.conn = None
        self.cursor = None

        self.create_connection()
        self.create_cursor()
        self.create_tables()
    
    def create_connection(self):

        self.conn = sqlite3.connect("data.db")
        return self.conn
        

    def create_cursor(self):

        self.cursor = self.conn.cursor()
        return self.cursor

    def create_tables(self):
        
        with open(self.filename, "r") as sql_file:
            self.cursor.executescript(sql_file.read())
            self.conn.commit()
    
    def open_connection(self):

        self.conn = self.create_connection()
        self.cursor = self.create_cursor()
    
    def close_connection(self):

        self.cursor.close()
        self.conn.close()
