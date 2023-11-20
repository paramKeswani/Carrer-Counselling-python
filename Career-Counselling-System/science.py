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



def PCB():
    pathway.destroy()
    import PCB

def PCMB():
    pathway.destroy()
    import python_PCMB

def PCM():
    pathway.destroy()
    import python_PCM        
    





Label = tk.Label(pathway, text="Science Fields", font=('Arial', 25))
Label.pack(padx=20, pady=100)

Label = tk.Label(pathway, text="Please specify Subjects You have Chosen After 10th", font=('Arial', 25))
Label.pack(padx=20, )

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



buttonframe = tk.Frame(pathway)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


btn1 = tk.Button(buttonframe, text="Physics, Chemistry, Mathematics & Biology (PCMB)", font=('Arial', 18),width=40, bg='dark blue', fg='white' , command=PCMB)
btn1.grid(row=1, column=0,pady=30, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Physics, Chemistry, Mathematics (PCM)", font=('Arial', 18),width=40, bg='dark blue', fg='white' , command=PCM)
btn1.grid(row=2, column=0,pady=30, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Physics, Chemistry, Biology (PCB)", font=('Arial', 18), width=40, bg='dark blue', fg='white' , command=PCB )
btn1.grid(row=3, column=0,pady=30, sticky=tk.W+tk.E)

buttonframe.pack()
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = tk.Label(pathway,image=logo,)
logolabel.place(x=1,y=5)

pathway.mainloop()