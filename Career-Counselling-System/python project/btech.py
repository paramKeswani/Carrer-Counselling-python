import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)



Label = tk.Label(pathway, text="B.TECH", font=('Arial', 25))
Label.pack(padx=20, pady=100)



T = Text(pathway, height = 15, width = 80, font=10)


Fact = """Bachelor of Technology (BTech) is a professional undergraduate engineering degree programme awarded to candidates after they complete four years of study in the field. Engineering is one of the most popular courses in India and there are many institutes that offer the course to aspiring students. Lakhs of students enrol every year in this prestigious and most popular course, B.Tech is one of the most sought after courses in India. India produces more than 10 lakh engineering graduates every year and the engineering education in India comprises around 2500 engineering colleges and 1300 polytechnic colleges. 

For admissions, the most common BTech entrance examinations are JEE Main and JEE Advanced. Along with these national level entrance examinations, there are many state and private level entrance examinations that the students can attempt for admission to the course. The basic eligibility criteria for BTech is class 12 with Physics, Chemistry and Mathematics. However, there are additional criteria in every entrance exam and institute. Some of the institutes also conduct admission to their courses on merit basis i.e. based on marks scored by candidates in their class 12 board exams."""
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


pathway.mainloop()
