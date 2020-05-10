import tkinter as tk
from tkinter import *

import rwp_func


def load_gui(self):
    self.lbl_reader = tk.Label(self.master, text='Readers Writers Problem', font=("Helvetica", 30))
    self.lbl_reader.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky=N + W)
    self.btn_execute = tk.Button(self.master, width=10, height=2, text='EXECUTE',
                                 command=lambda: rwp_func.onExecute())
    self.btn_execute.grid(row=2, column=0, padx=(10, 0), pady=(10, 10), sticky=W)
