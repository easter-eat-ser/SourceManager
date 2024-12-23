#!/usr/bin/env python

import os
from time import sleep
from tkinter import *
from tkinter.ttk import *
import PIL.Image
import srctools

try:
    import ttkthemes
except:
    ttkthemes=None



root = Tk()

root.geometry("640x1080")

if ttkthemes:
    style = ttkthemes.ThemedStyle()
    style.theme_use("arc")
else:
    style = Style()
    print("Install ttkthemes package for optional theming")

style.configure('TFrame')

style.configure('Border.TFrame', borderwidth=1)

def int_is_not_power(n):
    return not ((n != 0) and (n & (n-1) == 0))

def png_to_vtf(path_png, path_vtf):
    file_png = PIL.Image.open(path_png)
    print(file_png.size)


    if (int_is_not_power(file_png.size[0]) or int_is_not_power(file_png.size[1])):
        return 1

    file_vtf = srctools.VTF(file_png.size[0], file_png.size[1])
    file_vtf.get().copy_from(file_png.tobytes())
    file_vtf.save(open(path_vtf, "wb"))
    return 0

def treeview_append_filesystem(tree, directory):
    tree.delete(*tree.get_children())
    # tree.insert("Location", "end", "Identifier", text="Folder name") Example
    for root, dirs, files in sorted(os.walk(directory)):
        if (os.path.basename(root) != ""):
            tree.insert(os.path.dirname(root)[len(os.path.dirname(directory)):], "end", (root)[len(os.path.dirname(directory)):], text=os.path.basename(root))
        for file in sorted(files):
            if ((root)[len(os.path.dirname(directory)):] == "/"):
                tree.insert("", "end", text=file)
            else:
                tree.insert((root)[len(os.path.dirname(directory)):], "end", text=file)



main_path_select = Frame(root)
main_container = Frame(root)

path_entry = Entry(main_path_select, textvariable="texture_path")
path_select = Button(main_path_select, text="Load")

path_entry.setvar("texture_path", os.environ['HOME'] + "/.steam/steam/steamapps/sourcemods/")

container_treeview = Treeview(main_container)

container_panel = Frame(main_container, relief=SOLID, style="Border.TFrame")
container_filename = Label(container_panel, text="", anchor="w")
container_filetype = Label(container_panel, text="", anchor="w")
container_convert = Button(container_panel, text="Compile")

# ---------------------------------------------------

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

main_path_select.grid(column=0, row=0, sticky=EW)
main_container.grid(column=0, row=1, sticky=NSEW)

main_path_select.columnconfigure(0, weight=1)
path_select.grid(column=1, row=0)
path_entry.grid(column=0, row=0, sticky=EW)

main_container.rowconfigure(0, weight=1)
main_container.columnconfigure(0, weight=1, minsize=200)
main_container.columnconfigure(1, weight=1, minsize=100) # TODO: Change this later...
container_treeview.grid(column=0, row=0, sticky=NSEW)

container_panel.grid(column=1, row=0, sticky=NSEW, padx=5, pady=5)
container_filename.pack(fill=X, padx=8, pady=8)
container_filetype.pack(fill=X, padx=8, pady=8)
container_convert.pack(fill=X, padx=8, pady=8, side=BOTTOM)

#container_treeview.insert('', 'end', "cheese", text='Item 2')
#container_treeview.insert('cheese', 'end', "charles", text='Item 32')
#container_treeview.insert('charles', 'end', "chars", text='Item 432')

def treeview_update(*args):
    print("Update treeview")
    treeview_append_filesystem(container_treeview, path_entry.getvar("texture_path"))

def info_panel_update(event):
    tree = container_treeview
    try:
        item = tree.item(tree.selection()[0], "text")
        container_filename.configure(text=item)
        extension = item.split(".")[-1].lower()
        filetype = "Unknown"
        if (extension.lower() == item.lower()):
            filetype = ""
        else:
            match extension:
                case "vpk":
                    filetype = "Valve package"
                case "vtf":
                    filetype = "Valve texture file"
                case "vmt":
                    filetype = "Valve material"
                case "so":
                    filetype = "Code library"
                case "dll":
                    filetype = "Windows code library"
                case "exe":
                    filetype = "Windows executable"
                case "txt":
                    filetype = "Text file"
                case "cache":
                    filetype = "Cache file"
                case "dt":
                    filetype = "Voice ban list"
                case "tmp":
                    filetype = "Temporary data"
                case "wad":
                    filetype = "GoldSrc texture package"
                case "spr":
                    filetype = "GoldSrc sprite"
                case "lst":
                    filetype = "Map data list"
                case "mdl":
                    filetype = "Compiled model"
                case "qc":
                    filetype = "QLumpy compile script"
                case "smd":
                    filetype = "Source model data"
                case "tga":
                    filetype = "Targa image"
                case "wav":
                    filetype = "Lossless audio"
                case "mp4":
                    filetype = "MPEG-4 media"
                case "png":
                    filetype = "Lossless image"
                case "jpg":
                    filetype = "Lossy image"
                case "jpeg":
                    filetype = "Lossy image"
                case "bmp":
                    filetype = "Uncompressed image"
                case "bsp":
                    filetype = "Compiled Source map"
                case "vmf":
                    filetype = "Valve map file"
                case "log":
                    filetype = "Log file"
                case "cfg":
                    filetype = "Configuration file"
        container_filetype.configure(text=filetype)
    except:
        pass

def compile_selected():
    path = container_treeview
    print(path)

treeview_update()
path_select.configure(command=treeview_update)
container_convert.configure(command=compile_selected)
container_treeview.bind('<<TreeviewSelect>>', info_panel_update)
# container_treeview.grid_propagate(True) <<< same
#container_panel.grid_propagate(True) # <<< doing absolutely nothing

# png_to_vtf("/home/easter/Documents/SRLA.png", "/home/easter/Documents/SRLA.vtf") Testing the pngtovtf
# png_to_vtf("/home/easter/Documents/SRLR.png", "/home/easter/Documents/SRLR.vtf")

root.mainloop()