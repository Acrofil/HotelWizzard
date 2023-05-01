from connect_database import DatabaseConnection
import pandas as pd

class ReadData(DatabaseConnection):
    def __init__(self):
        super().__init__()

        pass

    def get_client(self, first_name, last_name):
        self.open_connection()

        client_search_q = "SELECT * FROM clients WHERE first_name = (?) COLLATE NOCASE AND last_name = (?) COLLATE NOCASE"

        client_first_name = first_name
        client_last_name = last_name

        sql_query = pd.read_sql(client_search_q, self.conn, params=(client_first_name, client_last_name))
        df = pd.DataFrame(sql_query, columns = ['id_client', 'client_personal_id', 'first_name', 'last_name','phone','email'])

        self.close_connection()
        
        return df
    
    def get_reservations_data(self, search_query, param_one, param_two):
        self.open_connection()

        sql_query = pd.read_sql(search_query, self.conn, params=(param_one, param_two))
        df = pd.DataFrame(sql_query, columns= ['id_reservation', 'reservation_number', 'titular_first_name', 'titular_last_name', 'checkin_date', 'checkout_date', 'total_days', 'date_created'])

        self.close_connection()

        return df

    def search_reservation_dates(self, check_in, check_out):
        
        reservation_search_q = "SELECT * FROM reservations WHERE checkin_date >= (?) AND checkout_date <= (?)"

        df = self.get_reservations_data(reservation_search_q, check_in, check_out)

        return df
    
    def search_reservation_titular(self, first_name, last_name):
        self.open_connection()

        reservation_search_q = "SELECT * FROM reservations WHERE titular_first_name = (?) COLLATE NOCASE AND titular_last_name = (?) COLLATE NOCASE "

        df = self.get_reservations_data(reservation_search_q, first_name, last_name)

        return df
    
    def update_reservation(self):
        pass

    def delete_reservation(self):
        pass
        

            

    
    
