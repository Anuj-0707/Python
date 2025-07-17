# Status Bar
from tkinter import *
window=Tk()
def change():
    Status_bar.config(text="GO")

Status_bar = Label(window,text="ready",relief="sunken",anchor=W,bd=5)
Status_bar.pack(side='bottom',fil=X)

bt = Button(window,text="OK",command=change)
bt.pack()

window.mainloop()