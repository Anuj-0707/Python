from tkinter import *
window=Tk()
window.config(bg="Yellow")
photo = PhotoImage(file="Screenshot (logo.png")
lb = Label(window,image=photo,bg="Red",text="Info Tech",font=("Times New Roman",30,"bold"),compound="top")
lb.place(x=100,y=100)
window.mainloop()