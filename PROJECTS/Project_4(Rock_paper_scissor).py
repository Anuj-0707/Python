from tkinter import *
import random
from tkinter.messagebox import showinfo,showwarning
window = Tk() # START
list=["Rock","Paper","Scissor"]

# Function
def comp_choice():
     return random.choice(list)

def rock_selected():
        rndm=comp_choice()
        if rndm=="Rock":
            showinfo(title="Result",message="Your choice: Rock\nComp choice: Rock\nNobody wins")
        elif rndm=="Paper":
            showinfo(title="Result",message="Your choice: Rock\nComp choice: Paper\nYou loose!")
        else:
            showinfo(title="Result",message="Your choice: Rock\nComp choice: Scissor\nYou win!")
        
def paper_selected():
        rndm=comp_choice()
        if rndm=="Rock":
            showinfo(title="Result",message="Your choice: Paper\nComp choice: Rock\nYou win!")
        elif rndm=="Paper":
            showinfo(title="Result",message="Your choice: Paper\nComp choice: Paper\nNobody wins")
        else:
            showinfo(title="Result",message="Your choice: Paper\nComp choice: Scissor\nYou loose")
        
def scissor_selected():
        rndm=comp_choice()                
        if rndm=="Rock":
            showinfo(title="Result",message="Your choice: Scissor\nComp choice: Rock\nYou loose")
        elif rndm=="Paper":
            showinfo(title="Result",message="Your choice: Scissor\nComp choice: Paper\n You win!")
        else:
            showinfo(title="Result",message="Your choice: Scissor\nComp choice: Scissor\nNobody wins") 

#Window setup
window.geometry("300x250")
window.config(bg="deepskyblue")
window.title("Rock_paper_scissor Game")
window.iconbitmap("Game logo_1.ico")
window.resizable(False,False)

#Heading
lb=Label(window,text="GAME",font=("Bauhaus 93",30),bg="deepskyblue",fg="navy")
lb.place(x=100,y=20,height=40,width=100)

#sub heading
lb1=Label(window,text="Rock Paper Scissor",font=("Bauhaus 93",20),bg="deepskyblue",fg="navy")
lb1.place(x=30,y=80,height=30,width=240)

#Choose one
lb2=Label(window,text="Choose one",font=("Bauhaus 93",15),bg="deepskyblue",fg="navy")
lb2.place(x=30,y=130,height=20,width=110)

#buttons
# Rock
var1=StringVar()
bt1=Button(window,text="Rock",font=("Bauhaus 93",15),bg="cornflowerblue",fg="navy",cursor="hand2",command=rock_selected)
bt1.place(x=9,y=170,height=20,width=90)

# Paper
var2=StringVar()
bt1=Button(window,text="Paper",font=("Bauhaus 93",15),bg="cornflowerblue",fg="navy",cursor="hand2",command=paper_selected)
bt1.place(x=105,y=170,height=20,width=90)

#Scissor
var3=StringVar()
bt1=Button(window,text="Scissor",font=("Bauhaus 93",15),bg="cornflowerblue",fg="navy",cursor="hand2",command=scissor_selected)
bt1.place(x=201,y=170,height=20,width=90)

# END
window.mainloop()