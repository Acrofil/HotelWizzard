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
    

    #def close_connections(self):
        #self.cursor.close()
        #self.conn.close()
    
    def add_client_to_database(self, client):
        # Create querrys for client to be executed
        client_q = "INSERT INTO clients (first_name, last_name, phone, email) VALUES (?, ?, ?, ?)"

        # Create client data tuples
        client_data = (client._first_name, client._last_name, client._phone, client._email)

        # Insert into database
        self.cursor.execute(client_q, client_data)

        # Commit changes
        self.conn.commit()

        # Close connections
        
    

    def add_reservation_to_database(self, reservation):
        # Create querrys for reservation
        reservation_q = "INSERT INTO reservations (reservation_number, checkin_date, checkout_date, total_days, date_created) VALUES (?, ?, ?, ?, ?)"

        # Create reservation data tuples
        reservation_data = (reservation._reservation_number, reservation._check_in, reservation._check_out, reservation._total_stay, reservation._date_created)

        # Insert into database table
        self.cursor.execute(reservation_q, reservation_data)

        # Commit changes
        self.conn.commit()


    def add_reservation_holder_to_database(self, client, reservation):
        # Create querry to insert client id and reservation id into database
        client_reservation_q = "INSERT INTO person_reservation (id_person, id_person_reservation) VALUES (?, ?)"

        # Find the id of the client
        client_id = self.cursor.execute("SELECT id_client FROM clients WHERE last_name = (?)", (client._last_name, ))
        cl_id = self.cursor.fetchone()
        cid = cl_id[0]


        # Find the reservation id of the client
        reservation_id = self.cursor.execute("SELECT id_reservation FROM reservations WHERE reservation_number = (?)", (reservation._reservation_number, ))
        res_id = self.cursor.fetchone()
        rid = res_id[0]

        # Insert into database
        self.cursor.execute(client_reservation_q, (cid, rid))

        # Commit the changes
        self.conn.commit()

        # Close cursor and connection
        

    
    def search_reservation(self):
        pass
    
    def update_reservation(self):
        pass

    def delete_reservation(self):
        pass