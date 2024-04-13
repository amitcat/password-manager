import random
import sqlite3
from sqlite3 import Error
from datetime import date
from settings import *




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
            self.create_user_table()
            conn, cursor = self.connect_to_db()
            cursor.execute(f'''
                INSERT INTO 
                    users (Username, Password, EnteredDate)
                VALUES 
                    ('{user_name}', '{password}', '{date.today()}')
            ''')
            conn.commit()
            cursor.close()
            conn.close()
        return output_message
    
    def check_user_to_web (self,user_name,web_name):
        '''checks if a certain user already have this web in the password table'''
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        cursor.execute(f'''
            SELECT * FROM passwordtable WHERE Username= '{user_name}' AND WebName= '{web_name}'
        ''')
        result = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return result is not None
    
    def check_user(self, user_name):
        '''checks if a certain user is in the users table'''
        self.create_user_table()
        conn, cursor = self.connect_to_db()
        cursor.execute(f'''
            SELECT * FROM users WHERE Username= '{user_name}'
        ''')
        result = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return result is not None

    def check_current_password(self, user_name, web_name, current_password, encryption):
        '''check if the current password is the same as the password stored in DB'''
        print('checking if the current password is the same as the password stored in DB')
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        cursor.execute(f'''
                SELECT PasswordToWeb FROM passwordtable WHERE Username= '{user_name}' AND WebName= '{web_name}'
    ''')
        result = cursor.fetchone()[0].encode()
        print(result)
        decrypted_result = encryption.decrypt(result)
        print(decrypted_result.decode())
        print('2')
        decrypted_current_password = encryption.decrypt(current_password)
        print('3')
        print(decrypted_result)
        print(decrypted_current_password)
        if decrypted_result == decrypted_current_password:
            same_password = True
        else:
            same_password = False
        
        conn.commit()
        cursor.close()
        conn.close()
        return same_password # return True if the current password is the same as the password stored in DB
        
    def check_current_password_to_new_password(self, user_name, web_name, new_password, encryption):
        '''check if the current password is the same as the new password'''
        print('checking if the current password is the same as the new password')
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        cursor.execute(f'''
                SELECT PasswordToWeb FROM passwordtable WHERE Username= '{user_name}' AND WebName= '{web_name}' 
            ''')
        same_password = None
        result = cursor.fetchone()[0].encode('utf-8')
        decrypted_result = encryption.decrypt(result)
        decrypted_new_password = encryption.decrypt(new_password)
        if decrypted_result == decrypted_new_password:
            same_password = True
        else:
            same_password = False
        
        conn.commit()
        cursor.close()
        conn.close()
        return same_password # return True if the current password is the same as the new password

    def login_into_the_system(self,user_name, password):
        '''check if user in the system and log him in'''
        print(self.check_user(user_name))
        self.create_user_table()
        conn, cursor = self.connect_to_db()
        if self.check_user(user_name):
            cursor.execute(f'''
                SELECT Password FROM users WHERE Username= '{user_name}'
            ''')
            result = cursor.fetchone()[0]
            if result == password:
                output_message = "ok"
            else:
                output_message= "problem"

        else:
            output_message = "not signed up"
        cursor.close()
        conn.close()
        return output_message
    
    def create_password_to_webs_table(self):
        '''creates password to web table if not exists'''
        conn, cursor = self.connect_to_db()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwordtable (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                WebName TEXT NOT NULL,
                PasswordToWeb TEXT NOT NULL,
                EnteredDate TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert_web_name_and_password(self,user_name, web_name, password_for_web):
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        # print(self.check_user_to_web(user_name,web_name)) >>> false
        if (self.check_user_to_web(user_name,web_name)):
            print('web already exists')
            output_message = 'problem'
        else:
            print(f'{user_name}  {web_name}  {password_for_web}  ')
            cursor.execute(f'''
                    INSERT INTO 
                        passwordtable (Username, WebName, PasswordToWeb, EnteredDate)
                    VALUES 
                        ('{user_name}', '{web_name}', '{password_for_web}' ,'{date.today()}')
                ''')
            
            output_message='ok'
            conn.commit()
            cursor.close()
            conn.close()
        print(output_message)
        return output_message


    def update_password_for_web(self,user_name, web_name, current_password_for_web, new_password_for_web , encryption):
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        output_message =''
        if self.check_user_to_web(user_name,web_name):
            if self.check_current_password(user_name, web_name ,current_password_for_web.encode(), encryption):
                if not self.check_current_password_to_new_password(user_name, web_name ,new_password_for_web.encode(), encryption):

                    cursor.execute(f'''
                        UPDATE passwordtable
                        SET PasswordToWeb = '{new_password_for_web}', EnteredDate= '{date.today()}'
                        WHERE Username= '{user_name}' AND WebName= '{web_name}'
                    ''')

                    output_message='ok'

                    conn.commit()
                    cursor.close()
                    conn.close()

                else:
                    print('new password is the same as the current password')
                    output_message= 'new password is the same as the current password'
            else:
                print('current password is wrong')
                output_message= 'current password is wrong'
        else:
            print('web not exists')
            output_message= 'web not exists'
        print(output_message)
        return output_message

