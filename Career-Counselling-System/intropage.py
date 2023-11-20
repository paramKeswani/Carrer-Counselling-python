from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

def drive():
    introwindow.destroy()   
    import signup

def drivelogin():
    introwindow.destroy()
    import signin

def services():
    introwindow.destroy()
    import services

introwindow = Tk()
screen_width = introwindow.winfo_screenwidth()
screen_height = introwindow.winfo_screenheight()
introwindow.geometry('1800x800+0+0')
introwindow.geometry(f"{screen_width}x{screen_height}+0+0")
introwindow.title('Welcome | Career Counselling System')
bgimage = ImageTk.PhotoImage(file='intro.png')
bglabel = Label(introwindow, image=bgimage)
bglabel.place(x=0,y=0)

logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(introwindow,image=logo,)
logolabel.place(x=1,y=0)

orlabel = Label(introwindow, text="Confused about your Career ?", font= ('Times New Roman',50,'bold'), fg = 'firebrick1', bg = 'white').place(x= 450, y=140 )

orlabel = Label(introwindow, text="Discover Yourself !!", font= ('Times New Roman',23,'bold'), fg = 'blue', bg = 'white').place(x= 1070, y=240 )

orlabel = Label(introwindow, text="Take Test to find ", font= ('Times New Roman',23,'bold'), fg = 'black', bg = 'white').place(x= 1070, y=320 )
orlabel = Label(introwindow, text=" perfect career for you", font= ('Times New Roman',23,'bold'), fg = 'black', bg = 'white').place(x= 1070, y=360 )

newaccbutton = Button(introwindow, text="Get Started", font=('Times New Roman', 16,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command=drive , relief='groove',borderwidth=5).place(x= 1150, y=460 )


newaccbutton = Button(introwindow, text="Services", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command=services).place(x= 1050, y=50 )
 



newaccbutton = Button(introwindow, text="About Us", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command=drive).place(x= 1150, y=50 )

newaccbutton = Button(introwindow, text="LogIn", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command=drivelogin).place(x= 1250, y=50 )

newaccbutton = Button(introwindow, text="Register", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command=drive).place(x= 1350, y=50 )



introwindow.mainloop()