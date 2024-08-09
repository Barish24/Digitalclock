from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('clock')

def time():
    string = strftime('%H:%M:%S %p')
    lb1.config(text = string)
    lb1.after(1000,time)
    
lb1 = Label(root,font=('calibri',40,'bold'),background='purple',foreground='white')

lb1.pack(anchor='center')
time()

mainloop()



