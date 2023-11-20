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

bglabel = tk.Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)




Label = tk.Label(pathway, text="Career options after PCMB", font=('Times New Roman', 25))
Label.pack(padx=20, pady=100)

Label = tk.Label(pathway, text="Great !! you have so many options to pursue your dream career", font=('Times New Roman', 25))
Label.pack(padx=20, )

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
    
newaccbutton = Button(frame0, text="Home", font=('Times New Roman', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command= home).place(x= 950, y=30 ) 


newaccbutton = Button(frame0, text="Services", font=('Times New Roman', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1050, y=30 )
 

newaccbutton = Button(frame0, text="About Us", font=('Times New Roman', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1150, y=30 )

newaccbutton = Button(frame0, text="LogOut", font=('Times New Roman', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1250, y=30 )

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


btn1 = tk.Button(buttonframe, text="B.Sc. in Dairy Technology", font=('Times New Roman', 18),width=40, bg='dark blue', fg='white' , command=BSCD)
btn1.grid(row=0, column=1, pady=10, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Bachelor in Pharmacy", font=('Times New Roman', 18), width=40, bg='dark blue', fg='white' , command=BPHA)
btn1.grid(row=1, column=1,pady=10, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Tech in Agriculture", font=('Times New Roman', 18), width=40, bg='dark blue', fg='white' , command=BAGRI)
btn1.grid(row=2, column=1,pady=10, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Sc. in Bio-Technology", font=('Times New Roman', 18), width=40, bg='dark blue', fg='white' , command=BSBT)
btn1.grid(row=3, column=1,pady=10, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Sc. in Agriculture", font=('Times New Roman', 18), width=40, bg='dark blue', fg='white' , command=BSCAGRI)
btn1.grid(row=4, column=1,pady=10, sticky=tk.W+tk.E)

buttonframe.pack(fill='x', pady=50)
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = tk.Label(pathway,image=logo,)
logolabel.place(x=1,y=5)

pathway.mainloop()