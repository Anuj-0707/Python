# Report Card Generator
from tkinter import *
from tkinter.messagebox import showinfo ,askokcancel 

# main window
window = Tk() # start
window.config(bg="Blue")
window.attributes('-alpha',0.7)
window.title("ABC School")
window.iconbitmap("Screenshot (7).ico")
window.geometry("600x550")
window.resizable(False,False)

#defining the functions
def get_data():
    name=st_nm_1.get()
    m1=hindi_marks.get()
    m2=english_marks.get()
    m3=science_marks.get()
    m4=maths_marks.get()
    m5=sst_marks.get()

    total_marks=m1+m2+m3+m4+m5
    percent=total_marks/5
    division=""
    if percent>=60:
        division="1st Division"
    elif percent>=50:
        division="2nd Division"
    elif percent>=35:
        division="3rd Division"
    else:
        division="Fail"
    print(total_marks)
    print(percent)
    print(division)

    messagebox(name,total_marks,percent,division)

def messagebox(*data):
    print_1=f"""
    Name        : {data[0]}
    Total marks : {data[1]}
    Percentage  : {data[2]}
    Division    : {data[3]}
    """
    askokcancel(title="RESULT",message=print_1)

# Title in the window
school_name = Label(window,text="ABC School",font=("lucida Calligraphy",40,"bold"),bg="blue")
school_name.place(x=120,y=20,height=55,width=360)

# Student name
st_nm = Label(window,text="Student Name",font=("Times New Roman",20,"bold"),bg="blue")
st_nm.place(x=30,y=80,height=30,width=165)
st_nm_1=StringVar()
st_nm_Entry = Entry(window,font=("Times New Roman",20,"bold"),textvariable=st_nm_1)
st_nm_Entry.place(x=225,y=80,height=30,width=300)

# Title in the window
subj_name = Label(window,text="Subjects",font=("Times New Roman",30,"bold"),bg="blue")
subj_name.place(x=30,y=130,height=40,width=200)
marks = Label(window,text="Marks",font=("Times New Roman",30,"bold"),bg="blue")
marks.place(x=330,y=130,height=40,width=200)

# Assigning the subjects
list = ["Hindi","English","Science","Mathematics","Social Studies"]
# Hindi
sb_nm1 = Label(window,text="Hindi",font=("Times New Roman",20,"bold"),bg="white")
sb_nm1.place(x=30,y=190,height=30,width=190)
hindi_marks=DoubleVar()
sb_nm1_Entry = Entry(window,font=("Times New Roman",20,"bold"),textvariable=hindi_marks)
sb_nm1_Entry.place(x=330,y=190,height=30,width=200)

#english
sb_nm2 = Label(window,text="English",font=("Times New Roman",20,"bold"),bg="white")
sb_nm2.place(x=30,y=240,height=30,width=190)
english_marks=DoubleVar()
sb_nm2_Entry = Entry(window,font=("Times New Roman",20,"bold"),textvariable=english_marks)
sb_nm2_Entry.place(x=330,y=240,height=30,width=200)

#Maths
sb_nm3 = Label(window,text="Mathematics",font=("Times New Roman",20,"bold"),bg="white")
sb_nm3.place(x=30,y=290,height=30,width=190)
maths_marks=DoubleVar()
sb_nm3_Entry = Entry(window,font=("Times New Roman",20,"bold"),textvariable=maths_marks)
sb_nm3_Entry.place(x=330,y=290,height=30,width=200)

#science
sb_nm4 = Label(window,text="Science",font=("Times New Roman",20,"bold"),bg="white")
sb_nm4.place(x=30,y=340,height=30,width=190)
science_marks=DoubleVar()
sb_nm4_Entry = Entry(window,font=("Times New Roman",20,"bold"),textvariable=science_marks)
sb_nm4_Entry.place(x=330,y=340,height=30,width=200)

# sst
sb_nm5 = Label(window,text="Social Studies",font=("Times New Roman",20,"bold"),bg="white")
sb_nm5.place(x=30,y=390,height=30,width=190)
sst_marks=DoubleVar()
sb_nm5_Entry = Entry(window,font=("Times New Roman",20,"bold"),textvariable=sst_marks)
sb_nm5_Entry.place(x=330,y=390,height=30,width=200)

# Button
bt = Button(window,text="Generate",font=("Times New Roman",20,"bold"),cursor="hand2",command=get_data)
bt.place(x=230,y=490,height=30,width=140)

window.mainloop()