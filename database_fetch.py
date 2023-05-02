from connect_database import DatabaseConnection
import pandas as pd

class ReadData(DatabaseConnection):
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

        
    def update_reservation(self):
        pass

    def delete_reservation(self):
        pass
        

            

    
    
