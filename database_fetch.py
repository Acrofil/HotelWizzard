from connect_database import DatabaseConnection
import pandas as pd

class ReadData(DatabaseConnection):
    def __init__(self):
        super().__init__()


    def get_client(self, first_name, last_name):
        self.open_connection()

        client_search_q = "SELECT * FROM clients WHERE first_name = (?) COLLATE NOCASE AND last_name = (?) COLLATE NOCASE"

        client_first_name = first_name
        client_last_name = last_name

        sql_query = pd.read_sql(client_search_q, self.conn, params=(client_first_name, client_last_name))
        df = pd.DataFrame(sql_query, columns = ['id_client', 'client_personal_id', 'first_name', 'last_name','phone','email'])

        self.close_connection()
        
        return df


    def search_reservation(self):
        pass
    
    def update_reservation(self):
        pass

    def delete_reservation(self):
        pass
        

            

    
    
