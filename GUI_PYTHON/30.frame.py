from tkinter import *
window= Tk()

window.attributes('-alpha',0.7)
frame= Frame(window,bd=8,bg="red",relief="sunken")
frame.place(height=600,width=600)

lb=Label(frame,text="Hello",font=50)
lb.place(x=300,y=200,height=100,width=100)
window.mainloop()