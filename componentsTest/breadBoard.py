#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("300x300+400+100")
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

