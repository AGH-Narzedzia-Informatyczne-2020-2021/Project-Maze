from tkinter import *
from PIL import  Image,ImageTk
from CalculatorDir import Calculator
import Quiz
from ChecklistDir import Checklist


class Menu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x450")
        self.master.title("Menu")
        self.frame = Frame(self.master)
        self.master.iconbitmap(r'Images\cube_icon_.ico')

        #icon
        self.calculator_icon = ImageTk.PhotoImage(Image.open(r'Images\calculator-icon.png'))
        self.quiz_icon = ImageTk.PhotoImage(Image.open(r'Images\earth.png'))
        self.checklist_icon = ImageTk.PhotoImage(Image.open(r'Images\checklist.png'))
        self.exit_icon = ImageTk.PhotoImage(Image.open(r'Images\exit-icon.ico'))

        program1 = Button(self.master, image=self.calculator_icon, padx=40, pady=50, command=self.new_window1)
        program2 = Button(self.master, image=self.quiz_icon, padx=40, pady=50, command=self.new_window2)
        program3 = Button(self.master, image=self.checklist_icon, padx=40, pady=50, command=self.new_window3)
        program4 = Button(self.master, image=self.exit_icon, padx=40, pady=50, command=self.new_window4)

        program1.grid(row=0, column=0, padx=50, pady=50)
        program2.grid(row=0, column=1, padx=50, pady=50)
        program3.grid(row=1, column=0, padx=50, pady=50)
        program4.grid(row=1, column=1, padx=50, pady=50)

    def new_window1(self):
        new_window = Toplevel(self.master)
        Calculator.Calculator(new_window)

    def new_window2(self):
        new_window = Toplevel(self.master)
        Quiz.Quiz(new_window)

    def new_window3(self):
        new_window = Toplevel(self.master)
        Checklist.Checklist(new_window, self)

    def new_window4(self):
        self.master.destroy()
        #new_window = Toplevel(self.master)
       #Window3.Window3(new_window, self)  # not exist yet
