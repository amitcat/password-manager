from datetime import date
import sqlite3
from sqlite3 import Error

name = "from new page" #getting name fron user
age = 25 # getting age from user
gender = "male" #getting name fron user
nationality = "IL" #getting name fron user
create_users = f""" 
    INSERT INTO
      users (name, age, gender, nationality, enteredDate)
    VALUES
      ('{name}', {age}, '{gender}', '{nationality}', '{date.today()}');
    """
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection('sm_app.sqlite')  # create the Connection DB

execute_query(connection, create_users) # creating user
