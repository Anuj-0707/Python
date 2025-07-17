#LabelFrame()
from tkinter import *
window=Tk()
Label_Frame= LabelFrame(window,text="Python",font=(30),labelanchor=N)
Label_Frame.place(x=150,y=200,height=150,width=500)
Label_1= Label(window,text="Java",font=(30))
Label_1.place(x=180,y=270)
window.mainloop()