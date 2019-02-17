from tkinter import *

screen = Tk()
text = Text(screen, height = 2, width = 30)
text.pack()
text.insert(END, '-')

def apress():
    text.insert(END, 'a')

btn = Button(screen, text = 'a', width = 5, command = apress)
btn.pack()

mainloop()
