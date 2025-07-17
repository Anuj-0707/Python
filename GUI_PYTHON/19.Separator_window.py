# Separator()
from tkinter import *
from tkinter import ttk
window = Tk()

label1 = Label(window,text="Python",font=60)
label1.pack()

sep=ttk.Separator(window,orient="horizontal")
sep.pack(fill=X)

label2 = Label(window,text="Java",font=60)
label2.pack()
window.mainloop()