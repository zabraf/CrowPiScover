#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def ExecuteExemple(buttonName, lbl):
    #Do your shit here
    lbl.config(text = buttonName)
    
def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("300x300+400+100")

lblBtnName = Label(window, text="He", font=("courrier", 25))
lblBtnName.place(x=100, y=35)

# Replace by the crowPiButton
Button(window, command= lambda: ExecuteExemple("Boop", lblBtnName), text="ON/OFF").place(x=75, y=55)

window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

