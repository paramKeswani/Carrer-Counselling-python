from tkinter import *
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox

import mysql.connector

signupwindow = tk.Tk()
screen_width = signupwindow.winfo_screenwidth()
screen_height = signupwindow.winfo_screenheight()
signupwindow.geometry('1800x800+0+0')
signupwindow.geometry(f"{screen_width}x{screen_height}+0+0")
signupwindow.title('SignUp | Carrer Counselling System')

conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='counselling')
cursor = conn.cursor()

def loginpage():
    signupwindow.destroy()
    import signin

def clear():
     emailentry.delete(0,END)
     usernameentry.delete(0,END)
     passwordentry.delete(0,END)
     confpassentry.delete(0,END)



def connect_database():
    print("The connect_database function is being called")
    if emailentry.get() == '' or usernameentry.get() == '' or confpassentry.get() == '':
            messagebox.showerror('Error', 'All Fields are Required')

    elif passwordentry.get() != confpassentry.get():
         messagebox.showerror('Error', 'Password Mismathced')

    elif check.get() == 0:
         messagebox.showerror('Error', 'Please Accept Terms and Conditions')
    

    else:
        cursor.execute('use counselling')
     #    query = 'select * from userdata where username= %s'
     #    cursor.execute(query,(usernameentry.get()))
        cursor.execute("SELECT * FROM userdata WHERE username = %s", (usernameentry.get(),))
        row = cursor.fetchone()
        if row != None:
              messagebox.showerror('Error','Username already exist')
        else:
           try:
          #   print('hi')
            (lambda :add_data())
            # con = pymysql.connect(host='localhost:0', user='root', password='Om@123')
            # mycursor = con.cursor()
           except mysql.connector.Error as error:
                    print('connection failed : {}'.format(error))
        
        # email = tk.DoubleVar()
       
        
        
        # try:
        #     query = 'create database userdata'
        #     mycursor.execute(query)
        #     query= 'use userdata'
        #     mycursor.execute(query)
        #     query= "create table data (id int auto_increment primary key not null, email varchar(50) , username varchar(100), password varchar(20))"
        #     mycursor.execute(query)
        # except:
        #     mycursor.execute('use userdata')
        
        # query =  'insert into data(email,username,password) values(%s,%s,%s)'
        # mycursor.execute(query,(emailentry.get(),usernameentry.get(),passwordentry.get()))
        # con.commit()
        # con.close()
        # messagebox.showinfo('Success','Registration succesful')
        # clear()
        # signupwindow.destroy()
        # import signin

def add_data() :
            emailid = emailentry.get()
            username = usernameentry.get()
            password = passwordentry.get()
            data1 = (emailid , username, password)

            num = 1
            

            insert_stmt = "INSERT INTO userdata(email, username, password) VALUES (%s, %s,%s)"

            try:

                 cursor.execute(insert_stmt, data1)

                 conn.commit()
                 
                 messagebox.showinfo('Success','Registration succesful')
                 signupwindow.destroy()
                 import signin
            except mysql.connector.Error as error:
                    print('connection failed : {}'.format(error))
                    # conn.rollback()
            pass





bgimage = ImageTk.PhotoImage(file='login3.png')

bglabel = Label(signupwindow, image=bgimage)
bglabel.place(x=0,y=0)
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(signupwindow,image=logo,)
logolabel.place(x=1250,y=5)

frame = Frame(signupwindow)
frame.place(x=950, y=160 )

heading = Label(frame, text = 'CREATE AN ACCOUNT', font=('TImes New Roman', 25, 'bold'), fg='firebrick1')
heading.grid(row=3, column=0, padx=10 , pady=10)

emaillabel = Label(frame, text='Email', font=('times new roman', 14 , 'bold'),bg= 'white',fg='firebrick1')
emaillabel.grid(row=4, column=0,sticky='w',padx=25,pady=(10,0))

emailentry = Entry(frame,width=40, font=('times new roman', 10, 'bold'), )
emailentry.grid(row=5, column=0,sticky='w',padx=25)


usernamelabel = Label(frame, text='Username', font=('times new roman', 14 , 'bold'),bg= 'white',fg='firebrick1')
usernamelabel.grid(row=6, column=0,sticky='w',padx=25, pady=(10,0))

usernameentry = Entry(frame,width=40, font=('times new roman', 10, 'bold'))
usernameentry.grid(row=7, column=0,sticky='w',padx=25)

passwordlabel = Label(frame, text='Password', font=('times new roman', 14 , 'bold'),bg= 'white',fg='firebrick1')
passwordlabel.grid(row=8, column=0,sticky='w',padx=25, pady=(10,0))

passwordentry = Entry(frame,width=40, font=('times new roman', 10, 'bold'))
passwordentry.grid(row=9, column=0,sticky='w',padx=25)

confpasslabel = Label(frame, text='Confirm Password', font=('times new roman', 14 , 'bold'),bg= 'white',fg='firebrick1')
confpasslabel.grid(row=10, column=0,sticky='w',padx=25, pady=(10,0))

confpassentry = Entry(frame,width=40, font=('times new roman', 10, 'bold'))
confpassentry.grid(row=11, column=0,sticky='w',padx=25)

check = IntVar()
terms = Checkbutton(frame,text='I agree to the terms & conditions', font = ('times new roman' , 9, 'bold') ,fg='firebrick1',bg='white', activebackground='white', activeforeground='firebrick1', variable=check)
terms.grid(row=12, column=0, pady=10, )

signupbutton = Button(frame, text='SignUp', font=('Open sans', 16 , 'bold'), bd = 0, bg = 'firebrick1', activeforeground='white', width=22, command= lambda :add_data())
signupbutton.grid(row=13,column=0, pady=5, padx=(0,60))

alreadyacc = Label(frame, text='Already have an account?', font = ('open sans', '9', 'bold'), bg='white', fg='firebrick1')
alreadyacc.grid(row=14, column=0, sticky='w', pady=10, padx=25)

loginbutton = Button(frame, text='log in', font=('Open sans', 10, 'bold underline'), bg= 'firebrick1', fg = 'black', bd = 0, cursor = 'hand2',width=35,height=2, activebackground = 'white', activeforeground='black', command=loginpage )
loginbutton.grid(row=15, column=0,  pady=10, padx=(0,60))

signupwindow.mainloop()