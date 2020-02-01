import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
parent = tk.Tk()
parent.title("Progressbar")
parent.geometry('200x50')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(parent, length=220, style='black.Horizontal.TProgressbar')
bar['value'] = 20
bar.grid(column=0, row=0)
parent.mainloop()
