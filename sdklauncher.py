#!/usr/bin/env python

from tkinter import *
import os
import subprocess
print("go")

pal_lite = "#4b5743"
pal_dark = "#3c4534"
pal_text = "white"
pal_stxt = "#c4b74e"
pal_hovr = "#1f221b"
pal_hovy = "#95892d"

pal_tes1 = "red"
pal_tes2 = "green"
pal_tes3 = "blue"
pal_tes4 = "yellow"

class Scrollable(Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame,
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        scrollbar = Scrollbar(frame, width=width, troughcolor=pal_lite, bg=pal_lite, activebackground=pal_lite)
        scrollbar.pack(side=RIGHT, fill=Y, expand=False)

        self.canvas = Canvas(frame, yscrollcommand=scrollbar.set, relief=SUNKEN, bd=0, bg=pal_dark, highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True, pady=0, ipady=0)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        Frame.__init__(self, frame, bg=pal_dark, pady=0)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=NW)


    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        scroll_scrollregion = list(self.canvas.bbox(self.windows_item))
        scroll_scrollregion[3] = scroll_scrollregion[3] + 100
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))
        print(self.canvas.bbox(self.windows_item))

root = Tk()
# root.wm_attributes('-type', 'splash')
# buffer_root_geometry = root.geometry()
# root.wm_overrideredirect(True) # This works, but it glitches absolutely everything on-screen.
# root.geometry(buffer_root_geometry)

image_close = PhotoImage(file = "./img/cls.png")
image_mini = PhotoImage(file = "./img/min.png")
image_height = PhotoImage(file = "./img/height.png")

ico_hammer = PhotoImage(file = "./img/i_hammer.png")
ico_model = PhotoImage(file = "./img/i_model.png")
ico_face = PhotoImage(file = "./img/i_face.png")
ico_itemtest = PhotoImage(file = "./img/i_itemtest.png")
ico_docu = PhotoImage(file = "./img/i_docu.png")
ico_createmod = PhotoImage(file = "./img/i_createmod.png")
ico_refresh = PhotoImage(file = "./img/i_refresh.png")
ico_resetedit = PhotoImage(file = "./img/i_resetedit.png")
ico_links = PhotoImage(file = "./img/i_links.png")


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



# Here we go.

root.geometry('350x476+350+200')
root.configure(bg=pal_lite, relief=RAISED, bd=1)

# Base layout
titlebar = Frame(root, bg=pal_lite)
titlebar.bind('<B1-Motion>', move_window)
titlebar.bind('<Button-1>', get_pos)

application = Frame(root, bg=pal_dark, relief=SUNKEN, bd=1)
application_s = Scrollable(application)

# Titlebar definitions
titlebar_label = Label(titlebar, text="     Source SDK Launcher", bg=pal_lite, fg=pal_text, font=("Tahoma", 10), justify="left")
# titlebar_close_fm = Frame(titlebar, width=18, height=18, relief=RAISED, bd=1, bg=pal_lite)
titlebar_mini = Button(titlebar, width = 14, height = 14, image = image_mini, bd=1, highlightthickness=0, takefocus=False, relief=RAISED, bg=pal_lite, activebackground=pal_lite)
titlebar_close = Button(titlebar, width = 14, height = 14, image = image_close, bd=1, highlightthickness=0, takefocus=False, relief=RAISED, bg=pal_lite, activebackground=pal_lite, command=root.destroy)

# Application definitions
application_m_apps = Label(application_s, text="ᴀᴘᴘʟɪᴄᴀᴛɪᴏɴs", bg=pal_dark, fg=pal_stxt, font=("Tahoma", 10), anchor="w")

application_s_apps = Frame(application_s, bg = pal_hovr)

app_hammer = Button(application_s, text="Hammer Editor", image=ico_hammer, compound="left", height=10, bg=pal_dark, fg=pal_text, font=("Tahoma", 10), anchor="w", bd=0, highlightthickness=0, activebackground=pal_hovy, activeforeground=pal_text)
app_model = Button(application_s, text="Model Viewer", image=ico_model, compound="left", height=10, bg=pal_dark, fg=pal_text, font=("Tahoma", 10), anchor="w", bd=0, highlightthickness=0, activebackground=pal_hovy, activeforeground=pal_text)
app_facer = Button(application_s, text="Face Poser", image=ico_face, compound="left", height=10, bg=pal_dark, fg=pal_text, font=("Tahoma", 10), anchor="w", bd=0, highlightthickness=0, activebackground=pal_hovy, activeforeground=pal_text)

application_m_mods = Label(application_s, text="sᴏᴜʀᴄᴇᴍᴏᴅs", bg=pal_dark, fg=pal_stxt, font=("Tahoma", 10), anchor="w")

application_s_mods = Frame(application_s, bg = pal_hovr)

prog_sourcemods = os.listdir(os.environ['HOME'] + "/.steam/steam/steamapps/sourcemods/")
app_sourcemod_list = []

for mod in prog_sourcemods:
    app_sourcemod_list.append(Button(application_s, text=mod, image=ico_itemtest, compound="left", height=10, bg=pal_dark, fg=pal_text, font=("Tahoma", 10), anchor="w", bd=0, highlightthickness=0, activebackground=pal_hovy, activeforeground=pal_text))

# Game picker and settings menu

menu = Frame(root, bg=pal_lite)

# ---------------------------------------------

titlebar.grid(row=0, column=0, sticky=EW, padx=7, pady=5, ipadx=0)

application.grid(row=1, column=0, sticky=NSEW, padx=7, pady=0, ipadx=5, ipady=5)

menu.grid(row=2, column=0, sticky=NSEW, padx=7, pady=0, ipadx=0, ipady=10)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
titlebar.grid_columnconfigure(1, weight=1)

titlebar_label.grid(column=0, row=0, sticky=W)
# titlebar_close_fm.grid(column=1, row=0)
titlebar_mini.grid(column=1, row=0, sticky=E, pady=0, padx=1)
titlebar_close.grid(column=2, row=0, sticky=E, pady=0, padx=1)

# App packing below

application_m_apps.pack(fill=BOTH, padx=24, pady=2)

application_s_apps.pack(fill=BOTH, padx=8)

app_hammer.pack(fill=BOTH, padx=0, pady=0, ipadx=0, ipady=0)
app_model.pack(fill=BOTH, padx=0, pady=0, ipadx=0, ipady=0)
app_facer.pack(fill=BOTH, padx=0, pady=0, ipadx=0, ipady=0)

application_m_mods.pack(fill=BOTH, padx=24, pady=2)

application_s_mods.pack(fill=BOTH, padx=8)

for button in app_sourcemod_list:
    button.pack(fill=BOTH, padx=0, pady=0, ipadx=0, ipady=0)

# The end.

application_s.update()

# center_window(root)

root.mainloop()