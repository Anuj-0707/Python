# askretrycancel
from tkinter import *
from tkinter.messagebox import askretrycancel
window=Tk()

def retry_cancel():
    ans = askretrycancel(title="Python",message="Welcome to python")
    if ans==True:
        retry_cancel()
    else:
        lb.config(text="Thank you")

lb=Label(window,text="",font=(40))
lb.place(x=10,y=100)

bt=Button(window,text="OK",command=retry_cancel)
bt.place(x=10,y=10,height=30,width=30)

window.mainloop()