#Checkbutton
from tkinter import *
def test():
    lb.config(text=var.get())
window=Tk()
var =StringVar()
cb = Checkbutton(window,text="Python", font=(30), variable=var,onvalue="python",offvalue="java")
cb.pack()
lb=Label(window,text="",font=30)
lb.pack()
bt = Button(window,text="Python",font=30,command=test)
bt.pack()
window.mainloop()