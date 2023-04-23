from database_insert import Data

class Client:
    def __init__(self, first_name, last_name, phone, email):
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        
    
    def get_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
