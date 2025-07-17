#Entry()
from tkinter import *

window = Tk()
window.geometry("380x500")
var1=StringVar()
var2=StringVar()
def log_in():
    label.config(text=var1.get())
    labe2.config(text=var2.get())
#Email
label1=Label(window,text="Email",font=(50))
label1.place(x=20,y=100)
entry1=Entry(window,font=70,cursor="hand2",bd=7,textvariable=var1)
entry1.place(x=140,y=100,width=230)

#Password
label2=Label(window,text="Password",font=70,)
label2.place(x=20,y=140)
entry2=Entry(window,font=70,cursor="hand2",show="*",bd=7,textvariable=var2)
entry2.place(x=140,y=140,width=230)

#button
bt=Button(window,text="Login",font=30,bg="blue",command=log_in)
bt.place(x=170,y=200,width=170)

label=Label(window,text="",font=50)
label.place(x=20,y=260,height=120,width=350)
labe2=Label(window,text="",font=50)
labe2.place(x=20,y=370,height=110,width=350)


window.mainloop()