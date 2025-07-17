# Scrollbar
from tkinter import *
from tkinter import ttk
window=Tk()

text= Text(window,font=(30))
text.place(x=10,y=10,height=500,width=500)

scrollbar=Scrollbar(window,orient="vertical",command=text.yview)
scrollbar.place(x=500,y=10,height=500,width=30)

text["yscrollcommand"]=scrollbar.set
window.mainloop()