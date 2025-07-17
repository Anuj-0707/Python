#askokcancel()
from tkinter import *
from tkinter.messagebox import askokcancel
window = Tk()

def okcancel():
    ans = askokcancel(title="Python",message="Welcome to python")
    print(ans)

bt= Button(window,text="OK",command=okcancel)
bt.pack()






window.mainloop()