#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def ExecuteExemple():
    #Do your shit here
    messagebox.showinfo("BipBip", "I'm a sheep")

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("300x300+400+100")

lblVeryLowLight = Label(window, bg="red", width="2", height="2")
lblLowLight = Label(window, bg="red", width="2", height="4")
lblNormalLight = Label(window, bg="red", width="2", height="6")
lblHighLight = Label(window, bg="red", width="2", height="8")
lblVeryHighLight = Label(window, bg="red", width="2", height="10")

lblVeryLowLight.place(x=80, y=50)
lblLowLight.place(x=110, y=50)
lblNormalLight.place(x=140, y=50)
lblHighLight.place(x=170, y=50)
lblVeryHighLight.place(x=200, y=50)

window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

