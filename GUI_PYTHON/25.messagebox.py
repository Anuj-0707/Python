#Message box
from tkinter import *
from tkinter.messagebox import showinfo,showerror,showwarning
window=Tk()
def test():
    showinfo(title="Python Info", message="Hello Python")
    showerror(title="Python Info", message="Hello Python")
    showwarning(title="Python Info", message="Hello Python")

bt = Button(window,text="OK",command=test)
bt.place(x=10,y=10,height=30,width=40)



window.mainloop()