from tkinter import *


class CalculatorWindow:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Window1")
        self.master.geometry("550x200")
        self.frame = Frame(self.master)

        self.num1entry = Entry(self.master)
        self.num1entry.pack(side=LEFT)

        Label(self.master, text="=").pack(side=LEFT)

        self.num2entry = Entry(self.master)
        self.num2entry.pack(side=LEFT)

        self.calculate_button = Button(self.master, text="=")
        self.calculate_button.bind("<Button-1>", self.get_sum)
        self.calculate_button.pack(side=LEFT)

        self.sum_entry = Entry(self.master)
        self.sum_entry.pack(side=LEFT)
        self.quitButton = Button(self.frame, text='Quit')
        self.quitButton.bind("<Button-1>", self.close_windows)
        self.quitButton.pack(side=LEFT)
        self.frame.pack()

    def close_windows(self, event):
        self.master.destroy()

    def get_sum(self, event):
        num1 = int(self.num1entry.get())
        num2 = int(self.num2entry.get())
        self.sum_entry.insert(0, num1 + num2)
