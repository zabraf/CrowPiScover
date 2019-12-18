from tkinter import * 

class Main:
    def DisplayButton(window):
        label = Label(window, text="Hello World")
        label.pack()
        Canvas(window, width=1024, height=600, bg='ivory').pack(side=TOP, padx=5, pady=5)
        Button(window, text ='Bouton 1').pack(side=LEFT, padx=42, pady=5)
        Button(window, text ='Bouton 2').pack(side=RIGHT, padx=5, pady=5)
        return window

    window = Tk() 
    window = DisplayButton(window)
    window.mainloop()



