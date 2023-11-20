from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
my_w = Tk()

import mysql.connector

variable_list = []
screen_width = my_w.winfo_screenwidth()
screen_height = my_w.winfo_screenheight()
my_w.geometry('1800x800+0+0')
my_w.geometry(f"{screen_width}x{screen_height}+0+0")
bgimage = ImageTk.PhotoImage(file='pathbg.png')

bglabel = Label(my_w, image=bgimage)
bglabel.place(x=0,y=0)

frame0 = Frame(my_w, width=1800, height=70, bg="black",)
frame0.place(x=0,y=0)

def home():
    my_w.destroy()
    import mainmenu
    
newaccbutton = Button(frame0, text="Home", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,command= home).place(x= 950, y=30 ) 
newaccbutton = Button(frame0, text="Services", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12, ).place(x= 1050, y=30 )
 

newaccbutton = Button(frame0, text="About Us", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12,).place(x= 1150, y=30 )

newaccbutton = Button(frame0, text="LogOut", font=('open sans', 12,'bold'), fg= 'white', bg='black', activeforeground='white' ,activebackground='black' ,cursor='hand2', bd=0,width=12, ).place(x= 1250, y=30 )

userimg = ImageTk.PhotoImage(file='user2.png')
userimg_pil = Image.open('user2.png')
userimg_small_pil = userimg_pil.resize((60, 60))  # Reduce image size to 100x100
userimg_small = ImageTk.PhotoImage(userimg_small_pil)
button = Button(frame0, image=userimg_small, bg='black')
button.place(x=1410, y=0)



conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='counselling')

my_w.geometry("1500x800")


frame1 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame1.pack(fill=X)
frame1.pack(padx=400,pady=(100,0),ipady=15)

frameu = Frame(frame1, width=780, height=40, bg="white",)
frameu.pack()

labela = Label(frameu, text='DISLIKE',font=('open sans', 16,'bold'), bg='white')
labela.pack(side='left', padx=(140,0))

labelb = Label(frameu, text='NEUTRAL',font=('open sans', 16,'bold'), bg='white')
labelb.pack(side='left' , padx=60)

labelc = Label(frameu, text='LIKE',font=('open sans', 16,'bold'), bg='white')
labelc.pack(side='left',  padx=(0, 190))


question = Label(frame1,text='install software on a large network'
                             ,background='RosyBrown2')
question.pack(pady=(50,0),padx=10)
question.config(font=('Helvetica bold', 17))
num1 = 5






dislike = Label(frame1,text="DISLIKE",background='RosyBrown2')
dislike.pack(side=LEFT,pady=(17,0),padx=(150,0))
dislike.config(font=('Helvetica bold', 15))


q_1_v = DoubleVar()

q_11 = Radiobutton(frame1, variable=q_1_v, value=1,bg='RosyBrown2')
q_11.pack(side =  LEFT,  fill =BOTH,padx=(20,0))
q_11.pack(pady=(17,0))

q_12 = Radiobutton(frame1, variable=q_1_v, value=2,bg='RosyBrown2')
q_12.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_12.pack(pady=(17,0))

q_13 = Radiobutton(frame1, variable=q_1_v, value=3,bg='RosyBrown2')
q_13.pack(side = LEFT,  fill = BOTH,padx=(10,0))
q_13.pack(pady=(17,0))

q_14 = Radiobutton(frame1, variable=q_1_v, value=4,bg='RosyBrown2')
q_14.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_14.pack(pady=(17,0))

q_15 = Radiobutton(frame1, variable=q_1_v, value=5,bg='RosyBrown2')
q_15.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_15.pack(pady=(17,0))




like = Label(frame1,text="LIKE",background='RosyBrown2')
like.pack(side=LEFT,padx=(0,145),pady=(17,0))
like.config(font=('Helvetica bold', 15))

variable_list.append(q_1_v)






num2 = 6
frame2 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame2.pack(fill=X)
frame2.pack(padx=400,pady=(0,0),ipady=15)


question = Label(frame2,text='buy and sell stocks and bonds ',background='RosyBrown2')
question.pack(pady=(50,0),padx=10)
question.config(font=('Helvetica bold', 17))






dislike = Label(frame2,text="DISLIKE",background='RosyBrown2')
dislike.pack(side=LEFT,pady=(17,0),padx=(150,0))
dislike.config(font=('Helvetica bold', 15))


q_2_v = DoubleVar()

q_21 = Radiobutton(frame2, variable=q_2_v, value=1,bg='RosyBrown2')
q_21.pack(side =  LEFT,  fill =BOTH,padx=(20,0))
q_21.pack(pady=(17,0))

q_22 = Radiobutton(frame2, variable=q_2_v, value=2,bg='RosyBrown2')
q_22.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_22.pack(pady=(17,0))

q_23 = Radiobutton(frame2, variable=q_2_v, value=3,bg='RosyBrown2')
q_23.pack(side = LEFT,  fill = BOTH,padx=(10,0))
q_23.pack(pady=(17,0))

q_24 = Radiobutton(frame2, variable=q_2_v, value=4,bg='RosyBrown2')
q_24.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_24.pack(pady=(17,0))

q_25 = Radiobutton(frame2, variable=q_2_v, value=5,bg='RosyBrown2')
q_25.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_25.pack(pady=(17,0))


like = Label(frame2,text="LIKE",background='RosyBrown2')
like.pack(side=LEFT,padx=(0,145),pady=(17,0))
like.config(font=('Helvetica bold', 15))
variable_list.append(q_2_v)






num3 = 7
frame3 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame3.pack(fill=X)
frame3.pack(padx=400,pady=(0,0),ipady=15)


question = Label(frame3,text='write books and plays',background='RosyBrown2')
question.pack(pady=(50,0),padx=10)
question.config(font=('Helvetica bold', 17))






