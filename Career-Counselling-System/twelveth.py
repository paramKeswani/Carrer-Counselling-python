from tkinter import *
from PIL import Image, ImageTk, ImageDraw

def loginpage():
    pathway.destroy()
    import signin

def chatbotpage():
    pathway.destroy()
    import chatbot2


pathway = Tk()
screen_width = pathway.winfo_screenwidth()
screen_height = pathway.winfo_screenheight()
pathway.geometry('1800x800+0+0')
pathway.geometry(f"{screen_width}x{screen_height}+0+0")
pathway.title('Pathway | Career Counselling System')

frame0 = Frame(pathway, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

def home():
    pathway.destroy()
    import mainmenu
newaccbutton = Button(frame0, text="Home", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command= home).place(x= 950, y=30 ) 


newaccbutton = Button(frame0, text="Services", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1050, y=30 )
 

newaccbutton = Button(frame0, text="About Us", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1150, y=30 )

newaccbutton = Button(frame0, text="LogOut", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1250, y=30 )

userimg = ImageTk.PhotoImage(file='user2.png')
userimg_pil = Image.open('user2.png')
userimg_small_pil = userimg_pil.resize((60, 60))  # Reduce image size to 100x100
userimg_small = ImageTk.PhotoImage(userimg_small_pil)
button = Button(frame0, image=userimg_small, bg='black')
button.place(x=1410, y=0)


logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1250,y=5)

heading = Label(pathway, text = 'Which Stream have you chosen in 10th ', font=('Microsoft Tahei UI Light', 25, 'bold'), bg='white' ,fg='firebrick1', )
heading.place(x=60,y=60)

newaccbutton = Button(pathway, text='Science', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=19,).place(x= 150, y=270 )
newaccbutton = Button(pathway, text='Arts', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=19,).place(x= 450, y=270 )
newaccbutton = Button(pathway, text='Commerce', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=19,).place(x= 150, y=570 )
newaccbutton = Button(pathway, text='Other Opportunities', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=19,).place(x= 450, y=570 )
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)

pathway.mainloop()
