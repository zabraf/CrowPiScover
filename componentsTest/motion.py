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
window.geometry("460x200+400+100")

lblTitle = Label(window, text="Mouvement(Rouge = aucun, Vert = mouvement) : ", font=("Courier", 12))
lblMovement = Label(window, bg="Red", width="54", height=5)

lblTitle.place(x=10, y=50)
lblMovement.place(x=10, y=70)

window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

