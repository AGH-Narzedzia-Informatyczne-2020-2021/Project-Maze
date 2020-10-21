from tkinter import *
from PIL import Image,ImageTk


class Quiz:
    def __init__(self, master, parent):
        self.master = master
        self.master.title("Quiz")
        self.master.geometry("500x450")
        self.master.iconbitmap(r'Images\earth_icon.ico')
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.parent = parent

    def close_windows(self):
        self.master.destroy()
