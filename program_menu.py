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
from hotel_manager import ManagerSearch
from hotel_manager import ManagerEdit
from hotel_manager import ManagerDelete

class Program:
    def __init__(self) -> None:
        # Create our database and database tables
        
        self._hotel_m = HotelManager()
        self._hotel_m_search = ManagerSearch()
        self._hotel_m_edit = ManagerEdit()
        self._hotel_m_delete = ManagerDelete()

    # Main menu 
    def menu(self):      
        print("\n Welcome to Hotel Wizzard! Please select what task would you like to perform?"
            "\n 1. Add Client or Reservation"
            "\n 2. Search for reservation"
            "\n 3. Search for clients"
            "\n 4. Show all arrivals today"
            "\n 5. Show all departures today"
            "\n 6. Edit or Delete Clients/Reservations"
            "\n 0. Exit program")      

    # Sub menus
    def sub_menus(self, menu_selector):
        while True:
           if menu_selector == '1':
                print("\n Please choose from available options: "
                    "\n 1. Create new Client"
                    "\n 2. Add new Reservation"
                    "\n 0. Return to main menu")
            
                self.execute_sub_menus(menu_selector)

           elif menu_selector == '2':
                print("\n Please choose from the available options:  "
                    "\n 1. Search all reservations from date to date"
                    "\n 2. Search all reservations by titular names"
                    "\n 3. Search All reservations by reservation number"
                    "\n 4. Show all reservations"
                    "\n 0. Return to main menu")
            
                self.execute_sub_menus(menu_selector)

           elif menu_selector == '3':
                print("\nPlease choose from the available options: "
                    "\n1. Search for client by first and last name"
                    "\n2. Search for client by the personal Id"
                    "\n3. Search for client by phone number"
                    "\n4. Show all Clients"
                    "\n0. Return to main menu")
                
                self.execute_sub_menus(menu_selector)

           elif menu_selector == '6':
                print("\nPlease choose from the available options: "
                    "\n1. Edit Client"
                    "\n2. Change Reservation titular"
                    "\n3. Change Reservation check in and check out dates"
                    "\n4. Delete Client"
                    "\n5. Delete Reservation"
                    "\n0. Return to main menu")
                
                self.execute_sub_menus(menu_selector)
               
    # Executing sub menus orders        
    def execute_sub_menus(self, menu_selector):
        action = input(f"\nSub-menu-{menu_selector}-input: ")

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
            elif action == '4':
                self.show_all_reservations()
            elif action == '0':
                self.execute()

        elif menu_selector == '3':
            if action == '1':
                self.search_client_names()
            elif action == '2':
                self.search_client_id()
            elif action == '3':
                self.search_client_phone()
            elif action == '4':
                self.show_all_clients()
            elif action == '0':
                self.execute()

        elif menu_selector == '6':
            if action == '1':
                self.edit_client()
            elif action == '2' or action == '3':
                self.edit_reservation(action)
            elif action == '4':
                self.delete_client()
            elif action == '0':
                self.execute()
				

    # Executing main menu orders   
    def execute(self):
        self.menu()

        while True:
            action = input("Main-menu-input: ")

            if action == '1':
                self.sub_menus(action)
            elif action == '2':
                self.sub_menus(action)
            elif action == '3':
                self.sub_menus(action)
            elif action == '4':
                self.arrivals_today()
            elif action == '5':
                self.departures_today()
            elif action == '6':
                self.sub_menus(action)		
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
    
    def search_client_names(self):
        self._hotel_m_search.search_clients_by_name()
    
    def search_client_id(self):
        self._hotel_m_search.search_clients_by_id()
    
    def search_client_phone(self):
        self._hotel_m_search.search_clients_by_phone()
    
    def show_all_clients(self):
        self._hotel_m_search.search_all_clients()
    
    def show_all_reservations(self):
        self._hotel_m_search.search_all_reservations()
    
    def arrivals_today(self):
        self._hotel_m_search.all_arrivals_today()
    
    def departures_today(self):
        self._hotel_m_search.all_departures_today()
    
    def edit_client(self):
        self._hotel_m_edit.edit_client()
    
    def edit_reservation(self, action):
        self._hotel_m_edit.edit_reservation(action)
    
    def delete_client(self):
        self._hotel_m_delete.delete_client()
   
    
    
    def add_reservation(self):
        
        self.client = self._hotel_m.create_client()
        self.reservation = self._hotel_m.create_reservation()

        self._hotel_m.add_reservation_holder(self.client, self.reservation)

        
      
        

