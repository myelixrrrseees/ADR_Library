CREATE TABLE IF NOT EXISTS users(
id integer PRIMARY KEY AUTOINCREMENT,
email text NOT NULL,
name text NOT NULL,
password text NOT NULL,
time integer NOT NULL
);