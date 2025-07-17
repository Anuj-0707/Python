from tkinter import *
window=Tk()
def text(var):
    var=value.get()
    lb.config(text=var)

opt_list=["C","C++","Python","Java"]

value=StringVar()
value.set("Language")

op=OptionMenu(window,value,command=text,*opt_list)
op.place(x=100,y=100,height=30,width=100)

lb=Label(window,text="")
lb.place(x=300,y=100,height=30,width=100)
window.mainloop()