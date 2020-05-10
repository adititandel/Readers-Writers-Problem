import tkinter as tk
from tkinter import *

import rwp_func
import rwp_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 200)
        self.master.maxsize(500, 500)
        rwp_func.center_window(self, 580, 300)
        self.master.title("OUTPUT WINDOW")

        self.master.protocol("WM_DELETE_WINDOW", lambda: rwp_func.ask_quit(self))

        rwp_gui.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
