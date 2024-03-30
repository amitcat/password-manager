import random
import sqlite3
from sqlite3 import Error
from datetime import date


def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    symbols = '?!$#*;/,._-'
    all_together = lower + upper + symbols
    pass_length = 16
    new_password = "".join(random.sample(all_together, pass_length))
    return new_password

class Database:
    def __init__(self) -> None:
        self.database = 'password_manager_db.sqlite'
    
    def connect_to_db(self):
        '''creates connection to the database'''
        conn = sqlite3.connect(self.database)
        return (conn ,conn.cursor())


    def create_user_table(self):
        '''creates the user table'''
        conn, cursor = self.connect_to_db()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                Username TEXT PRIMARY KEY NOT NULL,
                Password TEXT NOT NULL,
                EnteredDate TEXT
                
            );
        ''')
        conn.commit()
        conn.close()
        
    def insert_user(self, user_name, password):
        '''inserts a new user to the users table'''
        output_message = 'ok'
        if self.check_user(user_name):
            print('already exists')
            output_message = 'problem'
        else:
            print('after')
            self.create_user_table()
            conn, cursor = self.connect_to_db()
            cursor.execute(f'''
                INSERT INTO 
                    users (Username, Password, EnteredDate)
                VALUES 
                    ('{user_name}', '{password}', '{date.today()}')
            ''')
            conn.commit()
            conn.close()
        return output_message
    def check_user(self, user_name):
        '''checks if a certain user is in the users table'''
        self.create_user_table()
        conn, cursor = self.connect_to_db()
        cursor.execute(f'''
            SELECT * FROM users WHERE Username= '{user_name}'
        ''')
        result = cursor.fetchone()

        conn.commit()
        conn.close()

        return result
    
    def create_password_to_webs_table(self):
        '''creates password to web table if not exists'''
        conn, cursor = self.connect_to_db()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwordtable (
                Username TEXT PRIMARY KEY NOT NULL,
                Web TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

