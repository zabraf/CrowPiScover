from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk


class Main: 
    root = Tk() # Main form
    
    bgImage = Image.open(r"images/CrowPiBG.jpg") # Image background
    render = ImageTk.PhotoImage(bgImage) # Create a render of the background image

    lblImage = Label(root, image=render, height=1000) # Create a label on the root form, the picture and the height
    lblImage.place(x=-1, y=-1) # Change the position of the label

    label = Label(root, text="Hello World")
    label.pack()
    componentImage = ImageTk.PhotoImage(file = r"images/CrowPiBG.jpg")
    Button(root, borderwidth=0, image=componentImage).place(x=100, y=100)
    Button(root, text ='Quit', command=root.destroy, borderwidth=0).place(x=1500, y=1000)
    
    root.geometry("1920x1000")
    root.mainloop() # Load the form 
