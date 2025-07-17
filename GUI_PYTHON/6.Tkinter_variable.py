# there are four types of variables:
#BooleanVar()
#StrinVar()
#IntVar()
#DoubleVar()
#var=Tkinter_variable(master,value=any_value)
from tkinter import *
window=Tk()
#var = StringVar(window, value="Hello")
var = IntVar(window, value=25)
#var = BooleanVar(window, value=True)
#var = DoubleVar(window, value=12.34)
print(var.get())
window.mainloop()