import tkinter as tk
import pandas as pd
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

# establish database connection
my_conn = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='counselling')
cursor = my_conn.cursor(buffered=True)

# execute SQL query and create pandas dataframe
query = "SELECT question_type, sum FROM void ORDER BY id DESC LIMIT 4"
df = pd.read_sql(query, my_conn)

# create a list of labels
labels = ["Humanities","Arts","Commerce","Science"]

# get the index of the slice with the maximum value
max_index = df['sum'].idxmax()

# create a list to hold the explode values
explode = [0] * len(labels)
explode[max_index] = 0.1  # explode the slice with the maximum value

# create the pie chart
fig, ax = plt.subplots()
ax.pie(df['sum'], labels=labels, explode=explode)
ax.set_title("Question Types")

# create a Tkinter window and add the pie chart to it
root = tk.Tk()


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# start the Tkinter event loop
tk.mainloop()
