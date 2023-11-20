import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from PIL import ImageTk, Image


my_conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='counselling')


cursor = my_conn.cursor(buffered=True)
query = "SELECT question_type, sum FROM void ORDER BY id DESC LIMIT 4"
df = pd.read_sql(query, my_conn)

# create a list of labels
labels = ["Humanities","Arts","Commerce","Science"]

# create a list of values
values = list(df['sum'])

# get the index of the maximum value
max_index = values.index(max(values))

# create a list of colors with the maximum value highlighted
colors = ['blue' if i != max_index else 'red' for i in range(len(values))]

# create bar chart with custom labels and colors
fig = Figure(figsize=(8, 6), dpi=100)
ax = fig.add_subplot(111)
ax.bar(labels, values, color=colors)
ax.set_title("Question Types")

def piechart():
    import gptpie

# create a tkinter window
root = tk.Tk()
root.title("Chart")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('1800x800+0+0')
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg='light blue')


frame0 = Frame(root, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)


def home():
    root.destroy()
    import mainmenu
    
newaccbutton = Button(frame0, text="Home", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command= home).place(x= 950, y=30 )
newaccbutton = Button(frame0, text="Services", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12, ).place(x= 1050, y=30 )
 

newaccbutton = Button(frame0, text="About Us", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1150, y=30 )

newaccbutton = Button(frame0, text="LogOut", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12, ).place(x= 1250, y=30 )

piebutton = Button(root, text="SHOW PIE CHART", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=16, command=piechart).place(x= 850, y=150 )

userimg = ImageTk.PhotoImage(file='user2.png')
userimg_pil = Image.open('user2.png')
userimg_small_pil = userimg_pil.resize((60, 60))  # Reduce image size to 100x100
userimg_small = ImageTk.PhotoImage(userimg_small_pil)
button = Button(frame0, image=userimg_small, bg='black')
button.place(x=1410, y=0)

label2 = Label(root, text="Congratulations!! You Have Completed your first step. \n We hope  that you found this test helpful" ,font=('Times New Roman', 16, 'bold'),  fg='BLACK', )
label2.place(x=250,y=110)

label2 = Label(root, text="Here are the Results" ,font=('Times New Roman', 16, 'bold'),  fg='BLACK', )
label2.place(x=250,y=170)

# create a tkinter canvas and display the chart on it
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=200, y=220)

image = Image.open("logo.png")
image = image.resize((150, 130), Image.LANCZOS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(image)

# Create a Label widget and display the resized image
label = Label(root, image=photo)
label.place(x=1, y=1)


label2 = Label(root, text="To Explore Your Dream Career" ,font=('Times New Roman', 16, 'bold'),  fg='BLACK', )
label2.place(x=1100,y=500)
label2 = Label(root, text="Let Us Continue Further..." ,font=('Times New Roman', 16, 'bold'),  fg='BLACK', )
label2.place(x=1100,y=540)

def pathpage():
    root.destroy()
    import trial

frame = Frame(root, width=200, height=200, bg="black")
frame.place(x=1150, y=640)

original_image1 = Image.open("careerpathway.png")
resized_image1 = original_image1.resize((160, 90), Image.LANCZOS)
image1 = ImageTk.PhotoImage(resized_image1)
image_label1 = Label(frame, image=image1)
image_label1.pack()
newaccbutton1 = Button(frame, text='Career Pathway', font=('open sans', 16,'bold'), fg= 'white', bg='darkblue', activeforeground='white' ,activebackground='blue' ,cursor='hand2', bd=0,width=12,command=pathpage)
newaccbutton1.pack()
# run the tkinter event loop
tk.mainloop()
