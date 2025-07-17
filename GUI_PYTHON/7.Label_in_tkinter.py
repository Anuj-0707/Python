from tkinter import *
entry = input("Enter your data: ")
window = Tk()
window.config(bg="Red")
window.geometry("400x400")
window.attributes('-alpha',0.8)
var=StringVar()
lbl=Label(window, text="Hello Welcome \nto \nThe new world", font=("Arial Rounded MT Bold",20,"bold"),fg="black",bg="yellow",cursor="hand2",relief="sunken",justify="left",underline=2)# to remove bg blend it with windows bg colour
# using tyext variable
#lbl=Label(window, textvariable=var, font=("Arial Rounded MT Bold",20,"bold"),fg="black",bg="yellow",cursor="hand2",relief="sunken",justify="left")# to remove bg blend it with windows bg colour
lbl.place(x=100,y=100)
var.set(entry)
window.mainloop()