from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from chatbot3 import Chatbot


def loginpage():
    mainmenuwindow.destroy()
    import signin
    
def pathpage():
    mainmenuwindow.destroy()
    import trial


def test():
    mainmenuwindow.destroy()
    import justaddingpandas

def chatbotpage():
    newwindow = Toplevel(mainmenuwindow)
    app = Chatbot(newwindow)

def contact():
    
    mainmenuwindow.destroy()
    import contact

def service():
    mainmenuwindow.destroy()
    import services


mainmenuwindow = Tk()
screen_width = mainmenuwindow.winfo_screenwidth()
screen_height = mainmenuwindow.winfo_screenheight()
mainmenuwindow.geometry('1800x800+0+0')
mainmenuwindow.geometry(f"{screen_width}x{screen_height}+0+0")
mainmenuwindow.title('Main Menu | Career Counselling System')
bgimage = ImageTk.PhotoImage(file='m4.png')

bglabel = Label(mainmenuwindow, image=bgimage)
bglabel.place(x=0,y=0)

frame0 = Frame(mainmenuwindow, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

newaccbutton = Button(frame0, text="Services", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12, command=service).place(x= 1050, y=30 )
 

newaccbutton = Button(frame0, text="About Us", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1150, y=30 )

newaccbutton = Button(frame0, text="LogOut", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12, command=loginpage).place(x= 1250, y=30 )

userimg = ImageTk.PhotoImage(file='user2.png')
userimg_pil = Image.open('user2.png')
userimg_small_pil = userimg_pil.resize((60, 60))  # Reduce image size to 100x100
userimg_small = ImageTk.PhotoImage(userimg_small_pil)
button = Button(frame0, image=userimg_small, bg='black')
button.place(x=1410, y=0)



#######

image = Image.open("logo.png")
image = image.resize((150, 130), Image.LANCZOS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(image)

# Create a Label widget and display the resized image
label = Label(mainmenuwindow, image=photo)
label.place(x=1, y=1)



userimg = ImageTk.PhotoImage(file='user2.png')
userimg_pil = Image.open('user2.png')
userimg_small_pil = userimg_pil.resize((60, 60))  # Reduce image size to 100x100
userimg_small = ImageTk.PhotoImage(userimg_small_pil)
button = Button(mainmenuwindow, image=userimg_small, bg='black')
button.place(x=1410, y=0)


####
frame = Frame(mainmenuwindow, width=200, height=200, bg="black")
frame.place(x=100, y=200)

original_image1 = Image.open("careerpathway.png")
resized_image1 = original_image1.resize((160, 90), Image.LANCZOS)
image1 = ImageTk.PhotoImage(resized_image1)
image_label1 = Label(frame, image=image1)
image_label1.pack()
newaccbutton1 = Button(frame, text='Career Pathway', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=12,command=pathpage)
newaccbutton1.pack()

frame2 = Frame(mainmenuwindow, width=200, height=200, bg="black")
frame2.place(x=300, y=200)
original_image2 = Image.open("Test.png")
resized_image2 = original_image2.resize((160, 90), Image.LANCZOS)
image2 = ImageTk.PhotoImage(resized_image2)
image_label2 = Label(frame2, image=image2)
image_label2.pack()
newaccbutton2 = Button(frame2, text='Test', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=12,command=test)
newaccbutton2.pack()

frame3 = Frame(mainmenuwindow, width=200, height=200, bg="black")
frame3.place(x=100, y=400)
original_image = Image.open("user2.png")
resized_image3 = original_image.resize((160, 90), Image.LANCZOS)
image3 = ImageTk.PhotoImage(resized_image3)
image_label3 = Label(frame3, image = image3)
image_label3.pack()
newaccbutton3 = Button(frame3, text='Account', font=('open sans', 16,'bold'), fg='white', bg='darkblue', activeforeground='white', activebackground='blue', cursor='hand2', bd=0, width=12)
newaccbutton3.pack()


frame4 = Frame(mainmenuwindow, width=200, height=200, bg="black")
frame4.place(x=300, y=400)
original_image = Image.open("pic.png")
resized_image4 = original_image.resize((160, 90), Image.LANCZOS)
image4 = ImageTk.PhotoImage(resized_image4)
image_label4 = Label(frame4, image = image4)
image_label4.pack()
newaccbutton4 = Button(frame4, text='Chatbot', font=('open sans', 16,'bold'), fg='white', bg='darkblue', activeforeground='white', activebackground='blue', cursor='hand2', bd=0, width=12, command=chatbotpage)
newaccbutton4.pack()



frame5 = Frame(mainmenuwindow, width=200, height=200, bg="black")
frame5.place(x=100, y=600)
original_image = Image.open("contactus.jpeg")
resized_image5 = original_image.resize((160, 90), Image.LANCZOS)
image5 = ImageTk.PhotoImage(resized_image5)
image_label5 = Label(frame5, image = image5)
image_label5.pack()
newaccbutton5 = Button(frame5, text='Contact Us', font=('open sans', 16,'bold'), fg='white', bg='darkblue', activeforeground='white', activebackground='blue', cursor='hand2', bd=0, width=12, command=contact)
newaccbutton5.pack()


frame6 = Frame(mainmenuwindow, width=200, height=200, bg="black")
frame6.place(x=300, y=600)
original_image = Image.open("partnership.jpeg")
resized_image6 = original_image.resize((160, 90), Image.LANCZOS)
image6 = ImageTk.PhotoImage(resized_image6)
image_label6= Label(frame6, image = image6)
image_label6.pack()
newaccbutton6 = Button(frame6, text='Partnership', font=('open sans', 16,'bold'), fg='white', bg='darkblue', activeforeground='white', activebackground='blue', cursor='hand2', bd=0, width=12, command=contact)
newaccbutton6.pack()



mainmenuwindow.mainloop()
