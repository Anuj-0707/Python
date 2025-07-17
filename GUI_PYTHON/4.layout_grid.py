from tkinter import *
window=Tk()
window.config(bg="Blue")
window.attributes('-alpha',0.7)
lab=Label(window, text="hello", font=("Time Now Roman",30,"bold"),bg="Yellow")
lab.grid(row=0,column=0)#use row column
lab1=Label(window, text="Welcome", font=("Time Now Roman",30,"bold"),bg="Yellow")
lab1.grid(row=1,column=0)
window.mainloop()