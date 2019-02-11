import os
import time
from tkinter import *
from tkinter import scrolledtext, ttk

window = Tk()
window.title("Network Management TNP")
window.geometry('800x400')

nb = ttk.Notebook(window)
nb.place(x=10, y=10)
page1 = ttk.Frame(nb)
nb.add(page1, text='Network Scanner')
lbl = Label(window, text=" Network Scanner", font=("Arial Bold", 30))
lbl.place(relx=0.5, rely=0.15, anchor=CENTER)
nb.pack(expand=1, fill="both")


page2 = ttk.Frame(nb)
nb.add(page2, text='Next Scanner')
lbl = Label(window, text=" Page 2", font=("Arial Bold", 30))
lbl.place(relx=0.5, rely=0.15, anchor=CENTER)
nb.pack(expand=1, fill="both")



pgBar = ttk.Progressbar(window, orient = HORIZONTAL, length=300, mode = "determinate")
pgBar.place(x=250, y=80)


txt = scrolledtext.ScrolledText(window, width=90, height=10)
txt.place(relx=0.5, rely=0.5, anchor=CENTER)


def incrementBar():
    for x in range(1, 10):
        increment = 4 + x
        pgBar.step(increment)


def netcommand():
    f = os.popen('netstat -y')
    for line in f:
        line = line.strip()
        if line:
            txt.insert("end", line + "\n")
    txt.bind("<Return>", clicked)
    f.close()


def clicked():
    netcommand()


btnStart = Button(window, text="Start Scan", font=("Arial Bold", 20), bg="orange", fg="black", command=clicked)
btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
btnBack = Button(window, text="Back", font=("Arial Bold", 20), bg="orange", fg="black", command=clicked)
btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)

window.mainloop()


