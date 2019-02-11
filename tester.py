import tkinter as tk
import os
from tkinter import *
from tkinter import scrolledtext, ttk
from tkinter import ttk
import threading
import queue
import time


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.queue = queue.Queue()
        self.title("Network Management TNP")
        self.scrolledtext = scrolledtext.ScrolledText(self, width=80, height=20)
        self.progressbar = ttk.Progressbar(self, orient='horizontal', length=400, mode='determinate')
        self.button = tk.Button(self, text="Start", command=self.spawnthread)
        self.scrolledtext.pack(padx=10, pady=10)
        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)

    def spawnthread(self):
        self.button.config(state="disabled")
        self.thread = ThreadedClient(self.queue)
        self.thread.start()
        self.periodiccall()

    def periodiccall(self):
        self.checkqueue()
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.button.config(state="active")

    def checkqueue(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.scrolledtext.insert('end', msg)
                self.progressbar.step(25)
            except queue.Empty:
                pass


class ThreadedClient(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for x in range(1, 5):
            time.sleep(2)
            msg = "Function %s finished..." % x
            self.queue.put(msg)


if __name__ == "__main__":
    app = App()
    app.mainloop()
