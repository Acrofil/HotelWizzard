# create main menu
# 1 add person reservation
# 2 remove person reservation
# 3 edit person reservation
# 4 remove person reservation
# 5 see all reservations

import sys
import sqlite3
from database_insert import CreateData
from datetime import datetime, date, time
from hotel_manager import HotelManager
from hotel_manager import ManagerSearchReservations


class Program:
    def __init__(self) -> None:
        # Create our database and database tables
        
        self._hotel_m = HotelManager()
        self._hotel_m_search = ManagerSearchReservations()

    # Main menu 
    def menu(self):      
        print("\n Welcome to Hotel Wizzard! Please select what task would you like to perform?"
            "\n 1. Add Client or Reservation"
            "\n 2. Search for reservation"
            "\n 3. Edit reservation"
            "\n 4. See all reservations"
            "\n 5. Remove reservation"
            "\n 0. Exit program")    

    # Sub menus
    def sub_menus(self, choice):
        while True:
           if choice == '1':
                print("\n Please choose from available options: "
                    "\n 1. Create new Client"
                    "\n 2. Add new Reservation"
                    "\n 0. Return to main menu")
            
                self.execute_sub_menus(choice)

           elif choice == '2':
                print("\n Please choose from the available options:  "
                    "\n 1. Search all reservations from date to date"
                    "\n 2. Search all reservations by titular names"
                    "\n 3. Search All reservations by reservation number"
                    "\n 0. Return to main menu")
            
                self.execute_sub_menus(choice)
               
               


    # Executing sub menus orders        
    def execute_sub_menus(self, menu_selector):
        action = input("\nsub-menu-input: ")

        if menu_selector == '1':
            if action == '1':
                self.create_new_client()
            elif action == '2':
                self.create_new_reservation()
            elif action == '0':
                self.execute()
        
        elif menu_selector == '2':
            if action == '1':
                self.search_reservations_date()
            elif action == '2':
                self.search_reservations_titular()
            elif action == '3':
                self.search_reservations_number()
            elif action == '0':
                self.execute()

    # Executing main menu orders   
    def execute(self):
        self.menu()

        while True:
            action = input("Input: ")

            if action == '1':
                self.sub_menus(action)
            elif action == '2':
                self.sub_menus(action)
            elif action == '3':
                pass
            elif action == '4':
                pass
            elif action == '5':
                pass
            elif action == '0':
                print()
                sys.exit()
                
    def create_new_client(self):
        self._hotel_m.create_client()
    
    def create_new_reservation(self):
        self._hotel_m.create_reservation()
    
    def search_reservations_date(self):
       self._hotel_m_search.search_reservations_between_dates()
    
    def search_reservations_titular(self):
        self._hotel_m_search.search_reservations_by_titular()
    
    def search_reservations_number(self):
        self._hotel_m_search.search_reservations_by_number()
    
    def add_reservation(self):
        
        self.client = self._hotel_m.create_client()
        self.reservation = self._hotel_m.create_reservation()

        self._hotel_m.add_reservation_holder(self.client, self.reservation)

        
      
        

