# # # import socket
# # # my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # # print ("before send")
# # # my_socket.sendto('stok'.encode(), ('127.0.0.1',8201))
# # # print ("after send")
# # # (data, remote_address) = my_socket.recvfrom(1024)
# # # print('The server sent: ' + data.decode())
# # # my_socket.close()
# # # def main():
# # #         print('hello')

# # # def run_client():
# # #     main()

# # # run_client()
# # from tkinter import *
# # from tkinter import messagebox
# # class Client_gui:
# #     def __init__(self) -> None:
# #         self.user = ''
# #         self.pword = ''


# #     def run(self):
# #         self.log_in_screen()

# #     def log_in_screen(self):
# #         root=Tk()
# #         root.title('Log in')
# #         root.geometry('925x500+300+200')
# #         root.configure(bg="#fff")
# #         root.resizable(False,False)

# #         def signin():
# #             self.user = user.get()
# #             self.pword = pword.get()
# #             print(self.user)
# #             #בדיקה של משתמש
# #             if self.user == 'amit' and self.pword =='hi': #קיים בטבלה- ממשיך הלאה
# #                 messagebox.showinfo("login", 'you are now signed in')
# #                 root.destroy()
# #                 # self.main_screen()


# #             else: #לא קיים בטבלה- מכניס לטבלה וממשיך הלאה
# #                 messagebox.showerror('login' , 'your username or password was incorect')

# #         # def check_info_and_DB (self):
# #         #     pass

# #         img_src = r"C:\Users\amitk\OneDrive\Desktop\all\python\password_manager_project\images\login.png"
# #         img = PhotoImage(file= img_src)
# #         Label(root, image=img, bg='white').place(x=50,y=50)

# #         frame = Frame(root,width=350, height=350 , bg="white")
# #         frame.place(x=480,y=70)

# #         heading = Label(frame,text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
# #         heading.place(x=100,y=5)
        
# #         # place for username
# #         def on_enter_uname(e):
# #             user.delete(0,'end')

# #         def on_leave_uname(e):
# #             uname = user.get()
# #             if uname =='':
# #                 user.insert(0,'Username')

# #         user = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
# #         user.place(x=30,y=80)
# #         user.insert(0,'Username')
# #         user.bind('<FocusIn>', on_enter_uname)
# #         user.bind('<FocusOut>', on_leave_uname)

        
# #         Frame(frame,width=295, height=2, bg='black').place(x=25,y=107)

# #         # place for password
# #         def on_enter_pass(e):
# #             pword.delete(0,'end')

# #         def on_leave_pass(e):
# #             password = pword.get()
# #             if password =='':
# #                 pword.insert(0,'Password')

# #         pword = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
# #         pword.place(x=30,y=150)
# #         pword.insert(0,'Password')
# #         pword.bind('<FocusIn>', on_enter_pass)
# #         pword.bind('<FocusOut>', on_leave_pass)

       
        
# #         Frame(frame,width=295, height=2, bg='black').place(x=25,y=177)
# #         Button(frame,width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0 , command=signin).place(x=35,y=204)
# #         string_name = str(self.user)
# #         string_password = str(self.pword)

# #         def get_uname_and_pass():
# #             return f'{string_name} {string_password}'




# #         root.mainloop()
# #         return get_uname_and_pass()
    
# #     # def get_all(self):
# #     #     return f'{self.user} {self.pword}'

# #     def main_screen(self):
# #         root=Tk()
# #         root.title('Log in')
# #         root.geometry('925x500+300+200')
# #         root.configure(bg="#fff")
# #         root.resizable(False,False)

# #         root.mainloop()

# # g = Client_gui()
# # g.log_in_screen()
# # print(g.user)
# import hashlib
# word = 'hello'
# password = bytes(word, 'utf-8')
# unername_password = f'{hashlib.sha256(password).hexdigest()}'
# print(unername_password)


# request = ['c', '', 'p', 'd', 'np']
# print(request)
# request = 'next'.join(request)
# print(request)
# command , username , password, domain , new_pass = request.split("next")
# print(command, username, password, domain, new_pass)
# a = b'sdsdsd'
# print(str(a))

