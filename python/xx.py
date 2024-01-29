from tkinter import *
from tkinter import messagebox
# class Client_gui():
#     def __init__(self) -> None:
def first():      
    root=Tk()
    root.title('Log in')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    def signin():
        username = user.get()
        password = pword.get()
        if username == 'amit' and password =='hi':
            messagebox.showinfo("login", 'you are now signed in')
            root.destroy()
            second()
        else:
            messagebox.showerror('login' , 'your username or password was incorect')


    img_src = r"C:\Users\amitk\OneDrive\Desktop\all\python\password_manager_project\images\login.png"
    img = PhotoImage(file= img_src)
    Label(root, image=img, bg='white').place(x=50,y=50)

    frame = Frame(root,width=350, height=350 , bg="white")
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

    Button(frame,width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35,y=204)




    root.mainloop()

def second():
    root=Tk()
    root.title('Log in')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    root.mainloop()

first()