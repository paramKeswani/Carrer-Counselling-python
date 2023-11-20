import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



pathway = tk.Tk()

pathway.geometry ("1500x800")
pathway.title ("Career Counselling")

bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(pathway, image=bgimage)
bglabel.place(x=0,y=0)



Label = tk.Label(pathway, text="INDIAN ARMY", font=('Arial', 25))
Label.pack(padx=20, pady=100)



T = Text(pathway, height = 15, width = 80, font=10)


Fact = """The Indian Armed Forces are the military forces of the Republic of India. It consists of three professional uniformed services: the Indian Army, Indian Navy, and Indian Air Force.[12] Additionally, the Indian Armed Forces are supported by the Central Armed Police Forces,[13] Assam Rifles, Indian Coast Guard and Special Frontier Force and various inter-service commands and institutions such as the Strategic Forces Command, the Andaman and Nicobar Command and the Integrated Defence Staff. The President of India is the Supreme Commander of the Indian Armed Forces but the executive authority and responsibility for national security is vested in the Prime Minister of India and their chosen Cabinet Ministers.[14][15][16][17] The Indian Armed Forces are under the management of the Ministry of Defence of the Government of India. With strength of over 1.4 million active personnel,[18][19] it is the world's second-largest military force and has the world's largest volunteer army.[20] It also has the third-largest defence budget in the world.[21] The Global Firepower Index report lists it as the fourth most-powerful military.[22]"""
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
