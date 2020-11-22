from tkinter import *
from ChecklistDir import CreateButton
from ChecklistDir import DropDown



class Checklist:

    def __init__(self, master, parent):
        self.master = master
        self.master.title("Checklisty")
        self.master.geometry("500x500")
        #self.frame = Frame(self.master)
        #self.frame.pack()
        #self.parent = parent



        #deklaracja przycisków
        self.MakeChecklist = Button(self.master, text="Utworz nowa Checkliste", padx=30, pady=50, command=self.new_window1)
        self.DropDown = Button(self.master, text="Tu będzie wybor", padx=10, pady=50, command=self.new_window2)
        self.quitButton = Button(self.master, text='Wyjście', padx=80, pady= 10,  command=self.close_windows)

        #ustawienie w oknie
        self.DropDown.grid(row=0, column=2,  padx=5, pady=10, columnspan=1, sticky= W )
        self.MakeChecklist.grid(row=0, column=0, padx=5, pady=10, columnspan=1)
        self.quitButton.grid(row=1, column=0, padx=10, pady=10)

    def close_windows(self):
        self.master.destroy()

    #wyświetlanie w nowym oknie
    def new_window1(self):
        new_window = Toplevel(self.master)
        CreateButton.CreateButton(new_window, self)

    def new_window2(self):
        new_window = Toplevel(self.master)
        DropDown.DropDown(new_window, self)

        #komentrz naprawiający