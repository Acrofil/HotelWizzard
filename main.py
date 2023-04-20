# create main menu
# 1 add person reservation
# 2 remove person reservation
# 3 edit person reservation
# 4 remove person reservation
# 5 see all reservations

from people import PeopleReservations
from person import Person
import sqlite3
from database import Data
from datetime import datetime, date, time
import random


class Program:
    def __init__(self) -> None:
        # Create our database and database tables
        self.data = Data()
        self.data.create_tables()

    def menu(self):
        
        print("Welcome to reservation manager! Please select what task would you like to perform?"
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
        first_name = input("Please input first name of the reservation holder: ")
        last_name = input("Enter last name: ")
        phone = input("Phone number: ")
        email = input("Email: ")
        cin = input("Enter check in date D-M-Y: ")
        cot = input("Enter check out date D-M-Y: ")

        reservation_number = random.randint(1000, 9999)


        check_in = datetime.strptime(cin, '%d-%m-%Y').date()
        check_out = datetime.strptime(cot, '%d-%m-%Y').date()
        

        self.reservation = Person(first_name, last_name, phone, email, reservation_number, check_in, check_out, date.today())
        
        print("reservation added")
      
        

program = Program()
program.execute()