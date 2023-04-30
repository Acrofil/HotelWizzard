from database_insert import CreateData

class Client:
    def __init__(self, personal_id, first_name, last_name, phone, email):
        self._personal_id = personal_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        
    def get_personal_id(self):
        return self._personal_id
    
    def get_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_phone(self):
        return self._phone
    
    def get_email(self):
        return self._email
    
    
    def __str__(self):
        return f'"{self._first_name} {self._last_name}"'
    
