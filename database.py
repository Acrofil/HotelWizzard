import sqlite3

# Here  will be class for creatign the database and other classes to executing differnt querys into database
class Data:
    def __init__(self):
        self.filename = "tables.sql"

        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()

        self.create_tables()
 
    def create_tables(self):
        with open(self.filename, "r") as sql_file:
            self.cursor.executescript(sql_file.read())
            self.conn.commit()
    

    def add_reservation_to_database(self, first_name, last_name, phone, email, reservation_number, checkin_date, checkout_date, total_days, date_created):
        # Create querys to be executed
        client = "INSERT INTO clients (first_name, last_name, phone, email) VALUES (?, ?, ?, ?)"
        reservation = "INSERT INTO reservations (reservation_number, checkin_date, checkout_date, total_days, date_created) VALUES (?, ?, ?, ?, ?)"
        person_reservation = "INSERT INTO person_reservation (id_person, id_person_reservation) VALUES (?, ?)"

        # Create tuples
        client_data = (first_name, last_name, phone, email)
        reservation_data = (reservation_number, checkin_date, checkout_date, total_days, date_created)
        
        # Insert into database
        self.cursor.execute(client, client_data)
        self.cursor.execute(reservation, reservation_data)
        self.conn.commit()

        client_id = self.cursor.execute("SELECT id_client FROM clients WHERE last_name = (?)", (last_name, ))
        cl_id = self.cursor.fetchone()
        cid = cl_id[0]

        reservation_id = self.cursor.execute("SELECT id_reservation FROM reservations WHERE reservation_number = (?)", (reservation_number, ))
        res_id = self.cursor.fetchone()
        rid = res_id[0]
    

        self.cursor.execute(person_reservation, (cid, rid))

        # Commit the changes
        self.conn.commit()

        # Close cursor and connection
        self.cursor.close()
        self.conn.close()
    
    def search_reservation(self):
        pass
    
    def update_reservation(self):
        pass

    def delete_reservation(self):
        pass