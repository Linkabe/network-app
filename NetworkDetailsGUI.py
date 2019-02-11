import os
import time
from tkinter import *
from tkinter import scrolledtext, ttk
from tkinter import *


def raise_frame(frame):
    frame.tkraise()

window = Tk()
window.title("Network Management TNP")
window.geometry('800x400')

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)
f4 = Frame(window)

def wirelessinfo():
    f = os.popen('netsh wlan show interfaces')
    for line in f:
        line = line.strip()
        if line:
            txt4.insert("end", line + "\n")
        txt4.bind("<Return>", wirelessinfo)
    f.close()


def routingtable():
    f = os.popen('netstat -r')
    for line in f:
        line = line.strip()
        if line:
            txt3.insert("end", line + "\n")
        txt3.bind("<Return>", routingtable)
    f.close()


def netscanner():
    f = os.popen('arp -a')
    for line in f:
        line = line.strip()
        if line:
            txt2.insert("end", line + "\n")
        txt2.bind("<Return>", netscanner)
    f.close()

def netstatus():
    f = os.popen('netstat -y')
    for line in f:
        line = line.strip()
        if line:
            txt1.insert("end", line + "\n")
        txt1.bind("<Return>", netstatus)
    f.close()


for frame in (f1, f2, f3, f4):
    frame.place(width=800, height=400)


pgBar = ttk.Progressbar(f1, orient = HORIZONTAL, length=300, mode = "determinate")
pgBar.place(x=250, y=80)
txt1 = scrolledtext.ScrolledText(f1, width=90, height=10)
txt1.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(f1, text='Network Scanner', command=lambda:raise_frame(f2)).place(relx=0.0, rely=0.0)
Label(f1, text=" Network Status", font=("Arial Bold", 30)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnStart = Button(f1, text="Get Status", font=("Arial Bold", 20), bg="Green", fg="black", command=netstatus)
btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
btnBack = Button(f1, text="Back", font=("Arial Bold", 20), bg="Red", fg="black", command=netstatus)
btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)


pgBar = ttk.Progressbar(f2, orient = HORIZONTAL, length=300, mode = "determinate")
pgBar.place(x=250, y=80)
txt2 = scrolledtext.ScrolledText(f2, width=90, height=10)
txt2.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(f2, text='Routing Tables', command=lambda:raise_frame(f3)).place(relx=0.1, rely=0.0)
Label(f2, text=" Network Scanner", font=("Arial Bold", 30)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnStart = Button(f2, text="Start Scan", font=("Arial Bold", 20), bg="Green", fg="black", command=netscanner)
btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
btnBack = Button(f2, text="Back", font=("Arial Bold", 20), bg="Red", fg="black", command=netstatus)
btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)

pgBar = ttk.Progressbar(f3, orient = HORIZONTAL, length=300, mode = "determinate")
pgBar.place(x=250, y=80)
txt3 = scrolledtext.ScrolledText(f3, width=90, height=10)
txt3.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(f3, text='Wireless Information', command=lambda:raise_frame(f4)).place(relx=0.2, rely=0.0)
Label(f3, text=" Routing Tables", font=("Arial Bold", 30)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnStart = Button(f3, text="Routing TBL", font=("Arial Bold", 20), bg="Green", fg="black", command=routingtable)
btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
btnBack = Button(f3, text="Back", font=("Arial Bold", 20), bg="Red", fg="black", command=netstatus)
btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)

pgBar = ttk.Progressbar(f4, orient = HORIZONTAL, length=300, mode = "determinate")
pgBar.place(x=250, y=80)
txt4 = scrolledtext.ScrolledText(f4, width=90, height=10)
txt4.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(f4, text='Network Status', command=lambda:raise_frame(f1)).place(relx=0.3, rely=0.0)
Label(f4, text="Wireless Info", font=("Arial Bold", 30)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnStart = Button(f4, text="Get Info", font=("Arial Bold", 20), bg="Green", fg="black", command=wirelessinfo)
btnStart.place(relx=0.2, rely=0.8, anchor=CENTER)
btnBack = Button(f4, text="Back", font=("Arial Bold", 20), bg="Red", fg="black", command=netstatus)
btnBack.place(relx=0.8, rely=0.8, anchor=CENTER)

raise_frame(f1)
window.mainloop()

