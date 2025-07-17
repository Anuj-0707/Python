# Toplevel()
from tkinter import *
window = Tk()
window.title("Python")
window.config(bg="red")
def Top():
    tp = Toplevel(window)
    tp.title("Java")
    tp.config(bg="blue")
    lb=Label(tp,text="Thank you")
    lb.place(x=10,y=10)
    tp.mainloop()

bt = Button(window,text="OK",command=Top)
bt.place(x=20,y=20)

window.mainloop()