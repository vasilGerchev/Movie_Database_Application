import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
   id INTEGER PRIMARY KEY, 
   username VARCHAR(255) NOT NULL, 
   password VARCHAR(255) NOT NULL
)
""")


username1, password1 = "vasil123", hashlib.sha256("vasilpassword".encode()).hexdigest()
username2, password2 = "user123", hashlib.sha256("user123password".encode()).hexdigest()
username3, password3 = "user456", hashlib.sha256("user456password".encode()).hexdigest()
username4, password4 = "user789", hashlib.sha256("userpassword".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()

