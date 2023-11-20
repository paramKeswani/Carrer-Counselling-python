from tkinter import *
from PIL import ImageTk
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='counselling')

#FUnctionality
def signuppage():
    resetpasspage.destroy()
    import signin

def hide():
    openeye.config(file='closeye.png')
    passEntry.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passEntry.config(show='')
    eyebutton.config(command=hide)
    

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passEntry.get() == 'New Password':
        passEntry.delete(0,END)

def pass2_enter(event):
   if passEntry2.get() == 'Confirm Password':
        passEntry2.delete(0,END)


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
                resetpasspage.destroy()
                import mainmenu
        except:
            messagebox.showerror('Error','connection not established')
        finally:
            if mycursor:
                mycursor.close()


def change_pass():
    if usernameEntry.get() == '' or passEntry.get() == '' or passEntry2.get() == '':
        messagebox.showerror('Error','All fields are required')
    elif passEntry.get() !=  passEntry2.get() :
        messagebox.showerror('Error','PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH')

    else:
        mycursor = conn.cursor()
        query = ' SELECT * FROM userdata where username = %s'
        mycursor.execute(query, (usernameEntry.get(),))

        row = mycursor.fetchone()
        if row == None:
                    messagebox.showerror('Error','Incorrect Username')
        else:
             query = 'update userdata set password= %s where username = %s'
             mycursor.execute(query,(passEntry.get(), usernameEntry.get())) 
             conn.commit()
             conn.close() 
             messagebox.showinfo('Success','Password is reset, please login with new password')
             resetpasspage.destroy()
             import signin




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
#                 resetpasspage.destroy()
#                 import mainmenu

#GUI
resetpasspage = Tk()
screen_width = resetpasspage.winfo_screenwidth()
screen_height = resetpasspage.winfo_screenheight()
resetpasspage.geometry('1800x800+0+0')
resetpasspage.geometry(f"{screen_width}x{screen_height}+0+0")
resetpasspage.title('Reset  Password | Career Counselling System')
bgimage = ImageTk.PhotoImage(file='login3.png')

bglabel = Label(resetpasspage, image=bgimage)
bglabel.place(x=0,y=0)

logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(resetpasspage,image=logo,)
logolabel.place(x=1250,y=5)

heading = Label(resetpasspage, text = 'RESET PASSWORD', font=('Microsoft Tahei UI Light', 25, 'bold'), bg='white' ,fg='firebrick1')
heading.place(x=970, y=160)

usernameEntry = Entry(resetpasspage, width=30, font=('Microsoft Tahei UI Light', 18, 'bold'), bd=0, fg = 'firebrick1')
usernameEntry
usernameEntry.place(x = 1000, y=260 )
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>',user_enter)



frame1 = Frame(resetpasspage, width=250, height=2 ,bg = 'firebrick1').place(x=1000, y=290)



passEntry = Entry(resetpasspage, width=30, font=('Microsoft Tahei UI Light', 18, 'bold'), bd=0, fg = 'firebrick1')
passEntry
passEntry.place(x = 1000, y=330 )
passEntry.insert(0, 'New Password')
passEntry.bind('<FocusIn>',pass_enter)



passEntry2 = Entry(resetpasspage, width=30, font=('Microsoft Tahei UI Light', 18, 'bold'), bd=0, fg = 'firebrick1')
passEntry2
passEntry2.place(x = 1000, y=390 )
passEntry2.insert(0, 'Confirm Password')


passEntry2.bind('<FocusIn>',pass2_enter)

frame2 = Frame(resetpasspage, width=250, height=2 ,bg = 'firebrick1').place(x=1000, y=360)

frame3 = Frame(resetpasspage, width=250, height=2 ,bg = 'firebrick1').place(x=1000, y=420)

openeye = PhotoImage(file='openeye.png')
eyebutton = Button(resetpasspage, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyebutton.place(x= 1230, y=330 )



loginbutton = Button(resetpasspage, text='SUBMIT', font=('open sans', 16,'bold'), fg= 'white', bg='firebrick1', activeforeground='white' ,activebackground='firebrick1' ,cursor='hand2', bd=0,width=19, command=change_pass).place(x= 1000, y=470 )

orlabel = Label(resetpasspage, text='-------------- OR ---------------', font= ('Open Sans',16), fg = 'firebrick1', bg = 'white').place(x= 10000, y=530 )



orlabel = Label(resetpasspage, text="Have Account and Password ?", font= ('Open Sans',9,'bold'), fg = 'firebrick1', bg = 'white').place(x= 1000, y=610 )

newaccbutton = Button(resetpasspage, text='LOGIN', font=('open sans', 16,'bold'), fg= 'white', bg='firebrick1', activeforeground='white' ,activebackground='firebrick1' ,cursor='hand2', bd=0,width=19, command=signuppage).place(x= 1000, y=640 )


resetpasspage.mainloop()