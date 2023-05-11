# HOTEL MANAGER CLI PROGRAM ---- HOTEL WIZZARD ---- USING SQLite3 As Database.


# Readme Structure

- General Information about the Project
- How To Use
- Program Development Roadmap
- Program File Structure
- User Interface Structure
- SQLite3 Database Structure
- [Versions updates](https://github.com/Acrofil/hotel-wizzard/blob/main/VERSIONS.md)

# General Information For the Project

This is my personal project that i'am building. Starting date of the project is 19.04.2023
The project is intendet for the front end and back end office for the hotel managment in the Hotel, not for guest/client use. 

This project is created with the intention to practice OOP programming, inheritance, encapsulation, abstraction. Practicing also SQLite3 and SQL. Storing, fetching, modifying and deleting properties and values in databases in general.
Learning using Git version control and GitHub. Creating branches, working on improvements and merging them to the main repository. 
Maintaining some work flow.

Trying to keep everything organised and modular for testing and readability.
The program will cover the CRUD - Create, Read, Update and Delete 

The project is created with the intention to have real life usage/purpose and i do have plans on adding more features. 
For now starting slowly and will see where will it go. I will be updating the README with the changes i do.

# How To Use

Download all files. Run run.py. Follow the menu options.

# What is my plan for the stages that the program will be going:

- [x] Create simple program using SQLite3 to store clients and reservations in separated tables and link them together.
- [x] Create Client seaparatly and add it to the Database
- [x] Handle errors and correct user input for clients
- [x] Create Reservation separatly and add Reservation titular. 
- [x] Check if the titular is in the client list and return client info including the id with which we add it to the reservation.
- [x] If more than one client with same name return all with a promp which one to be added.
- [x] If there is no such client in the database promp for client creation. 
- [x] Handle errors and correct user input for reservations
- [x] Search reservations from date to date
- [x] Search by Reservation titular
- [x] Search by Reservation number
- [x] Search for Client by name
- [x] Search for Client by id
- [x] Search for Client by phone
- [x] Show all Clients
- [x] Show all reservations
- [x] Show all Arrivals today
- [x] Show all Departures today
- [x] Edit Client
- [x] Edit reservation dates
- [x] Edit reservation titular
- [x] Delete Client
- [x] Delete Reservation
- [] On program start up, check for Reservations that have expired - It is check out day after 12:00. Add them to other table with old Reservations and delete from the actual Reservations table.

- [] Add room types
- [] Add rooms total of each type and rooms capacity
- [] Add the option to create custom rate plans
- [] Add extra fees that can be applyed to the reservation when making it
- [] Add bill for the Client
- [] Add what the Client have paid
- [] Show whats left to be payed
- [] Add custom summ/receip to the Client bill

- [] Set cleaning interval. Set cleaning interval for specific stays lenght
- [] Get cleaning report for rooms to be cleaned today
- [] Mark room as cleaned

- [] Check availability for the specific dates the client wants to make reservation

- [] Get airport data for plane landing times

- [] Add csv filename and auto create new client if non-existent and add the reservation.
- [] On start up check for new csv files received in a directory and notify with info for all the reservations
- [] Select add from csv, input reservation id and add it to database. Repeat until all are added or force exit.

# Program file structure - Add links to the files later

- [run.py]
- [program_menu.py]
- [hotel_manager.py]
- [clients.py]
- [reservations.py]
- [connect_database.py]
- [database_insert.py]
- [database_fetch.py]
- [data.db]
- [tables.sql]

# User Interface Structure

- [1] Add Client or Reservation
- [1.1] Create Client
- [1.2] Add Reservation
- [1.0] Back to Main Menu
- [2] Search for Reservation/s
- [2.1] Search reservations from Check in to Check out
- [2.2] Search by Reservation Number
- [2.3] Search by Client First and Last name's
- [2.4] Show all reservations
- [2.0] Back to Main Menu
- [3] Search for clients
- [3.1] Search for clients by first and last name
- [3.2] Search for clients by the personal id
- [3.3] Search for clients by the phone number
- [3.4] Show all clients
- [3.0] Return to main menu
- [4] Show all arrival's today
- [5] Show all departure's today
- [6] Edit Reservation
- [7] Edit Client
- [8] Delete Client
- [9] Delete Reservation
- [0] Exit Program

The user should not have direct acces to client and reservation properties and other data. 
Except when the correct menu option is selected.

# SQLite3 Database Structure

Will add visualisation later
For now there are 3 tables
clients, reservations and person_reservation that links each person to their reservation.
