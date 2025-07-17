# Notebook
from tkinter import *
from tkinter import ttk
window=Tk()
notebook = ttk.Notebook(window)
notebook.pack(pady=10,expand=True)

frame1 = ttk.Frame(notebook,height=300,width=300)
frame1.pack(fill="both",expand=True)
lb_frame1 = Label(frame1,text="Python")
lb_frame1.place(x=10,y=10)

frame2 = ttk.Frame(notebook,height=300,width=300)
frame2.pack(fill="both",expand=True)
lb_frame2=Label(frame2,text="Java")
lb_frame2.place(x=10,y=10)

notebook.add(frame1,text="NEW")
notebook.add(frame2,text="OPEN")

window.mainloop()