#Radiobutton
from tkinter import *
window=Tk()
def test():
    lb.config(text=var.get())
list_1=(("python","Python"),("Java","j"),("c++","cpp"))
var=StringVar()
for i in list_1:
    radio_button1=Radiobutton(window,text=i[0],value=i[1],variable=var,command=test,cursor="hand2")
    radio_button1.deselect()
    radio_button1.pack()
lb=Label(window,text="",font=(30))
lb.pack()
window.mainloop()