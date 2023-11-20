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



Label = tk.Label(pathway, text="Great !! you have so many options to pursue your dream career", font=('Times New Roman', 25))
Label.pack(pady=(100,0) ) 

def bcom():
    pathway.destroy()
    import bcom

def CAFOUNDATION():
    pathway.destroy()
    import CAFOUNDATION

def BBA():
    pathway.destroy()
    import BBA

def CSFOUNDATION():
    pathway.destroy()
    import CSFOUNDATION


def BCA():
    pathway.destroy()
    import BCA

def BARCH():
    pathway.destroy()
    import BARCH
    

def DEd():
    pathway.destroy()
    import DEd
    
def CALLCENTRE():
    pathway.destroy()
    import CALLCENTRE
    
def MPSC():
    pathway.destroy()
    import MPSC


Label = tk.Label(pathway, text="Commerce", font=('Times New Roman', 25))
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


btn1 = tk.Button(buttonframe, text="C.A. Foundation", font=('Times New Roman', 18), command=CAFOUNDATION)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="B.COM", font=('Times New Roman', 18), command=bcom)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.B.A", font=('Times New Roman', 18), command=BBA)
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="C.S. FOUNDATION", font=('Times New Roman', 18),command=CSFOUNDATION)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.C.A", font=('Times New Roman', 18),command=BCA)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.ARCH", font=('Times New Roman', 18),command=BARCH)
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="D.Ed", font=('Times New Roman', 18), command=DEd)
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="CALL CENTRE", font=('Times New Roman', 18),command=CALLCENTRE)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="MPSC/UPSC", font=('Times New Roman', 18),command=MPSC)
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)
buttonframe.pack(fill='x', pady=50)

logo = ImageTk.PhotoImage(file='logo.png')
logolabel = tk.Label(pathway,image=logo,)
logolabel.place(x=1,y=5)

pathway.mainloop()

