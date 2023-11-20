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


def BAMS():
    pathway.destroy()
    import BAMS

def BHMS():
    pathway.destroy()
    import BHMS

def BVSc():
    pathway.destroy()
    import BVSc

def BDS():
    pathway.destroy()
    import BDS

def MBBS():
    pathway.destroy()
    import MBBS

def PARAMEDICALCOURSES():
    pathway.destroy()
    import PARAMEDICALCOURSES

def BScNURSING():
    pathway.destroy()
    import BScNURSING

def DIPLOMAINNURSING():
    pathway.destroy()
    import DIPLOMAINNURSING

def BMLT():
    pathway.destroy()
    import BMLT

def BScHOMESCIENCE():
    pathway.destroy()
    import BScHOMESCIENCE


def BScBOTANY():
    pathway.destroy()
    import BScBOTANY






Label = tk.Label(pathway, text="Career Options in PCB", font=('Times New Roman', 25))
Label.pack(padx=20, pady=(100,50))

frame0 = Frame(pathway, width=1500, height=70, bg="black",)
frame0.place(x=0,y=0)

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


btn1 = tk.Button(buttonframe, text="B.A.M.S", font=('Times New Roman', 18),command=BAMS)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="B.H.M.S", font=('Times New Roman', 18),command=BHMS)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.V.Sc", font=('Times New Roman', 18),command=BVSc)
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.D.S", font=('Times New Roman', 18),command=BDS)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.B.B.S", font=('Times New Roman', 18),command=MBBS)
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="PARAMEDICAL COURSES", font=('Times New Roman', 18),command=PARAMEDICALCOURSES)
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Sc.NURSING", font=('Times New Roman', 18),command=BScNURSING)
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="DIPLOMA IN NURSING", font=('Times New Roman', 18),command=DIPLOMAINNURSING)
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.M.L.T.", font=('Times New Roman', 18),command=BMLT)
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="B.Sc. HOME SCIENCE", font=('Times New Roman', 18),command=BScHOMESCIENCE)
btn1.grid(row=3, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="B.Sc.-Botany,Microbiology,Zoology", font=('Times New Roman', 18),command=BScBOTANY)
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)
buttonframe.pack(fill='x', pady=50)

logo = ImageTk.PhotoImage(file='logo.png')
logolabel = tk.Label(pathway,image=logo,)
logolabel.place(x=1,y=5)


pathway.mainloop()