import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image




pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)

def Commerce():
    pathway.destroy()
    import Commerce

def ARTS():
    pathway.destroy()
    import ARTS
    
Label = tk.Label(pathway, text="Career options after 12th", font=('Arial', 18))
Label.pack(padx=40, pady=40)


buttonframe = tk.Frame(pathway)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="Science", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn1 = tk.Button(buttonframe, text="Commerce", font=('Arial', 18), command= Commerce)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="Arts", font=('Arial', 18), command= ARTS)
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x',pady=250)

pathway.mainloop()
