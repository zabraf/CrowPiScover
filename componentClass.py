from tkinter import *

class Component:
    def Display(self):
        componentWindow = Tk()
        label = Label(componentWindow, text="Hello World")
        label.pack()
        Canvas(componentWindow, width=1024, height=600, bg='ivory').pack(side=TOP, padx=5, pady=5)
        Button(componentWindow, text ='Bouton 1').pack(side=LEFT, padx=42, pady=5)
        Button(componentWindow, text ='Go Back', command=componentWindow.destroy).pack(side=RIGHT, padx=5, pady=5)
        componentWindow.attributes("-fullscreen", True) 
        componentWindow.mainloop()
