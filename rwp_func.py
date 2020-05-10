import os
import threading as thread
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

global x  # Shared Data
x = 0
lock = thread.Lock()


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    a = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, a, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


def onExecute():
    window = tk.Tk()
    window.title('Execution Window')
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(window, width=50, height=20, yscrollcommand=scrollbar.set)

    def Reader():
        global x, Thread1, Thread2
        mylist.insert(END, 'Reader is reading')
        mylist.pack()
        lock.acquire()  # Acquire the lock before Reading (mutex approach)
        r = ('Shared Data:', x)
        mylist.insert(END, r)
        mylist.pack()
        lock.release()  # Release the lock after Reading
        mylist.insert(END, ' ')
        mylist.pack()

    def Writer():
        global x
        mylist.insert(END, 'Writer is writing')
        mylist.pack()
        lock.acquire()  # Acquire the lock before Writing
        x += 1  # Write on the shared memory
        mylist.insert(END, 'Writer is releasing the lock')
        mylist.pack()
        lock.release()  # Release the lock after Writing
        mylist.insert(END, ' ')
        mylist.pack()

    for i in range(0, 10):
        randomNumber = random.randint(0, 100)  # Generate a Random number between 0 to 100
        if randomNumber > 50:
            Thread1 = thread.Thread(target=Reader())
            Thread1.start()
        else:
            Thread2 = thread.Thread(target=Writer())
            Thread2.start()
    Thread1.join()
    Thread2.join()
    scrollbar.config(command=mylist.yview)
    window.mainloop()