# a = '1||2||3||4||5'
# print(a.split('||'))

from cryptography.fernet import Fernet
# KEY = Fernet.generate_key()
# CIPHER_SUITE = Fernet(KEY)
# print('key >>>>>>',KEY)
# print(CIPHER_SUITE)
# password = 'hello'.encode()
# e_password = CIPHER_SUITE.encrypt(password).decode()
# print(type(e_password))
# print('now >>>')
# d_password = CIPHER_SUITE.decrypt(e_password.encode())
# print(d_password.decode())


# from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# key =RSA.generate(1024)
# public_key = key.publickey()
# private_key = key
# msg = 'hello'
# cipher = PKCS1_OAEP.new(public_key)
# ciphertext = cipher.encrypt(msg.encode())
# # print(ciphertext)
# cipher = PKCS1_OAEP.new(private_key)
# plaintext = cipher.decrypt(ciphertext).decode()
# print(plaintext)
# print(public_key)
# print(private_key)

# print (cipher)
# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
# c = A()
# print(c.a)




class Encryption:
    def __init__(self):
        self.key =RSA.generate(1024)
        self.public_key = self.key.publickey()
        self.private_key = self.key
        # self.key_for_password = Fernet.generate_key()

    
    def export_public_key(self):
        return self.public_key.export_key()
    
    def encrypt(self, plaintext , public_key):
        # Implement code to encrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(public_key)
        chunk_size = 86 
        ciphertext = b""
        
        for i in range(0, len(plaintext),chunk_size ): # Encrypt in chunks
            chunk = plaintext[i:i + chunk_size]
            print(f'{chunk=}, {i=}')
            encrypted_chunk = cipher.encrypt(chunk)
            ciphertext += encrypted_chunk

        return ciphertext
        # ciphertext = cipher.encrypt(plaintext.encode())
        # return ciphertext
    
    def decrypt(self, ciphertext):
        # Implement code to decrypt ciphertext using symmetric encryption
        cipher = PKCS1_OAEP.new(self.private_key)
        chunk_size = 128
        plaintext = b""
        

        for i in range(0, len(ciphertext), chunk_size): # Decrypt in chunks
            chunk = ciphertext[i:i + chunk_size]
            decrypted_chunk = cipher.decrypt(chunk)
            plaintext += decrypted_chunk

        plaintext = plaintext.decode()
        return plaintext
        # plaintext = cipher.decrypt(ciphertext).decode()
        # return plaintext
    # def encrypt_password(self, password):
    #     cipher = Fernet(self.key_for_password)
    #     encrypted_password = cipher.encrypt(password.encode())
    #     return encrypted_password.decode()

    # def decrypt_password(self, encrypted_password):
    #     cipher = Fernet(self.key_for_password)
    #     decrypted_password = cipher.decrypt(encrypted_password).decode()
    #     return decrypted_password
    

class Client:
    def __init__(self) -> None:
        self.encryption = Encryption()
class b:
    def __init__(self, a) -> None:
        self.client = Client()
        self.hi = a
    def s(self, msg):
        self.hi = self.client.encryption.encrypt(msg, self.hi)
        return self.hi
    
# one = Encryption()
# two = b(RSA.import_key(one.export_public_key()))

# msg = 'ased'
# # encry_msg = two.client.encryption.encrypt_password(msg)
# # print(encry_msg)
# ciphertext = two.s(msg.encode())
# print(ciphertext)
# if '|||' in str(ciphertext):
#     print(str(ciphertext).index('|||'))
# # print(len(ciphertext))
# plaintext = one.decrypt(b'\x88\xc5C#\x17')
# # decry_msg = two.client.encryption.decrypt_password(plaintext)
# print(plaintext)
# msg = str('hi'.encode())
# for i in msg[2:-1]:
#     print(i, end='')

# dic = {}
# dic['a'] = 'hello'
# if 'b' not in dic.keys():
#     print('true')
# print(dic)


