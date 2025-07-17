from tkinter import *
window=Tk()
window.title("Layout")
window.config(bg="blue")
window.attributes('-alpha',0.5)
window.geometry("400x500")
#pack geometry
lab=Label(window, text="Label", font=("Time New Roman",30,"bold"), bg="Yellow")
#lab.pack() # use of padx and pady 
lab.pack(padx=30,pady=30)
#internal change
#lab.pack(ipadx=50,ipady=50)
lab.pack(ipadx=50,fill='x')
window.mainloop()
