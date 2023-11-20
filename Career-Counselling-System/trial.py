import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image


pathway = tk.Tk()
pathway.geometry("1500x800")
pathway.title('Pathway | Career Counselling System')

logo = ImageTk.PhotoImage(file='logo.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1,y=5)

def tenth():
    pathway.destroy()
    import tenth

    
def twelve():
    pathway.destroy()
    import twelve

bgimage = ImageTk.PhotoImage(file='pathbg.png')

# Get the width and height of the window
win_width = pathway.winfo_screenwidth()
win_height = pathway.winfo_screenheight()

# Open the image using PIL and resize it to the window size
bgimage_pil = Image.open('pathbg.png')
bgimage_pil = bgimage_pil.resize((win_width, win_height), Image.ANTIALIAS)

# Convert the PIL image to a PhotoImage object
bgimage = ImageTk.PhotoImage(bgimage_pil)

# Create a Label widget with the image and set its size to the window size
bglabel = Label(pathway, image=bgimage, width=win_width, height=win_height)

# Place the label at (0,0)
bglabel.place(x=0, y=0)
logo = ImageTk.PhotoImage(file='logo2.png')
logolabel = Label(pathway,image=logo,)
logolabel.place(x=1250,y=75)


label = tk.Label(pathway, text="Discover Yourself And Your Ideal Career" ,font=('Microsoft Tahei UI Light', 25, 'bold'), bg='white' ,fg='firebrick1', )
label.place(x=50,y=90)
label = tk.Label(pathway, text="Get expert career guidance and counselling from " ,font=('Microsoft Tahei UI Light', 25, 'bold'), bg='white' ,fg='firebrick1', )
label.place(x=50,y=140)
label = tk.Label(pathway, text="Mentoria’s experts to discover which field you will enjoy and excel in." ,font=('Microsoft Tahei UI Light', 25, 'bold'), bg='white' ,fg='firebrick1', )
label.place(x=50,y=190)


#header frame
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



# create a frame
frame = tk.Frame(pathway, width=200, height=200, bg="black",)
frame.place(x=500, y=300)

# create a button

image = tk.PhotoImage(file="tenthimage.png")
image_label = tk.Label(frame, image=image)
image_label.pack(pady=10)

label = tk.Label(frame, text="10th" ,font=('Microsoft Tahei UI Light', 25, 'bold'), bg='black', fg='firebrick1', )
label.pack(pady=10)

label2 = tk.Label(frame, text="Choose ideal stream and subjects" ,font=('Microsoft Tahei UI Light', 16, 'bold'),bg='black' , fg='firebrick1', )
label2.pack(pady=10)

button = tk.Button(frame, text='Choose Here', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=19, command=tenth)
button.pack(pady=10)

# create a fram2
frame2 = tk.Frame(pathway, width=200, height=200, bg="black")
frame2.place(x=1000, y=300)

# create a button

image3 = tk.PhotoImage(file="twelimage.png")
image_label3 = tk.Label(frame2, image=image3)
image_label3.pack(pady=10)

label3 = tk.Label(frame2, text="12th" ,font=('Microsoft Tahei UI Light', 25, 'bold'), bg='black',fg='firebrick1', )
label3.pack(pady=10)

label4 = tk.Label(frame2, text="Select your ideal course and career" ,font=('Microsoft Tahei UI Light', 16, 'bold'), bg='black',fg='firebrick1', )
label4.pack(pady=10)

button2 = tk.Button(frame2, text='Decide Here', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=19,command= twelve)
button2.pack(pady=10)


# create an image


# move the frame around


pathway.mainloop()