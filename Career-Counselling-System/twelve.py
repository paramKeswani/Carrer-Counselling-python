import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image




pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')





bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)

def science():
    pathway.destroy()
    import science


def Commerce():
    pathway.destroy()
    import Commerce

def ARTS():
    pathway.destroy()
    import ARTS
    
Label1 = tk.Label(pathway, text="STREAM YOU CHOOSE AFTER 10TH", font=('Times New Roman', 18))
Label1.pack(padx=40, pady=(80,120))


buttonframe = tk.Frame(pathway)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="Science", font=('Times New Roman', 22),width=40, bg='dark blue', fg='white' ,command=science)
btn1.grid(row=1, column=0, pady=30, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Commerce", font=('Times New Roman', 22),width=40,bg='dark blue',fg='white', command= Commerce)
btn1.grid(row=2, column=0, pady=30, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Arts", font=('Times New Roman', 22),width=40,bg='dark blue',fg='white', command= ARTS)
btn1.grid(row=3, column=0, pady=30, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Humanities", font=('Times New Roman', 22),width=40,bg='dark blue',fg='white', command= ARTS)
btn1.grid(row=4, column=0, pady=30, sticky=tk.W+tk.E)



buttonframe.pack()


frame0 = Frame(pathway, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

def home():
    pathway.destroy()
    import mainmenu
newaccbutton = Button(frame0, text="Home", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command= home).place(x= 950, y=30 ) 


newaccbutton = Button(frame0, text="Services", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1050, y=30 )
 

newaccbutton = Button(frame0, text="About Us", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1150, y=30 )

newaccbutton = Button(frame0, text="LogOut", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1250, y=30 )


logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)
pathway.mainloop()
