# Combobox()
from tkinter import   *
from tkinter import ttk
window=Tk()

def entry():
    p=var.get()
    lb.config(text=p)
list = ["C","C++","java","Python"]
var=StringVar()
combo = ttk.Combobox(window,value=list,height=30,width=40,font=40,textvariable=var)
combo.set("C")
combo.place(x=10,y=50)

lb=Label(window,text="",font=(40))
lb.place(x=100,y=200)

bt=Button(window,text="ok",font=30,command=entry)
bt.pack()
window.mainloop()