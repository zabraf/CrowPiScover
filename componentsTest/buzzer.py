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
window.geometry("300x100+400+100")
Button(window, command= lambda: ExecuteExemple(), bg="green", activebackground="darkgreen", width="10").place(x=100, y=35)
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

