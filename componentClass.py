from tkinter import *
from PIL import Image, ImageTk

class Component:
    def Display(self):
        componentWindow = Toplevel()
        Button(componentWindow, text ='Bouton 1').pack(side=LEFT, padx=42, pady=5)
        Button(componentWindow, text ='Go Back', command=componentWindow.destroy).pack(side=RIGHT, padx=5, pady=5)

        bgImage = ImageTk.PhotoImage(Image.open("images/CrowPiDessin.jpg")) # Create a render of the background image

        lblImage = Label(componentWindow, image=bgImage) # Create a label on the root form, the picture and the height
        lblImage.place(x=-1, y=-1) # Change the position of the label

        componentWindow.attributes("-fullscreen", True) 
        componentWindow.mainloop()
