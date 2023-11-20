import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

def contact():
    servicespage.destroy()
    import contact

servicespage = tk.Tk()
screen_width = servicespage.winfo_screenwidth()
screen_height = servicespage.winfo_screenheight()
servicespage.geometry('1800x800+0+0')
servicespage.geometry(f"{screen_width}x{screen_height}+0+0")
servicespage.title('Services | Career Counselling System')

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(servicespage, image=bgimage)
bglabel.place(x=0,y=0)

frame0 = Frame(servicespage, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)





def home():
    servicespage.destroy()
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

label2 = tk.Label(servicespage, text="HOW IT WORKS" ,font=('Times New Roman', 25, 'bold') , fg='MAGENTA', )
label2.place(x=660,y=80)


logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(servicespage,image=logo,)
logolabel.place(x=1,y=5)


frame = tk.Frame(servicespage, width=200, height=200, bg="#B19CD9",)
frame.place(x=270, y=150)

# create a button
label2 = tk.Label(frame, text="Take the Career Assessment." ,font=('times new roman', 18, 'bold'),bg='#B19CD9' , fg='black', )
label2.pack()


label2 = tk.Label(frame, text="Created by experts, this set of questions will help you understand who you are (personality),\nwhat you like (interests) and what you are good at (abilities).", font=('times new roman', 16, ), bg='#B19CD9', fg='black', justify='center', wraplength=400)
label2.pack()

def testpage():
    servicespage.destroy()
    import justaddingpandas


button = tk.Button(frame, text='Choose Here', font=('open sans', 16,'bold'), fg= 'white', bg='dark blue', activeforeground='white' ,activebackground='#B19cd9' ,cursor='hand2', bd=0,width=19,command=testpage )
button.pack(pady=10)


frame2 = tk.Frame(servicespage, width=200, height=200, bg="#B19CD9",)
frame2.place(x=550, y=500)

# create a button
label2 = tk.Label(frame2, text="Unlock the Career Pathway." ,font=('times new roman', 18, 'bold'),bg='#B19CD9' , fg='black', )
label2.pack()



label2 = tk.Label(frame2, text="Get detailed information about your chosen careers - \n where will you work, what will you do, and lots more!", font=('times new roman', 16, ), bg='#B19CD9', fg='black', justify='center', wraplength=400)
label2.pack()


def pathway():
    servicespage.destroy()
    import trial

button = tk.Button(frame2, text='Choose Here', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='#B19CD9' ,cursor='hand2', bd=0,width=19, command=pathway)
button.pack(pady=10)

frame3 = tk.Frame(servicespage, width=200, height=200, bg="#B19CD9",)
frame3.place(x=810, y=150)

# create a button
label2 = tk.Label(frame3, text="Book the Career Counselling Session." ,font=('times new roman', 18, 'bold'),bg='#B19CD9' , fg='black', )
label2.pack()



label2 = tk.Label(frame3, text="Our Career Counsellors will explain your Career Report to you \n and your parents, and help you choose your top three careers.", font=('times new roman', 16, ), bg='#B19CD9', fg='black', justify='center', wraplength=400)
label2.pack()




button = tk.Button(frame3, text='Choose Here', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='#B19CD9' ,cursor='hand2', bd=0,width=19, command=contact )
button.pack(pady=10)


frame4 = tk.Frame(servicespage, width=200, height=200, bg="#B19CD9",)
frame4.place(x=1070, y=500)

# create a button
label2 = tk.Label(frame4, text="Meet the Experts." ,font=('times new roman', 18, 'bold'),bg='#B19CD9' , fg='black', )
label2.pack()


label2 = tk.Label(frame4, text="Watch webinars by industry experts from your field, \n who tell you what it’s really like to work in that field.", font=('times new roman', 16,), bg='#B19CD9', fg='black', justify='center', wraplength=400)
label2.pack()




button = tk.Button(frame4, text='Choose Here', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='#B19CD9' ,cursor='hand2', bd=0,width=19, command=contact )
button.pack(pady=10)

image = ImageTk.PhotoImage(file="points.png")
image_label = tk.Label(servicespage, image=image)
image_label.place(x=570, y=380)

servicespage.mainloop()
