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
        Button(window, text ='Display', command=Callback, borderwidth=0).place(x=100, y=100)
        Button(window, text ='Quit', command=window.destroy, borderwidth=0).place(x=1500, y=1000)
        return window
    
    root = Tk()
    load = Image.open("city_sun_sunset_143693_1920x1080.jpg")
    render = ImageTk.PhotoImage(load)

    lblImage = Label(root, image=render, height=50%)

    lblImage.image = render
    lblImage.place(x=-1, y=-1)
     
    o = testClass.TestObject()
    root = DisplayButton(root, o)
    root.attributes("-fullscreen", True)
    root.mainloop()
    

  
