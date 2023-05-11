import random
from datetime import date, datetime
from clients import Client
from reservations import Reservation
from database_insert import CreateData
from database_fetch import ReadData
from database_fetch import EditData
from database_fetch import DeleteData
import re
import pandas as pd
from tabulate import tabulate

class HotelManager:
    def __init__(self):
        self._data = CreateData()
        self._search_data = ReadData()
        self._edit_data = EditData()
        self._delete_data = DeleteData()

        self.today = date.today()

        self.check_in = None
        self.check_out = None
        self.reservation_id = None

        self.clients_search = "Clients Search"
        self.reservations_search = "Reservations Search"
        self.arrivals = "All Arrivals Today"
        self.departures = "All Departures Today"

        # Bool values for when updating reservation
        self.update_dates = False
        self.update_client = False

        # Bool/values for when updating client
        self.client_id = None
        self.update = True

    def create_client(self, update=False):
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

        if update:
            self._edit_data.edit_client_data(self.client_id, self.first_name, self.last_name, self.phone, self.email)
            return
        
        # Generates id number with current date and time
        # Will be looking for a better solution to generate Unique id later in development storing ids in csv.
        client_personal_id = datetime.now().strftime('%Y%m%d%H%M%S')
      
        # Client object
        self.client = Client(client_personal_id, self.first_name, self.last_name, self.phone, self.email)
        add_client = self._data.add_client_to_database(self.client)

        if add_client:
            print(f"\n Client {self.client} created and added to the database successfully!")

    def create_reservation(self, update_dates=False, update_client=False):
        if not update_dates:
            self.first_name = input("\nReservation titular first name: ")
            self.last_name = input("Reservation titular last name: ")

            correct_name_input = self.validate_name_input()

            if not correct_name_input:
                return
            
            titular_in_database = self.check_db_client_exists()

            if not titular_in_database:
                return
            
            if update_client:
                self._edit_data.edit_reservation_client(self.first_name, self.last_name, self.reservation_id)
                return
            
        
        self.cin = input("Enter check in date D-M-Y: ")
        self.cot = input("Enter check out date D-M-Y: ")

        correct_date_format = self.date_correct_format(self.cin, self.cot)

        if not correct_date_format:
            print("\nDate is not the correct format! The format is DAY-MONTH-YEAR")
            return
           
        # For creating reservation number
        reservation_date = datetime.now().strftime('%Y%m%d%H%M%S')
        self.reservation_number = random.randint(1000, 9999) + int(reservation_date)
        
        present = datetime.now()

        # Check if the selected dates are not in the past
        if self.check_in < present.date() and self.check_out < present.date():
            print("\nNot a valid date! Be sure to select date greater than today's date")
            return
        
        total_stay = abs(self.check_in - self.check_out)

        if total_stay.days <= 0:
            print("The minimum possible days to stay is 1 day!")
            return
        
        if update_dates:
            self._edit_data.edit_reservation_dates(self.check_in, self.check_out, total_stay.days, self.reservation_id)
            return
        
        # Reservation object
        self.reservation = Reservation(self.reservation_number, self.first_name, self.last_name, self.check_in, self.check_out, total_stay.days)
        add_reservation = self._data.add_reservation_to_database(self.reservation)

        if add_reservation:
            print(f"\nReservation {self.reservation} added successfully!")
    
    def print_reservations_search_data(self, data, print_text, action_type):

        print(f"\n---------------------------  {action_type} ---------------------------")
        print(print_text)
        print()
        print(tabulate(data.set_index('id_reservation'), headers='keys', tablefmt='psql'))
        print()
    
    def print_clients_search_data(self, data, print_text, action_type):

        print(f"\n---------------------------  {action_type}  ---------------------------")
        print(print_text)
        print()
        print(tabulate(data.set_index('id_client'), headers='keys', tablefmt='psql'))
        print()
    
    def check_db_client_exists(self):    
        # Search database for first and last name matches and return all data that match
        data = self._search_data.search_clients_names(self.first_name, self.last_name)

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
            print_text = f"\nThis are the Clients that match the reservation titular - {self.first_name} {self.last_name}"
            self.print_clients_search_data(data, print_text, self.clients_search)

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
    
    def date_correct_format(self, cin, cot):

        try:
            self.check_in = datetime.strptime(cin, '%d-%m-%Y').date()
            self.check_out = datetime.strptime(cot, '%d-%m-%Y').date()
        except ValueError:
            return False

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


