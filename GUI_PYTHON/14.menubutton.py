#menu button
from tkinter import *
window=Tk()
def do():
    lb.config(text="Open menu")
menu_Button=Menubutton(window,text="File",relief="raised")
menu_Button.menu=Menu(menu_Button,tearoff=0)
menu_Button["menu"]=menu_Button.menu
menu_Button.menu.add_checkbutton(label="New File",command=do)
menu_Button.menu.add_checkbutton(label="Open File")
menu_Button.menu.add_checkbutton(label="Save File")
menu_Button.pack()
lb=Label(window,text="",font=30)
lb.pack()
window.mainloop()