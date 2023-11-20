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


def BPEd():
    pathway.destroy()
    import BPEd


def MA():
    pathway.destroy()
    import MA


def MAINMASSCOMMUNICATION():
    pathway.destroy()
    import MAINMASSCOMMUNICATION


def BACHELORINJOURNALISM():
    pathway.destroy()
    import BACHELORINJOURNALISM


def LLB():
    pathway.destroy()
    import LLB


def BACHELORinLIB():
    pathway.destroy()
    import BACHELORinLIB

def MBA():
    pathway.destroy()
    import MBA

def MPSC():
    pathway.destroy()
    import MPSC

def DIPLOMAINDRAMATISATION():
    pathway.destroy()
    import DIPLOMAINDRAMATISATION

def MCA():
    pathway.destroy()
    import MCA

def MCM():
    pathway.destroy()
    import MCM


def BEd():
    pathway.destroy()
    import BEd

def ADVERTISINGDIPLOMA():
    pathway.destroy()
    import ADVERTISINGDIPLOMA

def EVENTMANAGEMENTDIPLOMA():
    pathway.destroy()
    import EVENTMANAGEMENTDIPLOMA

def BSF():
    pathway.destroy()
    import BSF



Label = tk.Label(pathway, text="B.A", font=('Arial', 25))
Label.pack(padx=20, pady=100)

frame0 = Frame(pathway, width=1500, height=70, bg="black",)
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



buttonframe = tk.Frame(pathway)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


btn1 = tk.Button(buttonframe, text="B.P.Ed", font=('Arial', 18),command=BPEd)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="M.A", font=('Arial', 18),command=MA)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.A. IN MASS COMMUNICATION", font=('Arial', 18),command=MAINMASSCOMMUNICATION)
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="BACHELOR IN JOURNALISM", font=('Arial', 18),command=BACHELORINJOURNALISM)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="L.L.B", font=('Arial', 18),command=LLB)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="BACHELAR OF LIBRARY SCIENCE", font=('Arial', 18),command=BACHELORinLIB)
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.B.A.", font=('Arial', 18),command=MBA)
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.P.S.C/U.P.S.C.", font=('Arial', 18),command=MPSC)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="DIPLOMA IN DRAMATISATION", font=('Arial', 18),command=DIPLOMAINDRAMATISATION)
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="M.C.A.", font=('Arial', 18),command=MCA)
btn1.grid(row=3, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="M.C.M", font=('Arial', 18),command=MCM)
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Ed", font=('Arial', 18),command=BEd)
btn1.grid(row=3, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="ADVERTISING DIPLOMA", font=('Arial', 18),command=ADVERTISINGDIPLOMA)
btn1.grid(row=4, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="EVENT MANAGEMENT DIPLOMA", font=('Arial', 18),command=EVENTMANAGEMENTDIPLOMA)
btn1.grid(row=4, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="BSF/CRPF/CISF", font=('Arial', 18),command=BSF)
btn1.grid(row=4, column=2, sticky=tk.W+tk.E)
buttonframe.pack(fill='x', pady=50)
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)


pathway.mainloop()