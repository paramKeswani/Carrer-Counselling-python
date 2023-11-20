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


Label = tk.Label(pathway, text="M.S", font=('Arial', 25))
Label.pack(padx=20, pady=100)



T = Text(pathway, height = 15, width = 80, font=10)


Fact = """An MS is a graduate degree that provides knowledge and training in specific areas of science, technology, mathematics, or in the behavioral sciences, medicine, nursing, social work, and a broad range of related multi-disciplinary subject areas. There are MS programs in biology, chemistry, and physics, and MS degrees in environmental science, data science, computer science, cybersecurity, and many other fields. MS programs may consist of classroom-based instruction, laboratory research, or a combination of the two. Some MS programs include a master’s thesis component and/or an applied research capstone project. These programs typically take one-to-two years of full-time enrollment to complete, depending on the discipline and the structure of the program. An MS degree may provide targeted professional training and/or serve as a pathway toward earning a doctoral degree."""
T.pack()

T.insert(tk.END, Fact)

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
logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)


pathway.mainloop()
