import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)


def MBA():
    pathway.destroy()
    import MBA

def BANK():
    pathway.destroy()
    import BANK

def LLB():
    pathway.destroy()
    import LLB
    
def CA():
    pathway.destroy()
    import CA
        
def MEd():
    pathway.destroy()
    import MEd    

def ICWA():
    pathway.destroy()
    import ICWA

def BACHELORinLIB():
    pathway.destroy()
    import BACHELORinLIB

def CS():
    pathway.destroy()
    import CS

def IMPEXP():
    pathway.destroy()
    import IMPEXP 

def MCA():
    pathway.destroy()
    import MCA

def COMPCOURSES():
    pathway.destroy()
    import COMPCOURSES

def MPSC():
    pathway.destroy()
    import MPSC

def INDMILITARYACA():
    pathway.destroy()
    import INDMILITARYACA



Label = tk.Label(pathway, text="B.COM", font=('Arial', 25))
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


btn1 = tk.Button(buttonframe, text="M.B.A.", font=('Arial', 18), command=MBA)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="BANK", font=('Arial', 18), command=BANK)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="L.L.B.", font=('Arial', 18), command=LLB)
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="C.A.", font=('Arial', 18), command=CA)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.Ed", font=('Arial', 18), command=MEd)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="I.C.W.A", font=('Arial', 18), command=ICWA)
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="BACHELOR IN LIBRARY SCIENCE", font=('Arial', 18), command=BACHELORinLIB)
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="C.S.", font=('Arial', 18), command=CS)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="IMPORT EXPORT DIPLOMA", font=('Arial', 18), command=IMPEXP)
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="M.C.A.", font=('Arial', 18), command=MCA)
btn1.grid(row=3, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="COMPUTER COURSES", font=('Arial', 18), command=COMPCOURSES)
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.P.S.C./U.P.S.C.", font=('Arial', 18), command=MPSC)
btn1.grid(row=3, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="INDIAN MILITARY ACADEMY", font=('Arial', 18), command=INDMILITARYACA)
btn1.grid(row=4, column=0, sticky=tk.W+tk.E)

buttonframe.pack(fill='x', pady=50)

pathway.mainloop()