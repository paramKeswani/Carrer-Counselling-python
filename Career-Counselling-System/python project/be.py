import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)



Label = tk.Label(pathway, text="B.E.", font=('Arial', 25))
Label.pack(padx=20, pady=100)



T = Text(pathway, height = 15, width = 80, font=10)


Fact = """The Bachelor of Technology (commonly abbreviated as B.Tech. or B.Tech.(Hons)) is an undergraduate academic degree conferred after completion of a three or four year program of studies at an accredited university or accredited university-level institution In India, The Bachelor of Technology degree is awarded after completion of a 4 year program. The B.Tech. degree is conferred by government and private institutions in various fields like Electronics Engineering Mechanical Engineering Computer engineering, Electrical engineering, Civil engineering, Chemical engineering, Production Engineering and Textile Engineering, as well as a host of other prestigious institutes (both public and privately funded) for their professional engineering programs.

In India, The Bachelor of Technology (B. Tech) is the most preferred course study among the best students and they are looking forward to get admitted in this B. Tech professional degree course desperately to represent themselves on the international platform."""
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
