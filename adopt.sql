-- from the terminal run:
-- psql < adopt.sql

DROP DATABASE IF EXISTS adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets (
    id SERIAL PRIMARY KEY, 
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INTEGER,
    notes TEXT,
    available BOOLEAN NOT NULL DEFAULT true
);

-- seed.py doesn't work but this does
INSERT INTO pets (name, species, photo_url, age, notes, available)
VALUES
('Alvin', 'Turtle', 'URL', 57, 'old', True)