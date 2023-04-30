import random
from datetime import date, datetime
from clients import Client
from reservations import Reservation
from database_insert import CreateData
from database_fetch import ReadData
import re
import pandas as pd
from tabulate import tabulate

class HotelManager:
    def __init__(self):
        self._data = CreateData()
        self._search_data = ReadData()

    def create_client(self):
        self.first_name = input("Input first name of the Client: ")
        self.last_name = input("Input last name of the Client: ")

        correct_name_input = self.validate_name_input()
        if not correct_name_input:
            return

        self.phone = input("Phone number: ")

        correct_phone_input = self.validate_phone()
        if not correct_phone_input:
            return

        self.email = input("Email: ")

        correct_email_input = self.validate_email()
        if not correct_email_input:
            return
        
        # Generates id number with current date and time
        # Will be looking for a better solution to generate Unique id later in development storing ids in csv.
        client_personal_id = datetime.now().strftime('%Y%m%d%H%M%S')
      
        # Client object
        client = Client(client_personal_id, self.first_name, self.last_name, self.phone, self.email)
        add_client = self._data.add_client_to_database(client)

        if add_client:
            print(f"\n Client {client} created and added to the database successfully!")

    def create_reservation(self):
        self.first_name = input("\nReservation titular first name: ")
        self.last_name = input("Reservation titular last name: ")

        correct_name_input = self.validate_name_input()

        if not correct_name_input:
            return
        
        titular_in_database = self.check_db_client_exists()

        if not titular_in_database:
            return
        
        self.cin = input("Enter check in date D-M-Y: ")
        self.cot = input("Enter check out date D-M-Y: ")

        reservation_date = datetime.now().strftime('%Y%m%d%H%M%S')
        self.reservation_number = random.randint(1000, 9999) + int(reservation_date)

        try:
            self.check_in = datetime.strptime(self.cin, '%d-%m-%Y').date()
            self.check_out = datetime.strptime(self.cot, '%d-%m-%Y').date()
        except ValueError:
            print("\nDate is not the correct format! The format is DAY-MONTH-YEAR")
            return
        
        present = datetime.now()

        # Check if the selected dates are not in the past
        if self.check_in < present.date() and self.check_out < present.date():
            print("\nNot a valid date! Be sure to select date greater than today's date")
            return
        
        total_stay = abs(self.check_in - self.check_out)

        if total_stay.days <= 0:
            print("The minimum possible days to stay is 1 day!")
            return
        
        # Reservation object
        reservation = Reservation(self.reservation_number, self.first_name, self.last_name, self.check_in, self.check_out, total_stay.days)
        add_reservation = self._data.add_reservation_to_database(reservation)

        if add_reservation:
            print(f"\nReservation {reservation} added successfully!")
    
    def check_db_client_exists(self):
        
        # Search database for first and last name matches and return all data that match
        data = self._search_data.get_client(self.first_name, self.last_name)

        # If 0 == no match. Add it or Quit
        if len(data) <= 0:
            print("\nReservation titular is not in the Client's list. Would you like to add it?"
                "\n 1. Yes"
                "\n 2. No")
            choice = input("Choice: ")

            if choice == '1':
                self.create_client()
                self.create_reservation()
            elif choice == '2':
                return False

        # If > 0 we have data. Print all data    
        elif len(data) > 0:

            print("\n---------------------------  Clients Search  ---------------------------")
            print(f"\nThis are the Clients that match the reservation titular - {self.first_name} {self.last_name}")
            print()

            print(tabulate(data.set_index('id_client'), headers='keys', tablefmt='psql'))
            print()

            print("Please input the id_client number to add as titular of the reservation - 0 to exit.")
            
            try:
                client_id_input = int(input("\nClient Id: "))
            
            except ValueError:
                print("\nUse only numbers!")
                return

            if str(client_id_input) == '0':
                return False

            # Get all data that matches the given ID
            client_names = data[data["id_client"] == client_id_input]

            # Get the index
            index = client_names.index  

            # The index will always be at index[0]
            try:
                self.first_name = client_names.at[index[0], 'first_name']
                self.last_name = client_names.at[index[0], 'last_name']
            except IndexError:
                print("\n Not the correct id_client!")
                return

            # first and last name are set return True and continue with creating reservation
            return True
        
        elif len(data) == 1:
            client_names = data[data["first_name", 'last_name'] == self.first_name, self.last_name]
            index = client_names.index

            self.first_name = client_names.at[index[0], 'first_name']
            self.last_name = client_names.at[index[0], 'last_name']

            return True
    
    def validate_name_input(self):
        # Regex patterns to check for correct input
        name_pattern = '^[A-Za-z]+$'
        if not re.match(name_pattern, self.first_name) and not re.match(name_pattern, self.last_name):
            print("\n Only letters supported a-z/A-Z!")
            return False
    
        return True
    
    def validate_phone(self):
        phone_pattern = '^(?:[+\d].*\d|\d)$'
        if not re.match(phone_pattern, self.phone):
            print("\n Only digits and + sign supported!")
            return False
        
        return True
    
    def validate_email(self):
        email_pattern = '^\S+@\S+$'
        if not re.match(email_pattern, self.email):
            print("\n Incorect email address!")
            return False
        
        return True


    def add_reservation_holder(self, client, reservation):
        self._data.add_reservation_holder_to_database(self.client, self.reservation)