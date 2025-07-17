# askcolor
from tkinter import *
from tkinter.colorchooser import askcolor
window=Tk()

def color():
    ans = askcolor(title="COLORS")
    print(ans)
    window.config(bg=ans[1])

bt= Button(window,text="OK",command=color)
bt.place(x=20,y=20,height=30,width=30)


window.mainloop()