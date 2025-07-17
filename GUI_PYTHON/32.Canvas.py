# Canvas()
from tkinter import *
window = Tk()

canvas_1 = Canvas(window,bg = "Red")
canvas_1.place(x=0,y=0,height=700,width=700)
    #   x0,y0, x1,y1
coord_1 = 0,0,700,700
coord_2= 700,0,0,700

#create_line()
line=canvas_1.create_line(coord_1,fill="blue")
line=canvas_1.create_line(coord_2,fill="blue")

#create_arc()
#arc = canvas_1.create_arc(coord_1,start=0,extent=270,fill="Blue")
arc2 = canvas_1.create_arc(coord_1,start=0,extent=359,fill="Blue")
window.mainloop()