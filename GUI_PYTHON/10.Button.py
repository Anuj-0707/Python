from tkinter import *
def python():
    lb.config(text="Python")
window=Tk()
window.geometry("200x200")
window.config(bg="Blue")
window.attributes('-alpha',0.7)
bt= Button(window,text="ON",font=("Time New Roman",20,"bold"),bg="Yellow",relief="sunken",command=python)
bt.place(x=100,y=100)
lb=Label(window,text="Hello",font=20,bg="Yellow")
lb.place(x=200,y=200)
window.mainloop()