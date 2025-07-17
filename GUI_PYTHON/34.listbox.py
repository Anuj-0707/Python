## To_do_list
# Listbox()
from tkinter import *
from tkinter.messagebox import showwarning
window = Tk()
list=[]
#Functions
def add_list():
    task=var.get() 
    if task:
        list.append(task)
        update_list()
        eb.delete(0,END)
    else:
        showwarning(title="Input Error",message="Enter a task")

def delete_list():
    try:
        point=listbox.curselection()[0]
        list.pop(point)
        update_list()
    except:
        showwarning(title="Selection Error",message="Please select a Task\nSelected task will be deleted only")

def update_list():
    listbox.delete(0,END)
    for task in list:
        listbox.insert(END,task)

# Window
window.geometry("300x450")
window.config(bg="grey")
window.attributes('-alpha',0.7)
window.iconbitmap("Screenshot (8).ico")
window.title("To_do_list")

#Entrybox
var=StringVar()
eb = Entry(window,font=("Times New Roman",20,"bold"),cursor="hand2",textvariable=var)
eb.place(x=50,y=20,height=40,width=200)

#add_buttons
add_button=Button(window,text="Add Task",font=("Times New Roman",20,"bold"),cursor="hand2",bg="cornflowerblue",command=add_list)
add_button.place(x=75,y=90,height=30,width=150)

#delete_button
delete_button=Button(window,text="Delete Task",font=("Times New Roman",20,"bold"),cursor="hand2",bg="cornflowerblue",command=delete_list)
delete_button.place(x=70,y=150,height=30,width=160)


#List box
listbox = Listbox(window,font=("Times New Roman",20,"bold"))
listbox.place(x=20,y=220,height=210,width=260)


window.mainloop()