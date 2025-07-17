from tkinter import *
import random
from tkinter.messagebox import showinfo

# Initialize window
window = Tk()
window.geometry("300x300")
window.config(bg="deepskyblue")
window.title("Rock Paper Scissor Game")
# window.iconbitmap("Game logo_1.ico")  # Uncomment only if you have the icon file

options = ["Rock", "Paper", "Scissor"]

# Function
def get_computer_choice():
    return random.choice(options)

def rock_selected():
    comp = get_computer_choice()
    if comp == "Rock":
        showinfo(title="Result", message=f"Your choice: Rock\nComp choice: Rock\nNobody wins")
    elif comp == "Paper":
        showinfo(title="Result", message=f"Your choice: Rock\nComp choice: Paper\nYou lose!")
    else:
        showinfo(title="Result", message=f"Your choice: Rock\nComp choice: Scissor\nYou win!")

def paper_selected():
    comp = get_computer_choice()
    if comp == "Rock":
        showinfo(title="Result", message=f"Your choice: Paper\nComp choice: Rock\nYou win!")
    elif comp == "Paper":
        showinfo(title="Result", message=f"Your choice: Paper\nComp choice: Paper\nNobody wins")
    else:
        showinfo(title="Result", message=f"Your choice: Paper\nComp choice: Scissor\nYou lose!")

def scissor_selected():
    comp = get_computer_choice()
    if comp == "Rock":
        showinfo(title="Result", message=f"Your choice: Scissor\nComp choice: Rock\nYou lose!")
    elif comp == "Paper":
        showinfo(title="Result", message=f"Your choice: Scissor\nComp choice: Paper\nYou win!")
    else:
        showinfo(title="Result", message=f"Your choice: Scissor\nComp choice: Scissor\nNobody wins")

# Heading
lb = Label(window, text="GAME", font=("Bauhaus 93", 30), bg="white", fg="navy")
lb.place(x=100, y=20, height=40, width=100)

# Subheading
lb1 = Label(window, text="Rock Paper Scissor", font=("Bauhaus 93", 20), bg="white", fg="navy")
lb1.place(x=30, y=80, height=30, width=240)

# Instruction
lb2 = Label(window, text="Choose one", font=("Bauhaus 93", 15), bg="white", fg="navy")
lb2.place(x=30, y=130, height=20, width=110)

# Buttons
btn_rock = Button(window, text="Rock", font=("Bauhaus 93", 15), bg="white", fg="navy", cursor="hand2", command=rock_selected)
btn_rock.place(x=9, y=170, height=30, width=90)

btn_paper = Button(window, text="Paper", font=("Bauhaus 93", 15), bg="white", fg="navy", cursor="hand2", command=paper_selected)
btn_paper.place(x=105, y=170, height=30, width=90)

btn_scissor = Button(window, text="Scissor", font=("Bauhaus 93", 15), bg="white", fg="navy", cursor="hand2", command=scissor_selected)
btn_scissor.place(x=201, y=170, height=30, width=90)

# Start GUI
window.mainloop()
