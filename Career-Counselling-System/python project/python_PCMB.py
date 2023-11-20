import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)





Label = tk.Label(pathway, text="Career options after PCMB", font=('Arial', 25))
Label.pack(padx=20, pady=100)

frame0 = Frame(pathway, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

def BSCD():
    pathway.destroy()
    import bscdairy

def BPHA():
    pathway.destroy()
    import bpha

def BSBT():
    pathway.destroy()
    import bscdairy

def BAGRI():
    pathway.destroy()
    import bagri

def BSCAGRI():
    pathway.destroy()
    import bscagri                

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


btn1 = tk.Button(buttonframe, text="B.Sc. in Dairy Technology", font=('Arial', 18), command=BSCD)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Bachelor in Pharmacy", font=('Arial', 18), command=BPHA)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Tech in Agriculture", font=('Arial', 18), command=BAGRI)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Sc. in Bio-Technology", font=('Arial', 18), command=BSBT)
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Sc. in Agriculture", font=('Arial', 18), command=BSCAGRI)
btn1.grid(row=4, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill='x', pady=50)

pathway.mainloop()