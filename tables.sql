CREATE TABLE IF NOT EXISTS clients (
    id_client INTEGER NOT NULL,
    first_name TEXT,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    PRIMARY KEY (id_client)
);

CREATE TABLE IF NOT EXISTS reservations (
    id_reservation INTEGER NOT NULL,
    reservation_number INTEGER NOT NULL,
    checkin_date TEXT,
    checkout_date TEXT,
    total_days TEXT,
    date_created TEXT,
    PRIMARY KEY (id_reservation)
);

CREATE TABLE IF NOT EXISTS client_bill (
    id_bill INTEGER NOT NULL,
    bill_sum TEXT,
    PRIMARY KEY (id_bill)
);

CREATE TABLE IF NOT EXISTS person_reservation (
    id_person INTEGER NOT NULL,
    id_person_reservation INTEGER NOT NULL,
    FOREIGN KEY (id_person) REFERENCES clients(id_client),
    FOREIGN KEY (id_person_reservation) REFERENCES reservations(id_reservation)
);
