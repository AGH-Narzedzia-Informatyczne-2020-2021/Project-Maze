from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Window1")
        self.master.geometry("550x200")
        self.frame = Frame(self.master)

        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=0)

        self.calculate = Button(self.master, text="=", command=self.test)
        self.calculate.grid(row=0, column=1, rowspan=2, columnspan=2, sticky=N+S)

        self.result = Entry(self.master, text="0")
        self.result.grid(row=1, column=0)

        self.quitButton = Button(self.master, text='Zamknij', command=self.close_windows)
        self.quitButton.grid(row=0, column=3, rowspan=2, columnspan=2, sticky=N + S)

    def test(self):
        self.result.insert(0, self.entry.get())

    def close_windows(self):
        self.master.destroy()

