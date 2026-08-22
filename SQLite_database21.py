# Database connection
import sqlite3
from fastapi import FastAPI

app = FastAPI()

conn = sqlite3.connect("test.db", check_same_thread= False) # store database inside test.db | also create db file

cursor = conn.cursor() # cursor -> A cursor is used to execute SQL queries and interact with the database.

# Create own table
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed TEXT
    )               
""")

conn.commit()

@app.get("/")
def home():
    return {
        "message": "SQLite Connected fine"
    }



# After running this code, a file named test.db will be created.
