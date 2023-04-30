from datetime import date, datetime

class Reservation:
    def __init__(self, reservation_number,  first_name, last_name, check_in, check_out, total_stay):
        self._reservation_number = reservation_number
        self._titular_first_name = first_name
        self._titular_last_name = last_name
        self._check_in = check_in
        self._check_out = check_out
        self._total_stay = total_stay
        self._date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    def __str__(self) -> str:
        return f"with number: {self._reservation_number} and Client: {self._titular_first_name} {self._titular_last_name} as titular"