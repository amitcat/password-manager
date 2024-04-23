import random
import sqlite3
from sqlite3 import Error
from datetime import date
from settings import *
# start



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
            cursor.execute('''
                INSERT INTO 
                    users (Username, Password, EnteredDate)
                VALUES 
                    (?, ?, ?)
            ''', (user_name, password, date.today()))
            conn.commit()
            cursor.close()
            conn.close()
        return output_message
    
    def check_user_to_web (self,user_name,web_name):
        '''checks if a certain user already have this web in the password table'''
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        cursor.execute('''
            SELECT * FROM passwordtable WHERE Username= ? AND WebName= ?
        ''', (user_name, web_name))
        result = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return result is not None
    
    def check_user(self, user_name):
        '''checks if a certain user is in the users table'''
        self.create_user_table()
        conn, cursor = self.connect_to_db()
        cursor.execute('''
            SELECT * FROM users WHERE Username= ?
        ''', (user_name,))
        result = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return result is not None

    def check_current_password(self, user_name, web_name, current_password, encription):
        '''check if the current password is the same as the password stored in DB'''
        print('checking if the current password is the same as the password stored in DB')
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        cursor.execute('''
                SELECT PasswordToWeb FROM passwordtable WHERE Username= ? AND WebName= ?
    ''', (user_name, web_name))
        result = cursor.fetchone()[0]
        print('1')
        print('type', type(eval(result)))
        decrypted_result = encription.decrypt_msg(eval(result))
        print('2')
        decrypted_current_password = encription.decrypt_msg(eval(current_password))
        print('3')

        if decrypted_result == decrypted_current_password:
            same_password = True
        else:
            same_password = False
        
        conn.commit()
        cursor.close()
        conn.close()
        return same_password # return True if the current password is the same as the password stored in DB
        
    def check_current_password_to_new_password(self, user_name, web_name, new_password, encription):
        '''check if the current password is the same as the new password'''
        print('checking if the current password is the same as the new password')
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        cursor.execute('''
                SELECT PasswordToWeb FROM passwordtable WHERE Username= ? AND WebName= ? 
            ''', (user_name, web_name))
        same_password = None
        result = cursor.fetchone()[0]
        decrypted_result = encription.decrypt_msg(eval(result))
        print('hi ', decrypted_result)
        decrypted_new_password = encription.decrypt_msg(eval(new_password))
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
        self.create_user_table()
        conn, cursor = self.connect_to_db()
        if self.check_user(user_name):
            cursor.execute('''
                SELECT Password FROM users WHERE Username= ?
            ''', (user_name,))
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
            cursor.execute('''
                    INSERT INTO 
                        passwordtable (Username, WebName, PasswordToWeb, EnteredDate)
                    VALUES 
                        (?, ?, ? ,?)
                ''', (user_name, web_name, password_for_web ,date.today()))
            
            output_message='ok'
            conn.commit()
            cursor.close()
            conn.close()
        return output_message

    def update_password_for_web(self,user_name, web_name, current_password_for_web, new_password_for_web , encryption):
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        output_message =''
        if self.check_user_to_web(user_name,web_name):
            if self.check_current_password(user_name, web_name ,current_password_for_web, encryption):
                if not self.check_current_password_to_new_password(user_name, web_name ,new_password_for_web, encryption):

                    cursor.execute('''
                        UPDATE passwordtable
                        SET PasswordToWeb = ?, EnteredDate= ?
                        WHERE Username= ? AND WebName= ?
                    ''', (new_password_for_web, date.today(), user_name, web_name))

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
        return output_message

    def show_password_by_web (self, user_name, web_name, encryption, client_public_key):
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        output_message ='' # at the end output msg should be 'ok encrypted password' (enctypted with client public key)
        if self.check_user_to_web(user_name,web_name):
            cursor.execute('''
                        SELECT PasswordToWeb FROM passwordtable WHERE Username= ? AND WebName= ?
                    ''', (user_name, web_name))

            result_password = cursor.fetchone()[0]
            print(result_password)
            decrypted_password = encryption.decrypt_msg(eval(result_password))
            encrypted_password = encryption.encrypt_msg(decrypted_password.encode(), client_public_key)

            output_message=f'ok {encrypted_password}'

            conn.commit()
            cursor.close()
            conn.close()
        else:
            print('web not exists')
            output_message= 'web not exists'

        return output_message

    def delete_web_and_password(self,user_name, web_name):
        self.create_password_to_webs_table()
        conn, cursor = self.connect_to_db()
        if self.check_user_to_web(user_name,web_name):
            cursor.execute('''
                    DELETE FROM passwordtable WHERE Username= ? AND WebName= ?
                ''', (user_name, web_name))
            output_message='ok'
            conn.commit()
            cursor.close()
            conn.close()
        else:
            print('web not exists')
            output_message= 'web not exists'
        
        return output_message

