from tkinter import *
from tkinter import messagebox
from client import MultiThreadedClient
from settings import *
import hashlib
import random
from cryptography.fernet import Fernet



class GUI():
    def __init__(self,client) -> None:
        # self.user = ''
        # self.pword = ''
        self.client = client
        self.top_levels = ""
        self.message = []
        self.exit = False
        self.KEY = Fernet.generate_key()
        self.CIPHER_SUITE = Fernet(self.KEY)
        
        

    #region Screens
        
    def main_screen (self):
        root = Tk()
        root.title('Main page - Pass Protector')
        root.geometry('925x500+300+200')
        root.configure(bg="#fff")
        root.resizable(False,False)

        
        heading = Label(root,text='Pass Protector', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5,rely=0.3, anchor='center')

        exit_button = Button(root, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(root))
        exit_button.place(relx=0.55, rely=0.5, anchor='center')
        signIn = Button(root, text='SignIn', bg='#57a1f8', fg='white', border=0 , command=self.login_screen)
        signIn.place(relx=0.5, rely=0.5, anchor='center')
        signUp = Button(root, text='SignUp', bg='#57a1f8', fg='white', border=0 , command=self.signup_screen)
        signUp.place(relx=0.45, rely=0.5, anchor='center')
        root.mainloop()

    def login_screen(self):
        login_root=Toplevel()
        login_root.title('Log in')
        login_root.geometry('925x500+300+200')
        login_root.configure(bg="#fff")
        login_root.resizable(False,False)

        self.top_levels = login_root


        frame = Frame(login_root,width=925, height=500 , bg="white")
        frame.place(relx=0.5,rely=0.5, anchor='center')

        heading = Label(frame,text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5, rely=0.1, anchor='center')
        
        # place for username
        def on_enter_uname(e):
            user.delete(0,'end')

        def on_leave_uname(e):
            uname = user.get()
            if uname =='':
                user.insert(0,'Username')

        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        user.place(relx=0.5, rely=0.3, anchor='center')
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter_uname)
        user.bind('<FocusOut>', on_leave_uname)


        def on_enter_pass(e):
            pword.delete(0,'end')

        def on_leave_pass(e):
            password = pword.get()
            if password =='':
                pword.insert(0,'Password')

        pword = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        pword.place(relx=0.5, rely=0.4, anchor='center')
        pword.insert(0,'Password')
        pword.bind('<FocusIn>', on_enter_pass)
        pword.bind('<FocusOut>', on_leave_pass)

       
        #the line under username and password
        user_underline = Frame(frame,width=200, height=2, bg='black')
        user_underline.place(relx=0.5, rely=0.33, anchor='center') 
        password_underline =Frame(frame,width=200, height=2, bg='black')
        password_underline.place(relx=0.5, rely=0.43, anchor='center')
        
        signin_button = Button(frame,width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0 , command=lambda : self.login(user, pword, login_root))
        signin_button.place(relx=0.5,rely=0.6, anchor='center')

        exit_button = Button(frame, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(login_root.master)) # .master
        exit_button.place(relx=0.5, rely=0.75, anchor='center')

    def signup_screen(self):
        SignUp_root=Toplevel()
        SignUp_root.title('Sign up')
        SignUp_root.geometry('925x500+300+200')
        SignUp_root.configure(bg="#fff")
        SignUp_root.resizable(False,False)

        self.top_levels = SignUp_root

        frame = Frame(SignUp_root,width=925, height=500 , bg="white")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        heading = Label(frame,text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5, rely=0.1, anchor='center')
        
        # place for username
        def on_enter_uname(e):
            user.delete(0,'end')

        def on_leave_uname(e):
            uname = user.get()
            if uname =='':
                user.insert(0,'Username')

        user = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
        user.place(relx=0.5, rely=0.3, anchor='center')
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter_uname)
        user.bind('<FocusOut>', on_leave_uname)

        
        # place for password
        def on_enter_pass(e):
            pword.delete(0,'end')

        def on_leave_pass(e):
            password = pword.get()
            if password =='':
                pword.insert(0,'Password')

        pword = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
        pword.place(relx=0.5, rely=0.4, anchor='center')
        pword.insert(0,'Password')
        pword.bind('<FocusIn>', on_enter_pass)
        pword.bind('<FocusOut>', on_leave_pass)

        def gene_pass():
            lower = 'abcdefghijklmnopqrstuvwxyz'
            upper = lower.upper()
            symbols = '?!$#*;/,._-'
            all_together = lower + upper + symbols
            pass_length = 16
            new_password = "".join(random.sample(all_together, pass_length))
            pword.delete(0,"end")
            pword.insert(0,new_password)
       
        
         #the line under username or password
        user_under_line = Frame(frame,width=200, height=2, bg='black')
        user_under_line.place(relx=0.5, rely=0.33, anchor='center') 

        password_under_line =Frame(frame,width=200, height=2, bg='black')
        password_under_line.place(relx=0.5, rely=0.43, anchor='center')

        
        generate_password_button = Button(frame, width=14, pady=7, text='Generate Password', bg='#57a1f8', fg='white', border=0, command=gene_pass)
        generate_password_button.place(relx=0.35,rely=0.6, anchor='center')

        signup_button = Button(frame,width=14, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0 , command=lambda : self.signup(user, pword, SignUp_root))
        signup_button.place(relx=0.5, rely=0.6, anchor='center')
        
        exit_button = Button(frame, width=14, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(SignUp_root.master)) # .master
        exit_button.place(relx=0.65, rely=0.6, anchor='center')
        
    def menu_screen(self, username):
        menu_root=Toplevel()
        menu_root.title('menu')
        menu_root.geometry('925x500+300+200')
        menu_root.configure(bg="#fff")
        menu_root.resizable(False,False)

        self.top_levels = menu_root

        frame = Frame(menu_root,width=925, height=500 , bg="white")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        heading = Label(frame,text='Menu', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5, rely=0.1, anchor='center')

        welcome_msg = Label(frame,text=f'welcome {username}', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',15))
        welcome_msg.place(relx=0.1, rely=0.1, anchor='center')

        functions = Label(frame,text='what are we cooking today?', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',18))
        functions.place(relx=0.5, rely=0.2, anchor='center')

        #insert a new web name and password button
        insert_func_button = Button(frame, width=17, pady=7, text='insert new password', bg='#57a1f8', fg='white', border=0,
                               command=lambda : self.insert_web_name_and_password_screen(username))
        insert_func_button.place(relx=0.5,rely=0.3,anchor='center')

        #update password for a web button
        update_func_button = Button(frame, width=17, pady=7, text='update password', bg='#57a1f8', fg='white', border=0,
                              command=lambda : self.update_password_for_web_screen(username))
        update_func_button.place(relx=0.5,rely=0.4,anchor='center')

        #show password for a web button
        show_func_button = Button(frame, width=17, pady=7, text='show password', bg='#57a1f8', fg='white', border=0,
                              command=lambda : self.show_password_by_web_screen(username))
        show_func_button.place(relx=0.5,rely=0.5,anchor='center')

        #remove web and password button
        remove_web_func_button = Button(frame, width=17, pady=7, text='remove web', bg='#57a1f8', fg='white', border=0,
                                        command=lambda : self.remove_web_and_password_screen(username))
        remove_web_func_button.place(relx=0.5,rely=0.6,anchor='center')

        log_out_button = Button(frame, width=14, pady=7, text='Log Out', bg='#57a1f8', fg='white', border=0, command=lambda : self.logout(menu_root))
        log_out_button.place(relx=0.1, rely=0.2, anchor='center')

        exit_button = Button(frame, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(menu_root.master))
        exit_button.place(relx=0.5, rely=0.75, anchor='center')

    def insert_web_name_and_password_screen(self, username): #iwnp -> shortcut
        iwnp_root=Toplevel()
        iwnp_root.title('insert new web name and password')
        iwnp_root.geometry('925x500+300+200')
        iwnp_root.configure(bg="#fff")
        iwnp_root.resizable(False,False)

        self.top_levels = iwnp_root

        frame = Frame(iwnp_root,width=925, height=500 , bg="white")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        heading = Label(frame,text='Create new web & password', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5, rely=0.1, anchor='center')

        account_msg = Label(frame,text=f'user: {username}', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',15))
        account_msg.place(relx=0.1, rely=0.1, anchor='center')

        web_name_label = Label(frame, text='enter you web name:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',13))
        web_name_label.place(relx=0.4, rely=0.3, anchor='center')

        password_label = Label(frame, text='enter you password for the web:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',13))
        password_label.place(relx=0.35, rely=0.4, anchor='center')


        web_name = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        web_name.place(relx=0.6, rely=0.3, anchor='center')

        pword = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        pword.place(relx=0.6, rely=0.4, anchor='center')

        #the line under web name and password
        web_name_underline = Frame(frame,width=200, height=2, bg='black')
        web_name_underline.place(relx=0.6, rely=0.33, anchor='center') 
        password_underline =Frame(frame,width=200, height=2, bg='black')
        password_underline.place(relx=0.6, rely=0.43, anchor='center')

        def gene_pass():
            lower = 'abcdefghijklmnopqrstuvwxyz'
            upper = lower.upper()
            symbols = '?!$#*;/,._-'
            all_together = lower + upper + symbols
            pass_length = 16
            new_password = "".join(random.sample(all_together, pass_length))
            pword.delete(0,"end")
            pword.insert(0,new_password)

        add_button = Button(frame, width=14, pady=7, text='Add', bg='#57a1f8', fg='white', border=0,
                             command=lambda : self.insert_web_name_and_password_func(username,web_name,pword,iwnp_root))
        add_button.place(relx=0.6, rely=0.6, anchor='center')

        generate_password_button = Button(frame, width=14, pady=7, text='Generate Password', bg='#57a1f8', fg='white', border=0, command=gene_pass)
        generate_password_button.place(relx=0.4, rely=0.6, anchor='center')


        log_out_button = Button(frame, width=14, pady=7, text='Log Out', bg='#57a1f8', fg='white', border=0, command=lambda : self.logout(iwnp_root))
        log_out_button.place(relx=0.1, rely=0.2, anchor='center')

        exit_button = Button(frame, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(iwnp_root.master))
        exit_button.place(relx=0.5, rely=0.75, anchor='center')

    def update_password_for_web_screen(self,username): #upfw -> shortcut
        upfw_root=Toplevel()
        upfw_root.title('update password for web')
        upfw_root.geometry('925x500+300+200')
        upfw_root.configure(bg="#fff")
        upfw_root.resizable(False,False)

        self.top_levels = upfw_root

        frame = Frame(upfw_root,width=925, height=500 , bg="white")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        heading = Label(frame,text='Update password for web', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5, rely=0.1, anchor='center')

        account_msg = Label(frame,text=f'user: {username}', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',15))
        account_msg.place(relx=0.1, rely=0.1, anchor='center')

        web_name_label = Label(frame, text='enter you web name:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',13))
        web_name_label.place(relx=0.4, rely=0.3, anchor='center')

        password_label = Label(frame, text='enter you current password for the web:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',13))
        password_label.place(relx=0.32, rely=0.4, anchor='center')

        new_password_label = Label(frame, text='enter you new password for the web:', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',13))
        new_password_label.place(relx=0.33, rely=0.5, anchor='center')


        web_name = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        web_name.place(relx=0.6, rely=0.3, anchor='center')

        pword = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        pword.place(relx=0.6, rely=0.4, anchor='center')

        new_pword = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        new_pword.place(relx=0.6, rely=0.5, anchor='center')

        #the line under web name and password
        web_name_underline = Frame(frame,width=200, height=2, bg='black')
        web_name_underline.place(relx=0.6, rely=0.33, anchor='center') 
        password_underline =Frame(frame,width=200, height=2, bg='black')
        password_underline.place(relx=0.6, rely=0.43, anchor='center')
        new_password_underline = Frame(frame,width=200, height=2, bg='black')
        new_password_underline.place(relx=0.6, rely=0.53, anchor='center')

        def gene_pass():
            lower = 'abcdefghijklmnopqrstuvwxyz'
            upper = lower.upper()
            symbols = '?!$#*;/,._-'
            all_together = lower + upper + symbols
            pass_length = 16
            new_password = "".join(random.sample(all_together, pass_length))
            pword.delete(0,"end")
            pword.insert(0,new_password)

        update_button = Button(frame, width=14, pady=7, text='Update', bg='#57a1f8', fg='white', border=0,
                             command=lambda : self.update_password_for_web(username,web_name,pword, new_pword, upfw_root))
        update_button.place(relx=0.6, rely=0.7, anchor='center')

        generate_password_button = Button(frame, width=14, pady=7, text='Generate Password', bg='#57a1f8', fg='white', border=0, command=gene_pass)
        generate_password_button.place(relx=0.4, rely=0.7, anchor='center')


        log_out_button = Button(frame, width=14, pady=7, text='Log Out', bg='#57a1f8', fg='white', border=0, command=lambda : self.logout(upfw_root))
        log_out_button.place(relx=0.1, rely=0.2, anchor='center')

        exit_button = Button(frame, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(upfw_root.master))
        exit_button.place(relx=0.5, rely=0.85, anchor='center')

    def show_password_by_web_screen(self, username): #spbw -> shortcut
        spbw_root=Toplevel()
        spbw_root.title('show password by web')
        spbw_root.geometry('925x500+300+200')
        spbw_root.configure(bg="#fff")
        spbw_root.resizable(False,False)

        self.top_levels = spbw_root

        frame = Frame(spbw_root,width=925, height=500 , bg="white")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        heading = Label(frame,text='show password by web', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5, rely=0.1, anchor='center')

        account_msg = Label(frame,text=f'user: {username}', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',15))
        account_msg.place(relx=0.1, rely=0.1, anchor='center')

        web_name_label = Label(frame, text='Which website would you like to see the password for?', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',13))
        web_name_label.place(relx=0.5, rely=0.3, anchor='center')

        web_name = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        web_name.place(relx=0.5, rely=0.4, anchor='center')

        #the line under web name
        web_name_underline = Frame(frame,width=200, height=2, bg='black')
        web_name_underline.place(relx=0.5, rely=0.43, anchor='center')

        show_password_button = Button(frame, width=14, pady=7, text='Show Password', bg='#57a1f8', fg='white', border=0,
                             command=lambda : self.show_password_by_web(username,web_name,spbw_root))
        show_password_button.place(relx=0.5, rely=0.5, anchor='center')

        log_out_button = Button(frame, width=14, pady=7, text='Log Out', bg='#57a1f8', fg='white', border=0, command=lambda : self.logout(spbw_root))
        log_out_button.place(relx=0.1, rely=0.2, anchor='center')

        exit_button = Button(frame, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(spbw_root.master))
        exit_button.place(relx=0.5, rely=0.85, anchor='center')
        pass
    
    def remove_web_and_password_screen(self, username): #rwp -> shortcut
        rwp_root=Toplevel()
        rwp_root.title('remove web and password')
        rwp_root.geometry('925x500+300+200')
        rwp_root.configure(bg="#fff")
        rwp_root.resizable(False,False)

        self.top_levels = rwp_root

        frame = Frame(rwp_root,width=925, height=500 , bg="white")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        heading = Label(frame,text='remove web and password', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(relx=0.5, rely=0.1, anchor='center')

        account_msg = Label(frame,text=f'user: {username}', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',15))
        account_msg.place(relx=0.1, rely=0.1, anchor='center')

        web_name_label = Label(frame, text='Which website would you like to remove?', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',13))
        web_name_label.place(relx=0.5, rely=0.3, anchor='center')

        web_name = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        web_name.place(relx=0.5, rely=0.4, anchor='center')

        #the line under web name
        web_name_underline = Frame(frame,width=200, height=2, bg='black')
        web_name_underline.place(relx=0.5, rely=0.43, anchor='center')

        remove_button = Button(frame, width=14, pady=7, text='remove web', bg='#57a1f8', fg='white', border=0,
                             command=lambda : self.remove_web_and_password(username,web_name,rwp_root))
        remove_button.place(relx=0.5, rely=0.5, anchor='center')

        log_out_button = Button(frame, width=14, pady=7, text='Log Out', bg='#57a1f8', fg='white', border=0, command=lambda : self.logout(rwp_root))
        log_out_button.place(relx=0.1, rely=0.2, anchor='center')

        exit_button = Button(frame, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(rwp_root.master))
        exit_button.place(relx=0.5, rely=0.85, anchor='center')
        pass

    #endregion

    #region functions
        
    def run(self):
        self.main_screen()

    def exiting(self,root_to_exit):
        root_to_exit.destroy()
        self.message = ['exit','','','','','']
        self.client.send_message(self.message)

    def signup(self, user, pword, root):
        entered_username = user.get()
        entered_password = pword.get()

        #בדיקה של משתמש
        if entered_username == 'Username' or entered_password == 'Password' or entered_username == '' or entered_password == '' : #קיים בטבלה- ממשיך הלאה
            messagebox.showerror('signup' , 'your username or password can not be the default username or password')
            root.deiconify()
        elif "|||" in entered_username :
            messagebox.showerror('signup' , f'your username can not contain "|||"')
            root.deiconify()


        else: #לא קיים בטבלה- מכניס לטבלה וממשיך הלאה
            password = bytes(entered_password, 'utf-8')
            hash_password = hashlib.sha256(password).hexdigest()
            username_password = f'{entered_username}|||{hash_password}'
            self.message = ['signup' , username_password , '', '', '']
            self.client.messages = ""
            self.client.send_message(self.message)
            while self.client.messages == "":
                pass
            server_message = self.client.messages  # 'ok' or 'problem'
            # self.client.messages = ""

            if server_message.startswith('ok'):
                messagebox.showinfo("signup", 'you are now in the system')
                root.destroy()


            if server_message.startswith('problem'):
                messagebox.showinfo("signup", 'user name already exists')
                root.deiconify()

    def login(self, user, pword, root):
        entered_username = user.get()
        entered_password = pword.get()
        
        #בדיקה של משתמש
        if entered_username == 'Username' or entered_password == 'Password' or entered_username == '' or entered_password == '' : #קיים בטבלה- ממשיך הלאה
            messagebox.showerror('login' , 'your username or password can not be Username or Password or null')
            root.deiconify()
        elif "|||" in entered_username :
            messagebox.showerror('login' , f'your username can not contain "|||"')
            root.deiconify()


        else: #לבדוק האם זה נמצא בטבלת משתמשים, אם כן -> להכניס. אחרת -> לכתוב שהוא לא רשום
            password = bytes(entered_password, 'utf-8')
            hash_password = hashlib.sha256(password).hexdigest()
            username_password = f'{entered_username}|||{hash_password}'
            self.message = ['login' , username_password, '', '', '']
            self.client.messages = ""
            self.client.send_message(self.message)
            while self.client.messages == "":
                pass
            server_message = self.client.messages
            if server_message.startswith('ok'):
                messagebox.showinfo("login", 'you are now logged in')
                root.destroy()
                self.menu_screen(entered_username)

            if server_message.startswith('problem'):
                messagebox.showinfo("login", 'your username or password was incorrect')
                root.deiconify()

            if server_message.startswith('not signed up'):
                messagebox.showinfo("login", 'your are not in the system, please sign up')
                root.destroy()

    def logout(self, root):
        answer = messagebox.askquestion('Log Out', 'Are you sure you want to log out?')
        if answer == 'yes':
            root.destroy()
        else:
            messagebox.showinfo('Return', 'Returning to the menu')
            root.deiconify()
        
    def insert_web_name_and_password_func (self, username, web_name, password, root):
        entered_web = web_name.get()
        entered_password = password.get()

        if entered_web == '' or entered_password == '':
            messagebox.showerror('Add web and password' , 'your web name or password can not be null')
            root.deiconify()
        elif "|||" in entered_web :
            messagebox.showerror('Add web and password' , f'your web name can not contain "|||"')
            root.deiconify()
        else:
            password_to_encrypt = entered_password
            encrypted_password = self.client.client_encryption.encrypt_msg(password_to_encrypt.encode(), self.client.server_public_key) #.decode()
            # print('encrypted_password',encrypted_password)
            self.message = ['insert web and password' , username, '', entered_web, str(encrypted_password),'']
            self.client.messages = ""
            self.client.send_message(self.message)
            while self.client.messages == "":
                pass
            server_message = self.client.messages
            if server_message.startswith('ok'):
                messagebox.showinfo("insert new web name and password", f'{entered_web} and password have been successfully added')
                root.destroy()
                self.menu_screen(username)

            if server_message.startswith('problem'):
                messagebox.showinfo("insert new web name and password", f'{entered_web} already exists under your username')
                root.deiconify()

    def update_password_for_web(self, username, web_name, password, new_password, root):
        entered_web = web_name.get()
        entered_password = password.get()
        entered_new_password = new_password.get()

        if entered_web == '' or entered_password == '' or entered_new_password == '':
            messagebox.showerror('Add web and password' , 'your web name or password can not be null')
            root.deiconify()
        elif "|||" in entered_web :
            messagebox.showerror('Add web and password' , f'your web name can not contain "|||"')
            root.deiconify()
        else:
            password_to_encrypt = entered_password
            encrypted_password = self.client.client_encryption.encrypt_msg(password_to_encrypt.encode(), self.client.server_public_key) #.decode()
            new_password_to_encrypt = entered_new_password
            encrypted_new_password = self.client.client_encryption.encrypt_msg(new_password_to_encrypt.encode(), self.client.server_public_key) #.decode()
            self.message = ['update password for web' , username, '', entered_web, str(encrypted_password),str(encrypted_new_password)]
            self.client.messages = ""
            self.client.send_message(self.message)
            while self.client.messages == "":
                pass
            server_message = self.client.messages
            if server_message.startswith('ok'):
                messagebox.showinfo("update password for web", f'Your password for {entered_web} has been updated')
                root.destroy()
                self.menu_screen(username)

            if server_message.startswith('current password is wrong'):
                messagebox.showinfo("update password for web", 'Your current password was wrong')
                root.deiconify()
            
            if server_message.startswith('new password is the same as the current password'):
                messagebox.showinfo("update password for web", 'Your new password is the same as the current password')
                root.deiconify()

            if server_message.startswith('web not exists'):
                messagebox.showinfo("update password for web", f'{entered_web} not exists under your username')
                root.deiconify()
        pass

    def show_password_by_web (self, username, web_name, root):
        entered_web = web_name.get()
        if entered_web == '':
            messagebox.showerror('Show password' , 'your web name can not be null')
            root.deiconify()
        elif "|||" in entered_web :
            messagebox.showerror('Show password' , f'your web name can not contain "|||"')
            root.deiconify()
        else:
            self.message = ['show password by web' , username, '', entered_web, '','']
            self.client.messages = ""
            self.client.send_message(self.message)
            while self.client.messages == "":
                pass
            server_message = self.client.messages
            if server_message.startswith('ok'):
                encrypted_password = server_message[3:]
                decrypted_password = self.client.client_encryption.decrypt_msg(eval(encrypted_password))
                messagebox.showinfo("show password", f'Your password for {entered_web} is {decrypted_password}')
                answer = messagebox.askquestion('show password', 'do you want to continue searching for another password for webs?')
                if answer == 'yes':
                    root.deiconify()
                else:
                    messagebox.showinfo('Return', 'Returning to the menu')
                    root.destroy()
                    self.menu_screen(username)

            if server_message.startswith('web not exists'):
                messagebox.showinfo("show password", f'{entered_web} not exists under your username')
                root.deiconify()
        pass

    def remove_web_and_password(self, username, web_name, root):
        entered_web = web_name.get()
        if entered_web == '':
            messagebox.showerror('remove web and password' , 'your web name can not be null')
            root.deiconify()
        elif "|||" in entered_web :
            messagebox.showerror('remove web and password' , f'your web name can not contain "|||"')
            root.deiconify()
        else:
            answer = messagebox.askquestion('remove web and password', f'do you want to remove {entered_web} ?')
            if answer == 'yes':
                self.message = ['remove web and password' , username, '', entered_web, '','']
                self.client.messages = ""
                self.client.send_message(self.message)
                while self.client.messages == "":
                    pass
                server_message = self.client.messages
                if server_message.startswith('ok'):
                    messagebox.showinfo("remove web and password", f'{entered_web} has been removed')
                    root.destroy()
                    self.menu_screen(username)

                if server_message.startswith('web not exists'):
                    messagebox.showinfo("remove web and password", f'{entered_web} not exists under your username')
                    root.deiconify()
            else:
                messagebox.showinfo('reject', f'not removing {entered_web}')
                root.deiconify()
            


    #endregion
    
        

if __name__ == '__main__':
    client = MultiThreadedClient('127.0.0.1', SERVER_PORT)
    client.run()
    app = GUI(client)
    app.run()