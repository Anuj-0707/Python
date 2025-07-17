# Calculator
from tkinter import *
window=Tk() #start

data = ""
#function
def get_data(val):
    global data
    data = data+str(val)
    var.set(data)

def equal_data():
    global data
    try:
        total = str(eval(data))
        var.set(total)
    except:
        var.set("Error")

def clear():
    global data
    data=""
    var.set(data)


# Setting Up The Window
window.title("CALCULATOR")
window.config(bg="black")
window.geometry("400x550")
window.resizable(False,False)

# Title
lb = Label(window,text="CALCULATOR",font=("Times New Roman",30,"bold"),bg="black",fg="white")
lb.place(x=50,y=20,height=40,width=300)

#Frame
frame=Frame(window,bg="white")
frame.place(x=19,y=89,height=42,width=362)

# ENTRY BOX
var=StringVar()
eb = Entry(window,font=("Times New Roman",30,"bold"),bg="black",fg="white",textvariable=var)
eb.place(x=20,y=90,height=40,width=360)

#buttons
bt_1 = Button(window,text="1",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(1))
bt_1.place(x=20,y=190,height=60,width=90)

bt_2 = Button(window,text="2",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(2))
bt_2.place(x=110,y=190,height=60,width=90)

bt_3 = Button(window,text="3",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(3))
bt_3.place(x=200,y=190,height=60,width=90)

bt_add = Button(window,text="+",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data("+"))
bt_add.place(x=290,y=190,height=60,width=90)

bt_4 = Button(window,text="4",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(4))
bt_4.place(x=20,y=250,height=60,width=90)

bt_5 = Button(window,text="5",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(5))
bt_5.place(x=110,y=250,height=60,width=90)

bt_6 = Button(window,text="6",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(6))
bt_6.place(x=200,y=250,height=60,width=90)

bt_sub = Button(window,text="-",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data("-"))
bt_sub.place(x=290,y=250,height=60,width=90)

bt_7 = Button(window,text="7",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(7))
bt_7.place(x=20,y=310,height=60,width=90)

bt_8 = Button(window,text="8",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(8))
bt_8.place(x=110,y=310,height=60,width=90)

bt_9 = Button(window,text="9",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(9))
bt_9.place(x=200,y=310,height=60,width=90)

bt_mul = Button(window,text="*",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data("*"))
bt_mul.place(x=290,y=310,height=60,width=90)

bt_clear = Button(window,text="C",bg="grey",font=("Times New Roman",30,"bold"),command=clear)
bt_clear.place(x=20,y=370,height=60,width=90)

bt_0 = Button(window,text="0",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data(0))
bt_0.place(x=110,y=370,height=60,width=90)

bt_dot = Button(window,text=".",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data("."))
bt_dot.place(x=200,y=370,height=60,width=90)

bt_div = Button(window,text="/",bg="grey",font=("Times New Roman",30,"bold"),command=lambda:get_data("/"))
bt_div.place(x=290,y=370,height=60,width=90)

bt_equal= Button(window,text="=",bg="grey",font=("Times New Roman",30,"bold"),command=equal_data)
bt_equal.place(x=110,y=430,height=60,width=180)

window.mainloop() #end