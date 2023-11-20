from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import mysql.connector

contactwindow = tk.Tk()
contactwindow.title('Contact | Carrer Counselling System')
screen_width = contactwindow.winfo_screenwidth()
screen_height = contactwindow.winfo_screenheight()
contactwindow.geometry('1800x800+0+0')
contactwindow.geometry(f"{screen_width}x{screen_height}+0+0")
# contactwindow.configure(bg='#00002a')
bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(contactwindow, image=bgimage)
bglabel.place(x=0,y=0)
conn = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='counselling')
cursor = conn.cursor()


def loginpage():
    contactwindow.destroy()
    import signin


def clear():
    emailentry.delete(0, END)
    usernameentry.delete(0, END)
    passwordentry.delete(0, END)
    confpassentry.delete(0, END)


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
        cursor.execute(
            "SELECT * FROM userdata WHERE username = %s", (usernameentry.get(),))
        row = cursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exist')
        else:
            try:
               #   print('hi')
                (lambda: add_data())
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
        # contactwindow.destroy()
        # import signin


def add_data():
    emailid = emailentry.get()
    username = usernameentry.get()
    password = passwordentry.get()
    message = confpassentry.get()
    data1 = (emailid, username, password, message)

    num = 1

    insert_stmt = "INSERT INTO contact(email, name, phoneno, message) VALUES (%s, %s,%s,%s)"

    try:

        cursor.execute(insert_stmt, data1)

        conn.commit()

        messagebox.showinfo('Success', 'Registration succesful')
        
    except mysql.connector.Error as error:
        print('connection failed : {}'.format(error))
        # conn.rollback()
    pass


frame0 = Frame(contactwindow, width=1800, height=70, bg="black",)
frame0.place(x=0, y=0)


def home():
    contactwindow.destroy()
    import mainmenu


newaccbutton = Button(frame0, text="Home", font=('open sans', 12, 'bold'), fg='white', bg='black',
                      activeforeground='white', activebackground='black', cursor='hand2', bd=0, width=12, command=home).place(x=950, y=30)


newaccbutton = Button(frame0, text="Services", font=('open sans', 12, 'bold'), fg='white', bg='black',
                      activeforeground='white', activebackground='black', cursor='hand2', bd=0, width=12,).place(x=1050, y=30)


newaccbutton = Button(frame0, text="About Us", font=('open sans', 12, 'bold'), fg='white', bg='black',
                      activeforeground='white', activebackground='black', cursor='hand2', bd=0, width=12,).place(x=1150, y=30)

newaccbutton = Button(frame0, text="LogOut", font=('open sans', 12, 'bold'), fg='white', bg='black',
                      activeforeground='white', activebackground='black', cursor='hand2', bd=0, width=12,).place(x=1250, y=30)

userimg = ImageTk.PhotoImage(file='user2.png')
userimg_pil = Image.open('user2.png')
userimg_small_pil = userimg_pil.resize(
    (60, 60))  # Reduce image size to 100x100
userimg_small = ImageTk.PhotoImage(userimg_small_pil)
button = Button(frame0, image=userimg_small, bg='black')
button.place(x=1410, y=0)


logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(contactwindow, image=logo,)
logolabel.place(x=1, y=5)

frame2 = tk.Frame(contactwindow, width=500, height=750)
frame2.place(x=350, y=130)
frame2.configure(bg='#00002a')

heading = Label(frame2, text='CONTACT US', font=(
    'times new roman', 25, 'bold'), bg='#00002a', fg='white', )
heading.grid(row=3, column=0, padx=90, pady=20)


heading = Label(frame2, text='careerify@gmail.com',
                font=('times new roman', 14, 'bold'), bg='#00002a', fg='white',)
heading.grid(row=4, column=0, padx=10, pady=10)


heading = Label(frame2, text='7588711657', font=(
    'times new roman', 14, 'bold'), bg='#00002a', fg='white',)
heading.grid(row=5, column=0, padx=10, pady=(0,445))




frame = tk.Frame(contactwindow, width=200, height=200, )
frame.place(x=750, y=130)
frame.configure(bg='light blue')


heading = Label(frame, text="Let's Talk", font=(
    'times new roman', 25, 'bold'), bg='light blue',)
heading.grid(row=3, column=0, padx=190, pady=20)

emaillabel = Label(frame, text='Email', font=(
    'times new roman', 14, 'bold'), bg='light blue', fg='firebrick1')
emaillabel.grid(row=4, column=0, sticky='w', padx=(120,0), pady=(10, 0))

emailentry = Entry(frame, width=40, font=(
    'times new roman', 10, 'bold'), fg='black', bg='light blue',)
emailentry.grid(row=5, column=0, sticky='w', padx=(120,0) ,pady=10)


usernamelabel = Label(frame, text='Name', font=(
    'times new roman', 14, 'bold'),bg='light blue',fg='firebrick1')
usernamelabel.grid(row=6, column=0, sticky='w', padx=(120,0), pady=(10, 0))

usernameentry = Entry(frame, width=40, font=(
    'times new roman', 10, 'bold'), fg='black', bg='light blue',)
usernameentry.grid(row=7, column=0, sticky='w', padx=(120,0) ,pady=10)

passwordlabel = Label(frame, text='Phone Number', font=(
    'times new roman', 14, 'bold'),bg='light blue', fg='firebrick1')
passwordlabel.grid(row=8, column=0, sticky='w', padx=(120,0), pady=(10, 0))

passwordentry = Entry(frame, width=40, font=(
    'times new roman', 10, 'bold'),fg='black', bg='light blue',)
passwordentry.grid(row=9, column=0, sticky='w', padx=(120,0) ,pady=10)

confpasslabel = Label(frame, text='city', font=(
    'times new roman', 14, 'bold'),bg='light blue', fg='firebrick1')
confpasslabel.grid(row=10, column=0, sticky='w', padx=(120,0), pady=(10, 0))

confpassentry = Entry(frame, width=40, font=(
    'times new roman', 10, 'bold'),fg='black', bg='light blue',)
confpassentry.grid(row=11, column=0, sticky='w', padx=(120,0) ,pady=10)

confpasslabel = Label(frame, text='Message', font=(
    'times new roman', 14, 'bold'), bg='light blue', fg='firebrick1')
confpasslabel.grid(row=12, column=0, sticky='w', padx=(120,0), pady=(10, 0))

confpassentry = Entry(frame, width=40,  font=(
    'times new roman', 10, 'bold'), fg='black', bg='light blue', )
confpassentry.grid(row=13, column=0, sticky='w', padx=(120,0) ,pady=10)



check = IntVar()
# terms = Checkbutton(frame, text='I agree to the terms & conditions', font=('Microsoft  Yahei UI Light', 9, 'bold'),
#                     fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1', variable=check)
# terms.grid(row=12, column=0, pady=10, )

signupbutton = Button(frame, text='SUBMIT', font=('Times New Roman', 16, 'bold'), bd=0,
                      bg='firebrick1', activeforeground='white', width=10, command=lambda: add_data())
signupbutton.grid(row=15, column=0, padx=(50,0), pady=(20,78))




contactwindow.mainloop()
