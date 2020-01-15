from tkinter import *
from tkinter import messagebox
import testClass
from PIL import Image, ImageTk
from pynput import mouse

class Main: 
    def DisplayButton(window, o):
        label = Label(window, text="Hello World")
        label.pack()
        def Callback():
            o.Display()
        #Canvas(window, width=1024, height=600, bg='red').pack(side=TOP, padx=5, pady=5)
        Button(window, text ='Display', command=Callback, borderwidth=0).place(x=100, y=100)
        Button(window, text ='Quit', command=window.destroy, borderwidth=0).place(x=1500, y=1000)
        return window
    
    def OnClick(x, y, button, pressed):
        messagebox.showinfo("title", "{0}{1}".format('Pressed' if pressed else 'Released', (x,y))) 
    

    root = Tk() # Main form
    bgImage = Image.open("city_sun_sunset_143693_1920x1080.jpg") # Image background
    render = ImageTk.PhotoImage(bgImage) # Create a render of the background image

    listener = mouse.Listener(
        on_click=OnClick
    )
    listener.start()

    lblImage = Label(root, image=render, height=1000)

    lblImage.image = render
    lblImage.place(x=-1, y=-1)

    o = testClass.TestObject()
    root = DisplayButton(root, o)
    root.attributes("-fullscreen", True)
    root.mainloop()
    

  
