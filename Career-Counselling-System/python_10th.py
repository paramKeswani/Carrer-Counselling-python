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



Label = tk.Label(pathway, text="Career options after 10th", font=('Arial', 25))
Label.pack(padx=20, pady=100)

frame0 = Frame(pathway, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

def INDFOR():
    pathway.destroy()
    import indian_force

def LIC():
    pathway.destroy()
    import lic_agent

def ITI():
    pathway.destroy()
    import iti   
    
def DIP():
    pathway.destroy()
    import dip

def ADIP():
    pathway.destroy()
    import adip

def TC():
    pathway.destroy()
    import tc    

def CEXAM():
    pathway.destroy()
    import cexam

def CLERK():
    pathway.destroy()
    import clerk

def DIPDM():
    pathway.destroy()
    import dipdm

def SUP():
    pathway.destroy()
    import lic_agent

def DIPF():
    pathway.destroy()
    import dipdm

def MED():
    pathway.destroy()
    import med

def COMD():
    pathway.destroy()
    import comd

def PRIP():
    pathway.destroy()
    import prip

def MSCIT():
    pathway.destroy()
    import mscit                


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


btn1 = tk.Button(buttonframe, text="ITI", font=('Arial', 18), command=ITI)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Indian Forces", font=('Arial', 18), command=INDFOR)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Diploma", font=('Arial', 18), command=DIP)
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="LIC agent", font=('Arial', 18), command=LIC)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Art Diploma", font=('Arial', 18),command=ADIP)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Railway T.C.", font=('Arial', 18), command=TC)
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Clerical Exam", font=('Arial', 18),command=CEXAM)
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Gov. Clerk", font=('Arial', 18), command=CLERK)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Diploma in Dance/music", font=('Arial', 18), command=DIPDM)
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Building Supervisor", font=('Arial', 18), command=SUP)
btn1.grid(row=3, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Diploma in Farm Management", font=('Arial', 18), command=DIPF)
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Medical Laboratary Technician", font=('Arial', 18), command=MED)
btn1.grid(row=3, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Commercial and Diploma", font=('Arial', 18), command=COMD)
btn1.grid(row=4, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Private Secretary Pratices", font=('Arial', 18), command=PRIP)
btn1.grid(row=4, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="MS-CIT Couses", font=('Arial', 18), command=MSCIT)
btn1.grid(row=4, column=2, sticky=tk.W+tk.E)


buttonframe.pack(fill='x', pady=50)
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)

pathway.mainloop()