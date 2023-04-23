# create main menu
# 1 add person reservation
# 2 remove person reservation
# 3 edit person reservation
# 4 remove person reservation
# 5 see all reservations


import sqlite3
from database_insert import Data
from datetime import datetime, date, time
from hotel_manager import HotelManager


class Program:
    def __init__(self) -> None:
        # Create our database and database tables
        self._data = Data()
        self._data.create_tables()
        
        self._hotel_m = HotelManager()

    def menu(self):
        
        print("Welcome to Hotel Wizzard! Please select what task would you like to perform?"
            "\n 1. Add new reservation"
            "\n 2. Search for reservation"
            "\n 3. Edit reservation"
            "\n 4. See all reservations"
            "\n 5. Remove reservation"
            "\n 0. Exit program")    
            
    def execute(self):
        self.menu()

        while True:
            action = input("Input: ")

            if action == '1':
                self.add_reservation()
            elif action == '2':
                pass
            elif action == '3':
                pass
            elif action == '4':
                pass
            elif action == '5':
                pass
            elif action == '0':
                break
    
    def add_reservation(self):
        
        self.client = self._hotel_m.create_client()
        self.reservation = self._hotel_m.create_reservation()

        self._hotel_m.add_reservation_holder(self.client, self.reservation)

        print("reservation added")
      
        

