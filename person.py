from database import Data

class Person:
    def __init__(self, first_name, last_name, phone, email, reservation_number, start_date, end_date, reservation_made_time):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        
        self.reservation_number = reservation_number
        self.start_date = start_date
        self.end_date = end_date
        self.total_days = str(abs(start_date - end_date))
        self.reservation_made_time = reservation_made_time

        self.add_res()
    
    def get_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def add_res(self):
        self.data = Data()
        self.data.add_reservation_to_database(self.first_name, self.last_name, self.phone, self.email, self.reservation_number, self.start_date, self.end_date, self.total_days, self.reservation_made_time)
