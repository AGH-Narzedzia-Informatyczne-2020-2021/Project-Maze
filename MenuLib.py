from tkinter import *
import CalculatorLib


class Menu:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        # deklaracja przyciskow do programow
        self.program1 = Button(self.frame, text="program 1", padx=40, pady=50, command=self.new_window1())
        program2 = Button(self.master, text="program 2", padx=40, pady=50)
        program3 = Button(self.master, text="program 3", padx=40, pady=50)
        program4 = Button(self.master, text="program 4", padx=40, pady=50)

        # umiejscowienie w main
        self.program1.grid(row=0, column=0, padx=50, pady=50)
        program2.grid(row=0, column=1, padx=50, pady=50)
        program3.grid(row=1, column=0, padx=50, pady=50)
        program4.grid(row=1, column=1, padx=50, pady=50)

    def new_window1(self):
        new_window = Toplevel(self.master)
        CalculatorLib.CalculatorWindow(new_window)

    def new_window2(self):
        new_window = Toplevel(self.master)
        Window2(new_window, self)

    def new_window3(self):
        new_window = Toplevel(self.master)
        Window3(new_window, self)