class ManagerSearch(HotelManager):
    def __init__(self):
        super().__init__()
        pass

    # This will not check if the date is passed, Late will use it to search for older reservations too.
    def search_reservations_between_dates(self):
        # Ask user for starting and ending date to be used
        print("Input the Check in and Check out dates in the format D-M-Y")

        starting_date = input("\nCheck in date: ")
        end_date = input("\nCheck out date: ")

        correct_date_format = self.date_correct_format(starting_date, end_date)

        if not correct_date_format:
            print("\nDate is not the correct format! The format is DAY-MONTH-YEAR")
            return
        
        reservations_data = self._search_data.search_reservation_dates(self.check_in, self.check_out)

        if len(reservations_data) <= 0:
            print("\nThere are no reservations for the selected period!")
            return
        
        else:
            print_text = f"\nThis are the Reservations that match the selected dates for check in: {starting_date} and check out: {end_date}"
            self.print_reservations_search_data(reservations_data, print_text, self.reservations_search)
       
    def search_reservations_by_titular(self):
        print("Please input the reservation titular names")

        self.first_name = input("\nFirst name: ")
        self.last_name = input("Last name: ")

        correct_name = self.validate_name_input()

        if not correct_name:
            return
        
        reservations_data = self._search_data.search_reservation_titular(self.first_name, self.last_name)

        if len(reservations_data) <= 0:
            print("\nThere are no reservations with these names!")
            return
        
        elif len(reservations_data) > 0:
            print_text = f"\nThis are the Reservations that match the selected names for titular: {self.first_name}  {self.last_name}"
            self.print_reservations_search_data(reservations_data, print_text, self.reservations_search)
    
    def search_reservations_by_number(self):
        print("Please input the reservation number")

        number = input("\nNumber: ")

        if not number.isnumeric():
            print("Only numbers 0-9 supported!")
            return

        reservations_data = self._search_data.search_reservation_number(number)

        if len(reservations_data) <= 0:
            print(f"No reservation with number: {number}")
            return
        
        elif len(reservations_data) > 0:
            print_text = f"\nThis are the Reservations that match the selected reservation number: {number}"
            self.print_reservations_search_data(reservations_data, print_text, self.reservations_search)

    def search_clients_by_name(self):
        print("\nPlease input the client names\n")

        self.first_name = input("First name: ")
        self.last_name = input("Last name: ")

        correct_name_input = self.validate_name_input()
        if not correct_name_input:
            return

        clients_data = self._search_data.search_clients_names(self.first_name, self.last_name)

        if len(clients_data) <=0:
            print(f"There are no clients with name: {self.first_name} {self.last_name}")
            return
        
        elif len(clients_data) > 0:
            print_text = f"\nThis are the clients that match the names: {self.first_name} {self.last_name}"
            self.print_clients_search_data(clients_data, print_text, self.clients_search)


    def search_clients_by_id(self):
        print("\nPlease input the personal id of the client\n")

        self.personal_id = input("Client Personal Id: ")

        if not self.personal_id.isnumeric():
            print("\nOnly numbers 0-9 supported!")
            return
        
        clients_data = self._search_data.search_clients_id(self.personal_id)

        if len(clients_data) <= 0:
            print(f"There are no clients with name: {self.first_name} {self.last_name}")
            return
        
        elif len(clients_data) > 0:
            print_text = f"\nClient with personal id: {self.personal_id}"
            self.print_clients_search_data(clients_data, print_text, self.clients_search)

    def search_clients_by_phone(self):
        print("\n Please input the client phone number")

        self.phone = input("Phone number: ")

        correct_input = self.validate_phone()

        if not correct_input:
            return
        
        clients_data = self._search_data.search_clients_phone(self.phone)

        if len(clients_data) <= 0:
            print(f"There are no clients with phone number: {self.phone}")
            return
        
        elif len(clients_data) > 0:
            print_text = f"\nClients with phone number: {self.phone}"
            self.print_clients_search_data(clients_data, print_text, self.clients_search)

    def search_all_clients(self):
        clients_data = self._search_data.get_all_clients()
        print_text = f"\nAll clients in the database"
        self.print_clients_search_data(clients_data, print_text, self.clients_search)

    def search_all_reservations(self):
        reservations_data = self._search_data.get_all_reservations()

        print_text = f"\nAll reservations in the database"
        self.print_reservations_search_data(reservations_data, print_text, self.reservations_search)


    def all_arrivals_today(self):
        search_key = "arrivals" 
        today_arrivals = self._search_data.search_arrivals_or_departures_today(self.today, search_key)

        if len(today_arrivals) <= 0:
            print("\nThere are no arrivals today\n")
        
        else:
            print_text = f"\nToday's arrivals"
            self.print_reservations_search_data(today_arrivals, print_text, self.arrivals)
    
    def all_departures_today(self):
        search_key = "departures"
        today_departures = self._search_data.search_arrivals_or_departures_today(self.today, search_key)

        if len(today_departures) <= 0:
            print("\nThere are no departures today\n")
        
        else:
            print_text = f"\nToday's arrivals"
            self.print_reservations_search_data(today_departures, print_text, self.departures)

class ManagerEdit(ManagerSearch):
    def __init__(self):
            super().__init__()
            pass


    def edit_client(self):
        self.search_all_clients()
        print('\nPlease choose id_client to edit that client')
        self.client_id = input("Client id input: ")
        self.create_client(self.update)

    def edit_reservation(self, action):
        self.search_all_reservations()
        print("\nPlease choose id_reservation to edit that reservation")
        self.reservation_id = input("Reservation id: ")

        if not self.reservation_id.isnumeric():
            print("\nOnly Digits!")
            return

        # If 2 update reservation titular client if 3 update reservation dates
        if action == '2':
            self.update_client = True
            self.create_reservation(self.update_dates, self.update_client)
        elif action == '3':
            self.update_dates = True
            self.create_reservation(self.update_dates)

class ManagerDelete(ManagerEdit):
    def __init__(self):
        super().__init__()
        pass

    def delete_client(self):
        self.search_clients_by_name()

        client_id = input("\nInput the id_client number to delete it: ")

        if not client_id.isnumeric():
            print("Not a digit!")
            return
        
        confirm_delete = input("\nPlease type in 'DELETE': ")

        if confirm_delete == 'DELETE':
            self._delete_data.delete_client_data(client_id)
        elif confirm_delete != "DELETE":
            print("\nType DELETE to delete the client!")
            return

        