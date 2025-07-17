#Text()
from tkinter import*

window=Tk()
def show():
    var=text_1.get("1.0","end")
    lb.config(text=var)
#text box
text_1=Text(window,font=40,height=8)
text_1.place(x=10,y=10,width=500)

#button
bt=Button(window,text="ok",font=40,command=show)
bt.place(x=10,y=210,width=50)

# label
lb=Label(window,text="",font=40)
lb.place(x=10,y=260)
window.mainloop()