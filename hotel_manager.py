import random
from datetime import date, datetime
from clients import Client
from reservations import Reservation
from database_insert import Data
import uuid
import re

class HotelManager:
    def __init__(self):
        self._data = Data()
        #self._program = Program()

    def create_client(self):
        first_name = input("Input first name of the Client: ")
        last_name = input("Input last name of the Client: ")

        correct_name_input = self.validate_name_input(first_name, last_name)
        if not correct_name_input:
            return

        phone = input("Phone number: ")

        correct_phone_input = self.validate_phone(phone)
        if not correct_phone_input:
            return

        email = input("Email: ")

        correct_email_input = self.validate_email(email)
        if not correct_email_input:
            return
        
        # Generates id number with current date and time
        # Will be looking for a better solution to generate Unique id later in development storing ids in csv.
        client_personal_id = datetime.now().strftime('%Y%m%d%H%M%S')
      
        # Client object
        client = Client(client_personal_id, first_name, last_name, phone, email)
        add_client = self._data.add_client_to_database(client)

        if add_client:
            print(f"\n Client {client} created and added to the database successfully!")

    def create_reservation(self):
        self.cin = input("Enter check in date D-M-Y: ")
        self.cot = input("Enter check out date D-M-Y: ")
        self.reservation_number = random.randint(1000, 9999)


        self.check_in = datetime.strptime(self.cin, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(self.cot, '%d-%m-%Y').date()
        
        # Reservation object
        self.reservation = Reservation(self.reservation_number, self.check_in, self.check_out)
        self.add_reservation = self._data.add_reservation_to_database(self.reservation)
    
    def validate_name_input(self, first_name, last_name):
        # Regex patterns to check for correct input
        name_pattern = '^[A-Za-z]+$'
        if not re.match(name_pattern, first_name) and not re.match(name_pattern, last_name):
            print("\n Only letters supported a-z/A-Z! AAAAA")
            return False
    
        return True
    
    def validate_phone(self, phone):
        phone_pattern = '^(?:[+\d].*\d|\d)$'
        if not re.match(phone_pattern, phone):
            print("\n Only digits and + sign supported!")
            return False
        
        return True
    
    def validate_email(self, email):
        email_pattern = '^\S+@\S+$'
        if not re.match(email_pattern, email):
            print("\n Incorect email address!")
            return False
        
        return True


        

    def add_reservation_holder(self, client, reservation):
        self._data.add_reservation_holder_to_database(self.client, self.reservation)