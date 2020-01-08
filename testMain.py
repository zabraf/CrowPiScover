from tkinter import * 
import testClass
from PIL import Image, ImageTk


class Main: 
    def DisplayButton(window, o):
        label = Label(window, text="Hello World")
        label.pack()
        def Callback():
            o.Display()
       # Canvas(window, width=1024, height=600, bg='red').pack(side=TOP, padx=5, pady=5)
        Button(window, text ='Display', command=Callback).pack(side=LEFT, padx=42, pady=5)
        Button(window, text ='Quit', command=window.destroy).pack(side=RIGHT, padx=5, pady=5)
        return window
    
    root = Tk()
    load = Image.open("city_sun_sunset_143693_1920x1080.jpg")
    load.resize((2000,2000), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)

    lblImage = Label(root, image=render, height=1000)
    lblImage.image = render
    lblImage.place(x=0, y=0)
    lblImage.pack(side=TOP, expand = "no")
    
     
    o = testClass.TestObject()
    root = DisplayButton(root, o)
    root.attributes("-fullscreen", True) 
    root.mainloop()
    

  
