import datetime
import sqlite3

# Queries for the application 
CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_date REAL,
    watched INTEGER
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_date, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"

connection = sqlite3.connect("data.db")