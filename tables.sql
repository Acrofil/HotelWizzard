CREATE TABLE IF NOT EXISTS clients (
    id_client INTEGER NOT NULL,
    client_personal_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    PRIMARY KEY (id_client)
);

CREATE TABLE IF NOT EXISTS reservations (
    id_reservation INTEGER NOT NULL,
    reservation_number INTEGER NOT NULL,
    titular_first_name TEXT,
    titular_last_name TEXT,
    checkin_date DATE NOT NULL,
    checkout_date DATE NOT NULL,
    total_days DATE NOT NULL,
    date_created DATE,
    PRIMARY KEY (id_reservation)
);

CREATE TABLE IF NOT EXISTS person_reservation (
    id_person INTEGER NOT NULL,
    id_person_reservation INTEGER NOT NULL,
    FOREIGN KEY (id_person) REFERENCES clients(id_client),
    FOREIGN KEY (id_person_reservation) REFERENCES reservations(id_reservation)
);
