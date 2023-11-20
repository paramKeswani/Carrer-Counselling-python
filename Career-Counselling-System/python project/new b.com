import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)





Label = tk.Label(pathway, text="PCB", font=('Arial', 25))
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


btn1 = tk.Button(buttonframe, text="B.A.M.S", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="B.M.M.S", font=('Arial', 18))
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.V.Sc", font=('Arial', 18))
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.D.S", font=('Arial', 18))
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="M.B.B.S", font=('Arial', 18))
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="PARAMEDICAL COURSES", font=('Arial', 18))
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.Sc.NURSING", font=('Arial', 18))
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="DIPLOMA IN NURSING", font=('Arial', 18))
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="B.M.L.T.", font=('Arial', 18))
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="B.Sc. HOME SCIENCE", font=('Arial', 18))
btn1.grid(row=3, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="B.Sc.-Botany,Microbiology,Zoology", font=('Arial', 18))
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)
buttonframe.pack(fill='x', pady=50)

pathway.mainloop()