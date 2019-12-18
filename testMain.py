from tkinter import * 
import testClass

class Main: 
    def DisplayButton(window, o):
        label = Label(window, text="Hello World")
        label.pack()
        def Callback():
            o.Display()
        Canvas(window, width=1024, height=600, bg='ivory').pack(side=TOP, padx=5, pady=5)
        Button(window, text ='Display', command=Callback).pack(side=LEFT, padx=42, pady=5)
        Button(window, text ='Bouton 2').pack(side=RIGHT, padx=5, pady=5)
        return window
    
    window = Tk()
    o = testClass.TestObject()
    window = DisplayButton(window, o)
    # window.attributes("-fullscreen", True) 
    window.mainloop()
    

  
