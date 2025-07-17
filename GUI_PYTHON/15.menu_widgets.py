from tkinter import *
window=Tk()

def new():
    print("hello")

main_menu=Menu(window)
window.config(menu=main_menu)

#file
f_menu=Menu(main_menu,tearoff=0,relief='raised')
f_menu.add_command(label="New file",command=new)
f_menu.add_separator()
f_menu.add_command(label="Open file")
f_menu.add_separator()

#submenu
sub_menu=Menu(f_menu,tearoff=0,relief="raised")
sub_menu.add_command(label="Red")
sub_menu.add_separator()
sub_menu.add_command(label="Yellow")
f_menu.add_cascade(label="Save file",menu=sub_menu)

f_menu.add_separator()
f_menu.add_command(label="save as file")
main_menu.add_cascade(label='File',menu=f_menu)

#Edit
f_menu1=Menu(main_menu,tearoff=0,relief='raised')
f_menu1.add_command(label="cut")
f_menu1.add_separator()
f_menu1.add_command(label="copy")
f_menu1.add_separator()
f_menu1.add_command(label="paste")
f_menu1.add_separator()
f_menu1.add_command(label="undo")
main_menu.add_cascade(label='Edit',menu=f_menu1)
window.mainloop()