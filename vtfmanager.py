#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from srctools import *

root = Tk()

root.geometry("1280x720")

main_path_select = Frame(root, bg="red")
main_container = ttk.Frame(root)

path_entry = ttk.Entry(main_path_select, textvariable="texture_path")
path_select = ttk.Button(main_path_select, text="Pick...")

container_treeview = ttk.Treeview(main_container)

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

main_path_select.grid(column=0, row=0, sticky=EW)
main_container.grid(column=0, row=1, sticky=NSEW)

main_path_select.columnconfigure(0, weight=1)
path_select.grid(column=1, row=0)
path_entry.grid(column=0, row=0, sticky=EW)

main_container.rowconfigure(0, weight=1)
main_container.columnconfigure(0, weight=1) # TODO: Change this later...
container_treeview.grid(column=0, row=0, sticky=NSEW)

root.mainloop()