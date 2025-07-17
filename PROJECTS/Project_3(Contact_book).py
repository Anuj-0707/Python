from tkinter import *
from tkinter.messagebox import showwarning, showinfo
window=Tk() # start
contacts = [] 

def add():
    name = var1.get().strip()
    phone = var2.get().strip()
    email = var3.get().strip()
    address = var4.get().strip()
    if name and phone and email and address:
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contacts.append(contact)
        listbox.insert(END, f"{name} | {phone}")
        clear_entries()
    else:
        showwarning("Input Error", "All fields are required!")

def delete():
    selected = listbox.curselection()
    if not selected:
        showwarning("Delete Error", "No contact selected!")
        return
    idx = selected[0]
    listbox.delete(idx)
    contacts.pop(idx)
    clear_entries()

def update():
    selected = listbox.curselection()
    if not selected:
        showwarning("Update Error", "No contact selected!")
        return
    idx = selected[0]
    name = var1.get().strip()
    phone = var2.get().strip()
    email = var3.get().strip()
    address = var4.get().strip()
    if name and phone and email and address:
        contacts[idx] = {"name": name, "phone": phone, "email": email, "address": address}
        listbox.delete(idx)
        listbox.insert(idx, f"{name} | {phone}")
        clear_entries()
    else:
        showwarning("Input Error", "All fields are required!")

def clear_entries():
    eb_nm.delete(0, END)
    eb_ph.delete(0, END)
    eb_em.delete(0, END)
    eb_adrs.delete(0, END)

def on_select(event):
    if not listbox.curselection():
        return
    idx = listbox.curselection()[0]
    contact = contacts[idx]
    var1.set(contact["name"])
    var2.set(contact["phone"])
    var3.set(contact["email"])
    var4.set(contact["address"])
#Setting window
window.geometry("500x700")
window.title("Contact list")
window.iconbitmap("Screenshot (8).ico")
window.resizable(False,False)
window.config(bg="aquamarine")

#heading
heading=Label(window,text="Contact Book",font=("Times New Roman",40,"bold"),fg="blue",bg="aquamarine")
heading.place(x=75,y=30,height=50,width=350)

#sub heading
sub_heading=Label(window,text="Contact Details",font=("Times New Roman",30,"bold"),fg="blue",bg="aquamarine")
sub_heading.place(x=30,y=100,height=40,width=290)


#Contact details entry and labels
# Name
var1=StringVar()
name=Label(window,text="Name",font=("Times New Roman",20,"bold"),fg="blue",bg="aquamarine")
name.place(x=30,y=160,height=30,width=85)
eb_nm=Entry(window,font=20,bd=4,relief="sunken",textvariable=var1)
eb_nm.place(x=200,y=160,height=30,width=250)

#phone number
var2=StringVar()
ph_num=Label(window,text="Mob Num",font=("Times New Roman",20,"bold"),fg="blue",bg="aquamarine")
ph_num.place(x=30,y=200,height=30,width=130)
eb_ph=Entry(window,font=20,bd=4,relief="sunken",textvariable=var2)
eb_ph.place(x=200,y=200,height=30,width=250)

#email
var3=StringVar()
email=Label(window,text="E-mail",font=("Times New Roman",20,"bold"),fg="blue",bg="aquamarine")
email.place(x=30,y=240,height=30,width=90)
eb_em=Entry(window,font=20,bd=4,relief="sunken",textvariable=var3)
eb_em.place(x=200,y=240,height=30,width=250)

#address
var4=StringVar()
address=Label(window,text="Address",font=("Times New Roman",20,"bold"),fg="blue",bg="aquamarine")
address.place(x=30,y=280,height=30,width=100)
eb_adrs=Entry(window,font=20,bd=4,relief="sunken",textvariable=var4)
eb_adrs.place(x=200,y=280,height=30,width=250)

#buttons
bt1=Button(window,text="Add",font=("Times New Roman",20,"bold"),fg="blue",bg="white",cursor="hand2",command=add)
bt1.place(x=85,y=330,height=30,width=90)
bt1=Button(window,text="Delete",font=("Times New Roman",20,"bold"),fg="blue",bg="white",cursor="hand2",command=delete)
bt1.place(x=205,y=330,height=30,width=90)
bt1=Button(window,text="Update",font=("Times New Roman",20,"bold"),fg="blue",bg="white",cursor="hand2",command=update)
bt1.place(x=325,y=330,height=30,width=90)

#listbox
listbox=Listbox(window)
listbox.place(x=10,y=390,height=300,width=480)
listbox.bind('<<ListboxSelect>>', on_select)

window.mainloop() # end