from tkinter import *
window=Tk()
window.title("Layout")
window.config(bg="blue")
window.attributes('-alpha',0.5)
window.geometry("400x500")
lab=Label(window, text="Label", font=("Time New Roman",30,"bold"), bg="Yellow")
lab.place(x=180,y=30,height=100,width=100)
window.mainloop()