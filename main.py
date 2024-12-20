from tkinter import *
import os
import subprocess
print("go")



root = Tk()
# root.wm_attributes('-type', 'splash')
# buffer_root_geometry = root.geometry()
root.wm_overrideredirect(True) # I'll add a custom titlebar, eventually...
# root.geometry(buffer_root_geometry)

image_close = PhotoImage(file = "./img/cls.png")
image_mini = PhotoImage(file = "./img/min.png")

def get_pos(event):
    global xwin
    global ywin
    xwin = event.x + 6
    ywin = event.y + 6

#title bar drag functon.
def move_window(event):
    root.geometry(f"+{event.x_root - xwin}+{event.y_root - ywin}")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

pal_lite = "#4b5743"
pal_dark = "#3c4534"
pal_text = "white"
pal_stxt = "#c4b74e"

# Here we go.

root.geometry('350x500+350+200')
root.configure(bg=pal_lite, relief=RAISED, bd=1)

# Base layout
titlebar = Frame(root, bg=pal_lite)
titlebar.bind('<B1-Motion>', move_window)
titlebar.bind('<Button-1>', get_pos)
application = Frame(root, bg=pal_dark, relief=SUNKEN, bd=1)

# Titlebar definitions
titlebar_label = Label(titlebar, text="     Source SDK", bg=pal_lite, fg=pal_text, font=("Tahoma", 10), justify="left")
# titlebar_close_fm = Frame(titlebar, width=18, height=18, relief=RAISED, bd=1, bg=pal_lite)
titlebar_mini = Button(titlebar, width = 14, height = 14, image = image_mini, bd=1, highlightthickness=0, takefocus=False, relief=RAISED, bg=pal_lite)
titlebar_close = Button(titlebar, width = 14, height = 14, image = image_close, bd=1, highlightthickness=0, takefocus=False, relief=RAISED, bg=pal_lite)

# Application definitions
application_m_apps = Label(application, text="ᴀᴘᴘʟɪᴄᴀᴛɪᴏɴs", bg=pal_dark, fg=pal_stxt, font=("Tahoma", 10), justify="left")

titlebar.grid(row=0, column=0, sticky=EW, padx=7, pady=5, ipadx=0)
application.grid(row=1, column=0, sticky=NSEW, padx=7, pady=0, ipadx=5, ipady=5)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
titlebar.grid_columnconfigure(1, weight=1)

titlebar_label.grid(column=0, row=0, sticky=W)
# titlebar_close_fm.grid(column=1, row=0)
titlebar_mini.grid(column=1, row=0, sticky=E, pady=0, padx=1)
titlebar_close.grid(column=2, row=0, sticky=E, pady=0, padx=1)

application_m_apps.grid(column=2, row=0, sticky="w")

# The end.

# center_window(root)

root.mainloop()