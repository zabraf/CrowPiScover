from tkinter import *

class TestObject:
    def Display(self):
        newwindow = Tk()
        label = Label(newwindow, text="Hello World")
        label.pack()
        Canvas(newwindow, width=1024, height=600, bg='ivory').pack(side=TOP, padx=5, pady=5)
        Button(newwindow, text ='Bouton 1').pack(side=LEFT, padx=42, pady=5)
        Button(newwindow, text ='Go Back', command=newwindow.destroy).pack(side=RIGHT, padx=5, pady=5)
        newwindow.attributes("-fullscreen", True) 
        newwindow.mainloop()
