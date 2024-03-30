from tkinter import *
from tkinter import messagebox
from client import MultiThreadedClient
from settings import *
import hashlib


class GUI():
    def __init__(self,client) -> None:
        # self.user = ''
        # self.pword = ''
        self.client = client
        self.top_levels = ""
        self.message = []
        self.exit = False

    def run(self):
        self.main_page()

    def exiting(self,root_to_exit):
        root_to_exit.destroy()
        self.message = ['exit',':']
        self.client.send_message(self.message)


    def main_page (self):
        root = Tk()
        root.title('Main page')
        root.geometry('925x500+300+200')
        root.configure(bg="#fff")
        root.resizable(False,False)
        exit_button = Button(root, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(root))
        exit_button.place(relx=0.45, rely=0.5)
        signIn = Button(root, text='SignIn', bg='#57a1f8', fg='white', border=0 , command=self.login_screen)
        signIn.place(relx=0.4, rely=0.5)
        signUp = Button(root, text='SignUp', bg='#57a1f8', fg='white', border=0 , command=self.signup_screen)
        signUp.place(relx=0.35, rely=0.5)
        root.mainloop()

    def login_screen(self):
        login_root=Toplevel()
        login_root.title('Log in')
        login_root.geometry('925x500+300+200')
        login_root.configure(bg="#fff")
        login_root.resizable(False,False)

        self.top_levels = login_root

        img_src = r"C:\Users\amitk\OneDrive\Desktop\all\python\password_manager_project\images\login.png"
        img = PhotoImage(file= img_src)
        Label(login_root, image=img, bg='white').place(x=50,y=50)

        frame = Frame(login_root,width=350, height=350 , bg="white")
        frame.place(x=480,y=70)

        heading = Label(frame,text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)
        
        # place for username
        def on_enter_uname(e):
            user.delete(0,'end')

        def on_leave_uname(e):
            uname = user.get()
            if uname =='':
                user.insert(0,'Username')

        user = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
        user.place(x=30,y=80)
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter_uname)
        user.bind('<FocusOut>', on_leave_uname)

        
        Frame(frame,width=295, height=2, bg='black').place(x=25,y=107)

        # place for password
        def on_enter_pass(e):
            pword.delete(0,'end')

        def on_leave_pass(e):
            password = pword.get()
            if password =='':
                pword.insert(0,'Password')

        pword = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
        pword.place(x=30,y=150)
        pword.insert(0,'Password')
        pword.bind('<FocusIn>', on_enter_pass)
        pword.bind('<FocusOut>', on_leave_pass)

       
        
        Frame(frame,width=295, height=2, bg='black').place(x=25,y=177)
        Button(frame,width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0 , command=lambda : self.login(user, pword, login_root)).place(x=35,y=204)
        exit_button = Button(login_root, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(login_root.master)) # .master
        exit_button.place(relx=0.45, rely=0.5)


    def signup_screen(self):
        SignUp_root=Toplevel()
        SignUp_root.title('Sign up')
        SignUp_root.geometry('925x500+300+200')
        SignUp_root.configure(bg="#fff")
        SignUp_root.resizable(False,False)

        self.top_levels = SignUp_root

        frame = Frame(SignUp_root,width=350, height=350 , bg="white")
        frame.place(x=480,y=70)

        heading = Label(frame,text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)
        
        # place for username
        def on_enter_uname(e):
            user.delete(0,'end')

        def on_leave_uname(e):
            uname = user.get()
            if uname =='':
                user.insert(0,'Username')

        user = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
        user.place(x=30,y=80)
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter_uname)
        user.bind('<FocusOut>', on_leave_uname)

        
        Frame(frame,width=295, height=2, bg='black').place(x=25,y=107)

        # place for password
        def on_enter_pass(e):
            pword.delete(0,'end')

        def on_leave_pass(e):
            password = pword.get()
            if password =='':
                pword.insert(0,'Password')

        pword = Entry(frame,width=25, fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
        pword.place(x=30,y=150)
        pword.insert(0,'Password')
        pword.bind('<FocusIn>', on_enter_pass)
        pword.bind('<FocusOut>', on_leave_pass)

       
        
        Frame(frame,width=295, height=2, bg='black').place(x=25,y=177)
        Button(frame,width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0 , command=lambda : self.signup(user, pword, SignUp_root)).place(x=35,y=204)
        exit_button = Button(SignUp_root, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=lambda : self.exiting(SignUp_root.master)) # .master
        exit_button.place(relx=0.45, rely=0.5)
        pass

    def signup(self, user, pword, root):
        entered_username = user.get()
        entered_password = pword.get()

        #בדיקה של משתמש
        if entered_username == 'Username' or entered_password == 'Password' or entered_username == '' or entered_password == '' : #קיים בטבלה- ממשיך הלאה
            messagebox.showerror('signup' , 'your username or password can not be the default username or password')
        elif ":" in entered_username :
            messagebox.showerror('signup' , f'your username can not contain ":"')


        else: #לא קיים בטבלה- מכניס לטבלה וממשיך הלאה
            password = bytes(entered_password, 'utf-8')
            hash_password = hashlib.sha256(password).hexdigest()
            username_password = f'{entered_username}:{hash_password}'
            self.message = ['signup' , username_password]
            self.client.send_message(self.message)
            messagebox.showinfo("signup", 'you are now in the system')
            root.destroy()

    def login(self, user, pword, root):
        entered_username = user.get()
        entered_password = pword.get()
        
        #בדיקה של משתמש
        if entered_username == 'Username' or entered_password == 'Password' or entered_username == '' or entered_password == '' : #קיים בטבלה- ממשיך הלאה
            messagebox.showerror('login' , 'your username or password can not be Username or Password or null')
        elif ":" in entered_username :
            messagebox.showerror('login' , f'your username can not contain ":"')


        else: #לבדוק האם זה נמצא בטבלת משתמשים, אם כן -> להכניס. אחרת -> לכתוב שהוא לא רשום
            password = bytes(entered_password, 'utf-8')
            hash_password = hashlib.sha256(password).hexdigest()
            username_password = f'{entered_username}:{hash_password}'
            self.message = ['login' , username_password]
            self.client.send_message(self.message)
            messagebox.showinfo("login", 'you are now signed in')
            root.destroy()            
    
        

if __name__ == '__main__':
    client = MultiThreadedClient('127.0.0.1', SERVER_PORT)
    client.run()
    app = GUI(client)
    app.run()