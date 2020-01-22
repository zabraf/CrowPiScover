from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import componentClass

class Main: 
    def DisplayButton(window, o):
        def Callback():
            o.Display()
        
        global componentImage
        componentImage = ImageTk.PhotoImage(file = r"RaspberryDessin.jpg")
        Button(window, command=Callback, borderwidth=0, image=componentImage).place(x=100, y=100)
        Button(window, text ='Quit', command=window.destroy, borderwidth=0).place(x=1500, y=1000)
        return window
    
    root = Tk() # Main form
    bgImage = Image.open("city_sun_sunset_143693_1920x1080.jpg") # Image background
    render = ImageTk.PhotoImage(bgImage) # Create a render of the background image

    lblImage = Label(root, image=render, height=1000) # Create a label on the root form, the picture and the height
    lblImage.place(x=-1, y=-1) # Change the position of the label
    
    o = componentClass.Component() # Intialize the function in another file
    root = DisplayButton(root, o) # Call the display button method

    root.attributes("-fullscreen", True) # Resize the form in fullscreen
    root.mainloop() # Load the form
    

 
