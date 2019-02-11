import tkinter as tk
import os
import time
from tkinter import *
from tkinter import scrolledtext, ttk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       lbl = Label(self, text=" Routing Table", font=("Arial Bold", 30))
       lbl.place(relx=0.5, rely=0.15, anchor=CENTER)
       pgBar = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode="determinate")
       pgBar.place(x=250, y=80)
       txt = scrolledtext.ScrolledText(self, width=90, height=10)
       txt.place(relx=0.5, rely=0.5, anchor=CENTER)
       btnStart = Button(self, text="Start Scan", font=("Arial Bold", 20), bg="orange", fg="black")
       btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
       btnBack = Button(self, text="Back", font=("Arial Bold", 20), bg="orange", fg="black")
       btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       lbl = Label(self, text=" Network Scanner", font=("Arial Bold", 30))
       lbl.place(relx=0.5, rely=0.15, anchor=CENTER)
       pgBar = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode="determinate")
       pgBar.place(x=250, y=80)
       txt = scrolledtext.ScrolledText(self, width=90, height=10)
       txt.place(relx=0.5, rely=0.5, anchor=CENTER)
       btnStart = Button(self, text="Start Scan", font=("Arial Bold", 20), bg="orange", fg="black")
       btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
       btnBack = Button(self, text="Back", font=("Arial Bold", 20), bg="orange", fg="black")
       btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       lbl = Label(self, text=" Port Scanner", font=("Arial Bold", 30))
       lbl.place(relx=0.5, rely=0.15, anchor=CENTER)
       pgBar = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode="determinate")
       pgBar.place(x=250, y=80)
       txt = scrolledtext.ScrolledText(self, width=90, height=10)
       txt.place(relx=0.5, rely=0.5, anchor=CENTER)
       btnStart = Button(self, text="Start Scan", font=("Arial Bold", 20), bg="orange", fg="black")
       btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
       btnBack = Button(self, text="Back", font=("Arial Bold", 20), bg="orange", fg="black")
       btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x400")
    root.mainloop()
