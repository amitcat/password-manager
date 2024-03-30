from tkinter import *
from tkinter import messagebox
class Client_gui:
    def __init__(self) -> None:
        self.user = ''
        self.pword = ''
        self.command_to_exacute = {}
        self.uname_pass = ''
        self.sign_in_flag = False
    

    def run(self):
        self.log_in_screen()

    def main_page(self):
        root = Tk()
        root.title('Main page')
        root.geometry('925x500+300+200')
        root.configure(bg="#fff")
        root.resizable(False,False)
        exit_button = Button(root, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=root.destroy)
        exit_button.place(relx=0.45, rely=0.5)
        signIn = Button(root, text='SignIn', bg='#57a1f8', fg='white', border=0 , command=self.log_in_screen)
        signIn.place(relx=0.4, rely=0.5)
        root.mainloop()

        # width=39, pady=7,
        

    def log_in_screen(self):
        login_root=Toplevel()
        login_root.title('Log in')
        login_root.geometry('925x500+300+200')
        login_root.configure(bg="#fff")
        login_root.resizable(False,False)

        def signin():
            self.user = user.get()
            self.pword = pword.get()

            
            #בדיקה של משתמש
            if self.user == 'Username' or self.pword == 'Password' or self.user == '' or self.pword == '' : #קיים בטבלה- ממשיך הלאה
                messagebox.showerror('login' , 'your username or password was incorect')
            elif ":" in self.user :
                messagebox.showerror('login' , f'your username can not contain ":" ')


            else: #לא קיים בטבלה- מכניס לטבלה וממשיך הלאה
                messagebox.showinfo("login", 'you are now signed in')
                login_root.destroy()


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
        Button(frame,width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0 , command=signin).place(x=35,y=204)
        string_name = str(self.user)
        string_password = str(self.pword)
        exit_button = Button(login_root, width=39, pady=7, text='EXIT', bg='#57a1f8', fg='white', border=0 , command=login_root.master.destroy) # .master
        exit_button.place(relx=0.45, rely=0.5)
        self.sign_in_flag = True

        # login_root.mainloop()
        
        
    def get_uname_and_pass(self):
        self.uname_pass= f'{self.user}:{self.pword}'
        
        # close = root.protocol("WM_DELETE_WINDOW", confirm)
        
        # if close:
        #     root.destroy()
        #     return
        
    


    def menu_page(self):
        root=Toplevel()
        root.title('Menu')
        root.geometry('925x500+300+200')
        root.configure(bg="#fff")
        root.resizable(False,False)
        
        
        def get_action_to_exacute():
            return 
        return get_action_to_exacute()

