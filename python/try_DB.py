import sqlite3
from sqlite3 import Error
from datetime import date



def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    return []


connection = create_connection('sm_app.sqlite')  # create the Connection DB
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT,
  enteredDate TEXT
);
"""

# adding to the table
name = "amit" #getting name fron user
age = 25 # getting age from user
gender = "male" #getting name fron user
nationality = "IL" #getting name fron user
create_users = f""" 
    INSERT INTO
      users (name, age, gender, nationality, enteredDate)
    VALUES
      ('{name}', {age}, '{gender}', '{nationality}', '{date.today()}');
    """
new_name = "bla"
update_post_description = f"""
UPDATE
  users
SET
  name = "{new_name}"
WHERE
  age  = 35
"""

# execute_query(connection, create_users_table)  # creating table

# execute_query(connection, update_post_description)  # Updating

execute_query(connection, create_users) # creating user
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users) # returning list of users

for user in users:
    print(user)
