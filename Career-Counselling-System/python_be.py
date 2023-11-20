import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

screen_width = pathway.winfo_screenwidth()
screen_height = pathway.winfo_screenheight()
pathway.geometry('1800x800+0+0')
pathway.geometry(f"{screen_width}x{screen_height}+0+0")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)


logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)



Label = tk.Label(pathway, text="Career options after B.E.", font=('Arial', 25))
Label.pack(padx=20, pady=100)

frame0 = Frame(pathway, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

def IES():
    pathway.destroy()
    import ies

def MERNAV():
    pathway.destroy()
    import mernav

def ME():
    pathway.destroy()
    import me

def SCEX():
    pathway.destroy()
    import scex

def DDE():
    pathway.destroy()
    import dfde

def MBA():
    pathway.destroy()
    import mba

def MS():
    pathway.destroy()
    import ms
    
def MTECH():
    pathway.destroy()
    import mtech

def GOVCON():
    pathway.destroy()
    import govcon


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



buttonframe = tk.Frame(pathway)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


btn1 = tk.Button(buttonframe, text="I.E.S Exam", font=('Arial', 18), command=IES)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Mercant Navy", font=('Arial', 18), command=MERNAV)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.E.", font=('Arial', 18), command=ME)
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="MPSC/UPSC Exam", font=('Arial', 18), command=SCEX)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Defence Direct Entry", font=('Arial', 18), command=DDE)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.S.", font=('Arial', 18), command=MS)
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.B.A.", font=('Arial', 18), command=MBA)
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.Tech", font=('Arial', 18), command=MTECH)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Gov. Contractor", font=('Arial', 18), command=GOVCON)
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x', pady=50)
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)


pathway.mainloop()