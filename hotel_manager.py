import random
from datetime import date, datetime
from clients import Client
from reservations import Reservation
from database import Data

class HotelManager:
    def __init__(self):
        self._data = Data()

    def create_client(self):
        self.first_name = input("Please input first name of the reservation holder: ")
        self.last_name = input("Enter last name: ")
        self.phone = input("Phone number: ")
        self.email = input("Email: ")

        # Client object
        self.client = Client(self.first_name, self.last_name, self.phone, self.email)
        self.add_client = self._data.add_client_to_database(self.client)

        return self.add_client


    def create_reservation(self):

        self.cin = input("Enter check in date D-M-Y: ")
        self.cot = input("Enter check out date D-M-Y: ")
        self.reservation_number = random.randint(1000, 9999)


        self.check_in = datetime.strptime(self.cin, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(self.cot, '%d-%m-%Y').date()
        
        # Reservation object
        self.reservation = Reservation(self.reservation_number, self.check_in, self.check_out)
        self.add_reservation = self._data.add_reservation_to_database(self.reservation)

    def add_reservation_holder(self, client, reservation):
        self._data.add_reservation_holder_to_database(self.client, self.reservation)