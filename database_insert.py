from connect_database import DatabaseConnection

# Here  will be class for creatign the database and other classes to executing differnt querys into database
class CreateData(DatabaseConnection):
    def __init__(self):
        pass
 
    def add_client_to_database(self, client):
        # Create querrys for client to be executed
        client_q = "INSERT INTO clients (client_personal_id, first_name, last_name, phone, email) VALUES (?, ?, ?, ?, ?)"

        # Create client data tuples
        client_data = (client._personal_id, client._first_name, client._last_name, client._phone, client._email)

        # Insert into database
        self.open_connection()
        self.cursor.execute(client_q, client_data)

        # Commit changes
        self.conn.commit()
        
        self.close_connection()
        return True
         
    def add_reservation_to_database(self, reservation):
        # Create querrys for reservation
        reservation_q = "INSERT INTO reservations (reservation_number, titular_first_name, titular_last_name, checkin_date, checkout_date, total_days, date_created) VALUES (?, ?, ?, ?, ?, ?, ?)"

        # Create reservation data tuples
        reservation_data = (reservation._reservation_number, reservation._titular_first_name, reservation._titular_last_name, reservation._check_in, reservation._check_out, reservation._total_stay, reservation._date_created)

        # Insert into database table
        self.open_connection()
        self.cursor.execute(reservation_q, reservation_data)

        # Commit changes
        self.conn.commit()

        self.close_connection()
        return True

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
        
