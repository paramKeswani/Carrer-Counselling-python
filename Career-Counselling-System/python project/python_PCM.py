import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)





Label = tk.Label(pathway, text="Career options after PCM", font=('Arial', 25))
Label.pack(padx=20, pady=100)

frame0 = Frame(pathway, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

def BARCH():
    pathway.destroy()
    import barch

def NDA():
    pathway.destroy()
    import nda

def BDA():
    pathway.destroy()
    import bda

def INDARM():
    pathway.destroy()
    import indarm

def BE():
    pathway.destroy()
    import python_be

def BTECH():
    pathway.destroy()
    import btech

def ENGDIP():
    pathway.destroy()
    import engdip

def BSC():
    pathway.destroy()
    import bsc

def FTDIPLO():
    pathway.destroy()
    import ftdiplo

def HMD():
    pathway.destroy()
    import hmd


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



btn1 = tk.Button(buttonframe, text="B.Arch", font=('Arial', 18), command=BARCH)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="NDA", font=('Arial', 18), command=NDA)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Bachelor of planning and design", font=('Arial', 18), command=BDA)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Indian Army", font=('Arial', 18), command=INDARM)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.E.", font=('Arial', 18), command=BE)
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Tech", font=('Arial', 18), command=BTECH)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Engineering Diploma", font=('Arial', 18), command=ENGDIP)
btn1.grid(row=3, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Sc.", font=('Arial', 18), command=BSC)
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Film & Technology Diploma", font=('Arial', 18), command=FTDIPLO)
btn1.grid(row=4, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Hotel Management Degree", font=('Arial', 18), command=HMD)
btn1.grid(row=4, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill='x', pady=50)

pathway.mainloop()