import sqlite3


def login():
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
       id INTEGER PRIMARY KEY, 
       username VARCHAR(255) NOT NULL, 
       password VARCHAR(255) NOT NULL
    )
    """)

    create_username = input("Create your username")
    create_password = input("Create your password")

    cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (create_username, create_password))

    conn.commit()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():

        print("Login successful!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return False
