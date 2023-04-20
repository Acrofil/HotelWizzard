from datetime import date

class Reservation:
    def __init__(self, reservation_number, check_in, check_out):
        self._reservation_number = reservation_number
        self._check_in = check_in
        self._check_out = check_out
        self._total_stay = str(abs(check_out - check_in))
        self._date_created = date.today()