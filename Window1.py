from tkinter import *


class Window1:
    def __init__(self, master, parent):
        self.master = master
        self.master.title("Window2")
        self.master.geometry("300x200")
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.parent = parent
        #sffdfdfdfdfdf

    def close_windows(self):
        self.master.destroy()
