import hashlib
import sqlite3


def register():
    response = False
    while not response:
        response = input("If you don't have account select (N) to create one, if you already have select (Y): ").upper()
        if response not in ("Y", "N"):
            response = False
        else:
            if response == "N":
                create_username = input("Create your username: ")
                create_password = input("Create your password: ")

                conn = sqlite3.connect("userdata.db")
                cur = conn.cursor()

                cur.execute("""
                CREATE TABLE IF NOT EXISTS userdata (
                   id INTEGER PRIMARY KEY, 
                   username VARCHAR(255) NOT NULL, 
                   password VARCHAR(255) NOT NULL
                )
                """)

                username, password = create_username, hashlib.sha256(create_password.encode()).hexdigest()

                cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, password))

                conn.commit()
                conn.close()

                print("Account registered successfully!")


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

    username = input("Enter your username: ")

    # Load hashed password from the database
    cur.execute("SELECT password FROM userdata WHERE username = ?", (username,))
    result = cur.fetchone()
    if result:
        hashed_password_db = result[0]
    else:
        print("Invalid username or password. Please try again.")
        return False

    password = input("Enter your password: ")
    # Load input password and comparing it with hashed password from the database
    if hashlib.sha256(password.encode()).hexdigest() == hashed_password_db:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return False


register()
