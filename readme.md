# HOTEL MANAGER CLI APPLICATION ------------ HOTEL WIZZARD ------------

This is my personal project that i'am building. Starting date of the project is 19.04.2023
The project is intendet for the front end and back end office for the hotel managment, not for direct client use. 

This project is created with the intention to practice OOP programming, inheritance, encapsulation, abstraction. Practicing also SQLite3 and SQL in general. Trying to keep everything organised and modular for testing and readability.
The program will cover the CRUD - Create, Read, Update and Delete 
The project is created with the intention to have real life usage and i do have plans on adding more features. For now starting slow and will see where will it go. I will be updating the readme with the changes.

# What is my plan for the stages the program will be going is:

- [x] Create simple program using SQLite3 to store clients and reservations in their tables and link them together. 
- [] Search for Reservation by specific criterias
- [] Show all reservations
- [] Edit client
- [] Edit reservation
- [] Delete Client
- [] Delete Reservation

- [] Add the option to create custom rate plans
- [] Add extra fees that can be applyed to the reservation when making it
- [] Add bill to the client

- [] Check availability for the specific dates the client wants to make reservation

- [] Check for arrivals for the current day
- [] Check for departures for the current day

- [] Get airport data for plane landing times

- [] Add csv filename and auto create new client if non-existent and add the reservation.

# Program Structure

## User interface / menu
- [1] Add New Reservation
- [2] Search for Reservation/s
- [2.1] From Date to Date
- [2.2] Search by Reservation Number
- [2.3] Search by Client First and Last name's
- [3] Show all reservations
- [4] Edit Reservation
- [5] Edit Client
- [6] Delete Client
- [7] Delete Reservation
- [0] Exit Program



The user should not have direct acces to client and reservation properties. Except when the correct menu option is selected.


# Program structure - Add links to the files later

- [main]
- [hotel_manager.py]
- [clients.py]
- [reservatuibs.py]
- [database.py]
- [data.db]
- [tables.sql]

# SQLite3 Database Structure

Will add visualisation later
For now there are 3 tables
clients, reservations and person_reservation that links each person to their reservation.


# Update v.0 , 20.04.2023
The program succesfully adds clients and reservations to database and links them together
