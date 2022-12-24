CREATE TABLE IF NOT EXISTS users(
id integer PRIMARY KEY AUTOINCREMENT,
email text NOT NULL,
name text NOT NULL,
password text NOT NULL,
avatar BLOB DEFAULT NULL,
time integer NOT NULL
);


CREATE TABLE IF NOT EXISTS books(
id integer PRIMARY KEY AUTOINCREMENT,
book text NOT NULL,
photo text NOT NULL,
txt text DEFAULT NULL
);