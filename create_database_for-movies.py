import sqlite3

connection = sqlite3.connect('movie_database')
cursor = connection.cursor()

sql_command = """CREATE TABLE sample"""
cursor.execute(sql_command)
connection.close()
