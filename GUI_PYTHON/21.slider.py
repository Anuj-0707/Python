# Scale()
from tkinter import *
from tkinter import ttk
window=Tk()
def call(p):
    p=str(var.get())
    lb.config(text=p)


var=DoubleVar()

scale=Scale(window,from_=0.0,to=100.0,orient="vertical",variable=var,command=call)
scale.place(x=100,y=100)

lb=Label(window,text="",font=(50))
lb.place(x=200,y=200)
window.mainloop()