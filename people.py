from clients import Person


class PeopleReservations:
    def __init__(self):
        self.__reservations = {}
    
    def add_reservation(self, first_and_last_name, phone, start_date, end_date):
        if first_and_last_name not in self.__reservations:
            start_date = start_date.split(".")
            d = start_date[0]
            m = start_date[1]
            y = start_date[2]

            end_date = end_date.split(".")
            ed = end_date[0]
            em = end_date[1]
            ey = end_date[2]

            check_in = date(day=int(d), month=int(m), year=int(y))
            check_out = date(day=int(ed), month=int(em), year=int(ey))

            reservation = Person(first_and_last_name, phone, check_in, check_out, date.today())

            self.__reservations[first_and_last_name] = []
            self.__reservations[first_and_last_name].append(reservation)
            
            return True
        
        elif first_and_last_name in self.__reservations:
            return False
    

