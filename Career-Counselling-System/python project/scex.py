import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)



Label = tk.Label(pathway, text="MPSC/UPSC EXAM", font=('Arial', 25))
Label.pack(padx=20, pady=100)



T = Text(pathway, height = 15, width = 80, font=10)


Fact = """The Maharashtra Public Service Commission (MPSC) is a body created by the Constitution of India under article 315 to select officers for civil service jobs in the Indian state of Maharashtra according to the merits of the applicants and the rules of reservation.

Maharashtra Public Service Commission (MPSC) is a Constitutional Body established Under Article 315 of Constitution of India which provides a smooth and efficient functioning of the Government of Maharashtra by providing suitable candidates for various Government posts and advise them on various service matters like formulation of Recruitment Rules, advise on promotions, transfers and disciplinary actions.

UPSC is a Constitutional Body under Article 315-323 Part XIV Chapter II of the Constitution of India to discharge their duties, functions and obligations assigned under Article 320. The UPSC  conducts various examinations  in accordance with the Rules of examination as notified by the Government of India in a just, fair and impartial manner  for making a merit based selection and recommendation of candidates for various Group A and Group B Services  of the Govt. of India."""


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
