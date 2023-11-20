from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Chatbot():
    def __init__(self,root):
        self.root = root
        self.root.title('ChatBot')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry('1800x800+0+0')
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        
        frame0 = Frame(self.root, width=1800, height=70, bg="black",)
        frame0.place(x=0,y=0)
        def home():
            self.root.destroy()
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



        self.root.bind('<Return>',self.enter_fun)

        self.logo = ImageTk.PhotoImage(file='logo.png')
        self.logolabel = Label(root,image=self.logo)
        self.logolabel.place(x=1,y=5)

        main_frame = Frame(self.root, bd = 4, bg='powder blue',width=610)
        main_frame.pack(pady=(80,0))

        img_chat = Image.open('pic.jpg')
        img_chat = img_chat.resize((150,150))
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw',width=730,compound= LEFT, 
                            image=self.photoimg,text="Let's Chat",font = ('arial',30,'bold'),fg='green',bg='white') 
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame = Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label1 = Label (btn_frame,text='Type Something',font = ('arial',20,'bold'),fg='green',bg='white')
        label1.grid(row=0,column=0,padx=5,sticky=W)


        self.entry= StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry, width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send= Button(btn_frame,text="Send >>",command=self.send, font=('arial',15,'bold'),width=8,bg='green',)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear= Button(btn_frame,text="Clear",command= self.clear, font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=1,padx=5,sticky=W)

        self.msg=''
        self.label11 = Label (btn_frame,text=self.msg,font = ('arial',20,'bold'),fg='red',bg='white')
        self.label11.grid(row=1,column=2,padx=5,sticky=W)

    def send(self):
        send= '\t\t\t'+'You :'+self.entry.get()
        self.text.insert(END, '\n' +send)
        self.text.yview(END)
        

        if (self.entry.get()== ''):
            self.msg='Please enter some input'
            self.label11.config(text=self.msg,fg='red')
        
        else:
            self.msg=''
            self.label11.config(text=self.msg,fg='red')

     

        if (self.entry.get()== 'hii' or self.entry.get()== 'hello' or self.entry.get()== 'hi' or self.entry.get()== 'Hii' or self.entry.get()== 'Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello Sir')
            self.text.insert(END,'\t'+'How can I help you ?')

        elif (self.entry.get()== 'how will personal assessment help me in my career' or self.entry.get()== 'how will career assessment help me'):
            self.text.insert(END,'\n\n'+'Bot: Personal assessment helps you know yourself better, \n enabling you to pursue the right career path, \n set goals, and develop strategies to succeed in your professional life. \n you can go to test section to get your personal assesment')

        elif (self.entry.get()== 'can i get one to one counselling session'):
            self.text.insert(END,'\n\n'+'Bot: Yes, Absolutely, \n Please fill the contact form and our counselling team will contact you shortly')

        elif (self.entry.get()== 'what is your name'):
            self.text.insert(END,'\n\n'+'Bot: I am chatbot. \n I am here for your help')

        elif (self.entry.get()== 'what is your name'):
            self.text.insert(END,'\n\n'+'Bot: I am chatbot. \n I am here for your help')

        elif(self.entry.get()== 'thank you' or self.entry.get()== 'Thank you' or self.entry.get()== 'thanks' or self.entry.get()== 'thank you so much'):
             self.text.insert(END,"\n\n"+"Bot: You're most welcome sir.")

        elif(self.entry.get()== ''):
             self.text.insert(END,'')

        elif(self.entry.get()== 'what can you do'):
             self.text.insert(END,'\n\n'+'Bot: I am here to help you to solve your queries regarding the system.')

        elif(self.entry.get()== 'what does career pathway include' or self.entry.get()== 'what  does career pathway include'):
             self.text.insert(END,'\n\n'+'Bot: Sir, Our career pathway will provide you overview of all the career you can pursue after 10th and 12th')

        else:
            self.text.insert(END,'\n\n'+"Bot: Sorry I didn't get it. \n I will convey this message to our team and your query will be solved shortly. \n Thank You for your patience")

    def enter_fun(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set()

if __name__ == '__main__':
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()