dislike = Label(frame3,text="DISLIKE",background='RosyBrown2')
dislike.pack(side=LEFT,pady=(17,0),padx=(150,0))
dislike.config(font=('Helvetica bold', 15))


q_3_v = DoubleVar()

q_31 = Radiobutton(frame3, variable=q_3_v, value=1,bg='RosyBrown2')
q_31.pack(side =  LEFT,  fill =BOTH,padx=(20,0))
q_31.pack(pady=(17,0))

q_32 = Radiobutton(frame3, variable=q_3_v, value=2,bg='RosyBrown2')
q_32.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_32.pack(pady=(17,0))

q_33 = Radiobutton(frame3, variable=q_3_v, value=3,bg='RosyBrown2')
q_33.pack(side = LEFT,  fill = BOTH,padx=(10,0))
q_33.pack(pady=(17,0))

q_34 = Radiobutton(frame3, variable=q_3_v, value=4,bg='RosyBrown2')
q_34.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_34.pack(pady=(17,0))

q_35 = Radiobutton(frame3, variable=q_3_v, value=5,bg='RosyBrown2')
q_35.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_35.pack(pady=(17,0))


like = Label(frame3,text="LIKE",background='RosyBrown2')
like.pack(side=LEFT,padx=(0,145),pady=(17,0))
like.config(font=('Helvetica bold', 15))
variable_list.append(q_3_v)






num4=8
frame4 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame4.pack(fill=X)
frame4.pack(padx=400,pady=(0,0),ipady=15)


question = Label(frame4,text='love to learn about psycology, anthropology, etc',background='RosyBrown2')
question.pack(pady=(50,0),padx=10)
question.config(font=('Helvetica bold', 17))






dislike = Label(frame4,text="DISLIKE",background='RosyBrown2')
dislike.pack(side=LEFT,pady=(17,0),padx=(150,0))
dislike.config(font=('Helvetica bold', 15))


q_4_v = DoubleVar()

q_41 = Radiobutton(frame4, variable=q_4_v, value=1,bg='RosyBrown2')
q_41.pack(side =  LEFT,  fill =BOTH,padx=(20,0))
q_41.pack(pady=(17,0))

q_42 = Radiobutton(frame4, variable=q_4_v, value=2,bg='RosyBrown2')
q_42.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_42.pack(pady=(17,0))

q_43 = Radiobutton(frame4, variable=q_4_v, value=3,bg='RosyBrown2')
q_43.pack(side = LEFT,  fill = BOTH,padx=(10,0))
q_43.pack(pady=(17,0))

q_44 = Radiobutton(frame4, variable=q_4_v, value=4,bg='RosyBrown2')
q_44.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_44.pack(pady=(17,0))

q_45 = Radiobutton(frame4, variable=q_4_v, value=5,bg='RosyBrown2')
q_45.pack(side =  LEFT,  fill = BOTH,padx=(10,0))
q_45.pack(pady=(17,0))


like = Label(frame4,text="LIKE",background='RosyBrown2')
like.pack(side=LEFT,padx=(0,145),pady=(17,0))
like.config(font=('Helvetica bold', 15))

variable_list.append(q_4_v)







def fun():
    msg_box = messagebox.askquestion('Confirmation', 'Do you want to save these answerss?',default='no')
    if msg_box == 'yes':

        data_commit()
        final_table()
        my_w.destroy()
        import gptbar


    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')

def data_commit() :
    for num in range(1,len(variable_list)+1):
        ans = variable_list[num-1].get()

        cursor = conn.cursor()
        insert_stmt = (
            "INSERT INTO mcq(question_number, answers)"
            "VALUES ('%s', '%s')")
        data1 = (num, ans)
        try:

            cursor.execute(insert_stmt, data1)

            conn.commit()
        except:
            conn.rollback()

    pass

def final_table() :
    cursor = conn.cursor()
    try:
        cursor.execute(" insert into void(question_type,sum)"
"select question_number,sum(answers) from mcq where question_number % 5 = 1 group by question_number LIMIT 1;")
        conn.commit()




    except:
        conn.rollback()


    try:
        cursor.execute("insert into void(question_type,sum)"
"select question_number, sum(answers) as total_sum from mcq where question_number IN(2)group by question_number LIMIT 1;")
        conn.commit()




    except:
        conn.rollback()

    try:
        cursor.execute("insert into void(question_type,sum)"
"select question_number,sum(answers) as total_sum  from mcq where question_number IN(3)group by question_number LIMIT 1;")
        conn.commit()




    except:
        conn.rollback()


    try:
        cursor.execute("insert into void(question_type,sum)"
"select question_number,sum(answers) as total_sum  from mcq where question_number IN(4)group by question_number LIMIT 1;")
        conn.commit()




    except:
        conn.rollback()


    try:
        cursor.execute("insert into void(question_type,sum)"
"select question_number, SUM(answers) as total_sum  from mcq where question_number IN(5)group by question_number LIMIT 1;")
        conn.commit()




    except:
        conn.rollback()



image = Image.open("logo.png")
image = image.resize((150, 130), Image.LANCZOS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(image)

# Create a Label widget and display the resized image
label = Label(my_w, image=photo)
label.place(x=1, y=1)




b3 = Button(my_w, text = "SUBMIT",activeforeground = "green", width=10, activebackground = "pink",pady = 10,command=lambda : fun())
b3.place(x=1150,y=700)

my_w.mainloop()







import pandas as pd 
my_dict={
'NAME':['Ravi','Raju','Alex','Ronn'],
'MATH':[30,40,50,50]
}
df = pd.DataFrame(data=my_dict)
df.plot.pie(title="Std Mark",y='MATH')