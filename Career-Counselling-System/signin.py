from tkinter import *
from PIL import ImageTk
import mysql.connector
from tkinter import messagebox


conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='counselling')

#FUnctionality
def signuppage():
    loginwindow.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passEntry.config(show='*')
    eyebutton.config(command=show)

def forgetpass():
    loginwindow.destroy()
    import resetpass

def show():
    openeye.config(file='openeye.png')
    passEntry.config(show='')
    eyebutton.config(command=hide)
    

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passEntry.get() == 'Password':
        passEntry.delete(0,END)


def login_user():
    if usernameEntry.get() == '' or passEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')  
    else:
        try:
            mycursor = conn.cursor()
            query='select * from userdata where username=%s and password=%s'
            mycursor.execute(query, (usernameEntry.get(), passEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid username or password')
            else:
                messagebox.showinfo('Success','Login is successful')
                username=usernameEntry.get()
                print(username)
                # dashboard(username)
                loginwindow.destroy()
                import mainmenu
        except:
            messagebox.showerror('Error','connection not established')
        finally:
            if mycursor:
                mycursor.close()


# def login_user():
#     if usernameEntry.get() == '' or passEntry.get() == '':
#        messagebox.showerror('Error', 'All fields are required')  

#     else:
#          try:
#             mycursor = conn.cursor()
#          except:
#               messagebox.showerror('Error','connecction not established')
#               return
#         #  query = 'use counselling'
#         #  conn.execute(query)
#          query='select * from userdata where username=%s and password=%s'
#          mycursor.execute(query,(usernameEntry.get(), passEntry.get()))
#          mycursor.fetchall()
#         #  if row == None:
#         #       messagebox.showerror('Error', 'Invalid username or password')
#         #  else:
#         #       messagebox.showerror('Success','Login is succesful')
#          conn.commit()
#          mycursor.close()

                 

#     query = 'use counselling'
#     conn.execute(query)
   
#     conn.execute(query,(usernameEntry.get(),passEntry.get()))
#     row=conn.fetchone()
#     if row==None:
#         messagebox.showerror('Error','Invalid username or password')

#     else:
#                 messagebox.showinfo('Success','Login is successful')
#                 username=usernameEntry.get()
#                 print(username)
#                 # dashboard(username)
#                 loginwindow.destroy()
#                 import mainmenu

#GUI
loginwindow = Tk()
screen_width = loginwindow.winfo_screenwidth()
screen_height = loginwindow.winfo_screenheight()
loginwindow.geometry('1800x800+0+0')
loginwindow.geometry(f"{screen_width}x{screen_height}+0+0")
loginwindow.title('Login | Career Counselling System')
bgimage = ImageTk.PhotoImage(file='login3.png')

bglabel = Label(loginwindow, image=bgimage)
bglabel.place(x=0,y=0)

logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(loginwindow,image=logo,)
logolabel.place(x=1250,y=5)

heading = Label(loginwindow, text = 'USER LOGIN', font=('Times New Roman', 30, 'bold'), bg='white' ,fg='firebrick1')
heading.place(x=1000, y=160)

usernameEntry = Entry(loginwindow, width=30, font=('Microsoft Tahei UI Light', 18, 'bold'), bd=0, fg = 'firebrick1')
usernameEntry
usernameEntry.place(x = 1000, y=260 )
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(loginwindow, width=250, height=2 ,bg = 'firebrick1').place(x=1000, y=290)



passEntry = Entry(loginwindow, width=30, font=('Microsoft Tahei UI Light', 18, 'bold'), bd=0, fg = 'firebrick1')
passEntry
passEntry.place(x = 1000, y=330 )
passEntry.insert(0, 'Password')

passEntry.bind('<FocusIn>',pass_enter)

frame2 = Frame(loginwindow, width=250, height=2 ,bg = 'firebrick1').place(x=1000, y=360)

openeye = PhotoImage(file='openeye.png')
eyebutton = Button(loginwindow, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyebutton.place(x= 1230, y=330 )

forgetbutton = Button(loginwindow, text = 'Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2', font=('Microsoft Tahei UI Light', 9, 'bold'), fg = 'firebrick1' , activeforeground='firebrick1', command=forgetpass)
forgetbutton.place(x= 1150, y=390 )


loginbutton = Button(loginwindow, text='LOGIN', font=('open sans', 16,'bold'), fg= 'white', bg='firebrick1', activeforeground='white' ,activebackground='firebrick1' ,cursor='hand2', bd=0,width=19, command=login_user).place(x= 1000, y=470 )

orlabel = Label(loginwindow, text='-------------- OR ---------------', font= ('Open Sans',16), fg = 'firebrick1', bg = 'white').place(x= 1000, y=530 )


fblogo = PhotoImage(file='facebook.png')
fblabel = Label(loginwindow, image=fblogo, bg= 'white')
fblabel.place(x=1120, y=570)

twlogo = PhotoImage(file='twitter.png')
twlabel = Label(loginwindow, image=twlogo, bg= 'white')
twlabel.place(x=1160, y=570)

glogo = PhotoImage(file='google.png')
glabel = Label(loginwindow, image=glogo, bg= 'white')
glabel.place(x=1200, y=570)

orlabel = Label(loginwindow, text="Don't have an Account ?", font= ('Open Sans',9,'bold'), fg = 'firebrick1', bg = 'white').place(x= 1040, y=610 )

newaccbutton = Button(loginwindow, text='Create New Account', font=('open sans', 16,'bold'), fg= 'white', bg='firebrick1', activeforeground='white' ,activebackground='firebrick1' ,cursor='hand2', bd=0,width=19, command=signuppage).place(x= 1000, y=640 )


loginwindow.mainloop()