from tkinter import *
window=Tk()
# widgets are added here
# to change title
window.title("Info Tech")
#to transparent the window
window.attributes('-alpha',0.5)# value is between 0 and 1
# to set back ground colour
window.config(bg="blue")
# window size and location
width=400
height=400
#window.geometry("400x500") # width x height
#to find system height and width
sys_width = window.winfo_screenwidth()
sys_height = window.winfo_screenheight()
# to find center position
c_x=int(sys_width/2 - width/2)
c_y=int(sys_height/2 - height/2)
window.geometry(f"{width}x{height}+{c_x}+{c_y}")
#to stop resizable
window.resizable(False,False)
window.mainloop()