from tkinter import *
from tkinter import messagebox
my_w = Tk()

import mysql.connector

variable_list = []

conn = mysql.connector.connect(
                    user='root', password='', host='127.0.0.1', database='counselling')



my_w.geometry("1500x800")
my_w.configure(background="bisque2")

frame1 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame1.pack(fill=X)
frame1.pack(padx=400,pady=(60,0),ipady=15)


question = Label(frame1,text='Inspect a roof for leaks '
                             ,background='RosyBrown2')
question.pack(pady=(50,0),padx=10)
question.config(font=('Helvetica bold', 17))
num1 = 1






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






num2 = 2
frame2 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame2.pack(fill=X)
frame2.pack(padx=400,pady=(0,0),ipady=15)


question = Label(frame2,text='Use precision machines to build '
                             'custom metal parts',background='RosyBrown2')
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






num3 = 3
frame3 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame3.pack(fill=X)
frame3.pack(padx=400,pady=(0,0),ipady=15)


question = Label(frame3,text='Analyze the structure of molecules',background='RosyBrown2')
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






num4=4
frame4 = Frame(my_w, highlightbackground="black", highlightthickness=5,bg='RosyBrown2')
frame4.pack(fill=X)
frame4.pack(padx=400,pady=(0,0),ipady=15)


question = Label(frame4,text='Do scientific experiments',background='RosyBrown2')
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


def home():
    my_w.destroy()
    import page2


newaccbutton = Button(my_w, text="Home", font=('open sans', 12, 'bold'), fg='white', bg='black',
                      activeforeground='white', activebackground='black', cursor='hand2', bd=0, width=12,
                      command=home).place(x=950, y=30)



def fun():
    msg_box = messagebox.askquestion('Confirmation', 'Do you want to save these answers?',default='no')
    if msg_box == 'yes':

        data_commit()
        final_table()
        my_w.destroy()


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








b3 = Button(my_w, text = "SUBMIT",activeforeground = "green",activebackground = "pink",pady = 10,command=lambda : fun())
b3.pack(side = BOTTOM)

my_w.mainloop()







import pandas as pd 
my_dict={
'NAME':['Ravi','Raju','Alex','Ronn'],
'MATH':[30,40,50,50]
}
df = pd.DataFrame(data=my_dict)
df.plot.pie(title="Std Mark",y='MATH')