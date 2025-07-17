# Spinbox
from tkinter import *
from tkinter import ttk
window=Tk()
def show():
    lb.config(text=str(var.get()))

var=IntVar()
Spin= Spinbox(window,font=(30),from_=0 ,to=10,textvariable=var,wrap=True,command=show)
Spin.place(x=10,y=10,height=30,width=50)

lb= Label(window,text="",font=(30))
lb.place(x=200,y=100,height=300,width=300)
window.mainloop()