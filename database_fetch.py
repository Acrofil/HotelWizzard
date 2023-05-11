from connect_database import DatabaseConnection
from database_insert import CreateData
import pandas as pd

class ReadData(CreateData):
    def __init__(self):
        super().__init__()

        pass
    
    def get_all_clients(self):
        self.open_connection()

        client_search_q = "SELECT * FROM clients"

        sql_query = pd.read_sql(client_search_q, self.conn)
        df = pd.DataFrame(sql_query, columns= ['id_client', 'client_personal_id', 'first_name', 'last_name','phone','email'])

        self.close_connection()

        return df

    def get_all_reservations(self):
        self.open_connection()

        reservations_search_q = "SELECT * FROM reservations"

        sql_query = pd.read_sql(reservations_search_q, self.conn)
        df = pd.DataFrame(sql_query, columns= ['id_reservation', 'reservation_number', 'titular_first_name', 'titular_last_name', 'checkin_date', 'checkout_date', 'total_days', 'date_created'])

        self.close_connection()

        return df

    
    def get_client_data(self, search_query, search_tuple):
        self.open_connection()

        sql_query = pd.read_sql(search_query, self.conn, params=search_tuple)
        df = pd.DataFrame(sql_query, columns= ['id_client', 'client_personal_id', 'first_name', 'last_name','phone','email'])

        self.close_connection()

        return df
    
    def get_reservations_data(self, search_query, search_tuple):
        self.open_connection()

        sql_query = pd.read_sql(search_query, self.conn, params=search_tuple)
        df = pd.DataFrame(sql_query, columns= ['id_reservation', 'reservation_number', 'titular_first_name', 'titular_last_name', 'checkin_date', 'checkout_date', 'total_days', 'date_created'])

        self.close_connection()

        return df

    def search_reservation_dates(self, check_in, check_out):    
        reservation_search_q = "SELECT * FROM reservations WHERE checkin_date >= (?) AND checkout_date <= (?)"

        search_tuple = (check_in, check_out)

        df = self.get_reservations_data(reservation_search_q, search_tuple)

        return df
    
    def search_reservation_titular(self, first_name, last_name):
        reservation_search_q = "SELECT * FROM reservations WHERE titular_first_name = (?) COLLATE NOCASE AND titular_last_name = (?) COLLATE NOCASE "

        search_tuple = (first_name, last_name)

        df = self.get_reservations_data(reservation_search_q, search_tuple)

        return df

    def search_reservation_number(self, number):
        reservation_search_q = "SELECT * FROM reservations WHERE reservation_number = (?)"

        search_tuple = (number,)

        df = self.get_reservations_data(reservation_search_q, search_tuple)

        return df
    

    def search_clients_names(self, first_name, last_name):
        client_search_q = "SELECT * FROM clients WHERE first_name = (?) COLLATE NOCASE AND last_name = (?) COLLATE NOCASE"

        search_tuple = (first_name, last_name)

        df = self.get_client_data(client_search_q, search_tuple)
        
        return df

    def search_clients_id(self, personal_id):
        client_search_q = "SELECT * FROM clients WHERE client_personal_id = (?)"

        search_tuple = (personal_id, )

        df = self.get_client_data(client_search_q, search_tuple)

        return df

    def search_clients_phone(self, phone_number):
        client_search_q = "SELECT * FROM clients WHERE phone = (?)"

        search_tuple = (phone_number, )

        df = self.get_client_data(client_search_q, search_tuple)

        return df
    
    def search_arrivals_or_departures_today(self, today, search_key):
        if search_key == 'arrivals':

            reservations_search_q = "SELECT * FROM reservations where checkin_date = (?)"
        
        elif search_key == 'departures':

            reservations_search_q = "SELECT * FROM reservations where checkout_date = (?)"

        search_tuple = (today, )

        df = self.get_reservations_data(reservations_search_q, search_tuple)

        return df
    
class EditData(ReadData):
    def __init__(self):
            super().__init__()
            pass


    def edit_client_data(self, client_id, first_name, last_name, phone, email):
        self.open_connection()

        client_edit_q = "UPDATE clients SET first_name = (?), last_name = (?), phone = (?), email = (?) WHERE id_client = (?)"

        client_tuple = (first_name, last_name, phone, email, client_id)

        self.cursor.execute(client_edit_q, client_tuple)
        self.conn.commit()
        self.close_connection()

    def edit_reservation_client(self, first_name, last_name, reservation_id):
        self.open_connection()

        reservation_edit_q = "UPDATE reservations SET titular_first_name = (?), titular_last_name = (?) WHERE id_reservation = (?)"
        reservation_tuple = (first_name, last_name, reservation_id)

        self.cursor.execute(reservation_edit_q, reservation_tuple)
        self.conn.commit()
        self.close_connection()
    
    def edit_reservation_dates(self, check_in, check_out, total_days, reservation_id):
        self.open_connection()

        reservation_edit_q = "UPDATE reservations SET checkin_date = (?), checkout_date = (?), total_days = (?) WHERE id_reservation = (?)"
        reservation_tuple = (check_in, check_out, total_days, reservation_id)
        self.cursor.execute(reservation_edit_q, reservation_tuple)
        self.conn.commit()
        self.close_connection()

class DeleteData(EditData):
    def __init__(self):
        super().__init__()
        pass

    def delete_client_data(self, id_client):
        self.open_connection()

        delete_client_q = "DELETE FROM clients WHERE id_client = (?)"
        delete_client_tuple = (id_client, )

        self.cursor.execute(delete_client_q, delete_client_tuple)
        self.conn.commit()
        self.close_connection()

    def delete_reservation_data(self, id_reservation):
        self.open_connection()

        delete_reservation_q = "DELETE FROM reservations WHERE id_reservation = (?)"
        delete_reservation_tuple = (id_reservation, )

        self.cursor.execute(delete_reservation_q, delete_reservation_tuple)
        self.conn.commit()
        self.close_connection()        

        
        