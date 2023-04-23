CREATE TABLE IF NOT EXISTS clients (
    id_client INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    PRIMARY KEY (id_client)
);

CREATE TABLE IF NOT EXISTS reservations (
    id_reservation INTEGER NOT NULL,
    reservation_number INTEGER NOT NULL,
    checkin_date TEXT NOT NULL,
    checkout_date TEXT NOT NULL,
    total_days TEXT NOT NULL,
    date_created TEXT,
    PRIMARY KEY (id_reservation)
);

CREATE TABLE IF NOT EXISTS person_reservation (
    id_person INTEGER NOT NULL,
    id_person_reservation INTEGER NOT NULL,
    FOREIGN KEY (id_person) REFERENCES clients(id_client),
    FOREIGN KEY (id_person_reservation) REFERENCES reservations(id_reservation)
);
