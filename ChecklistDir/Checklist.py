from tkinter import *
from ChecklistDir import CreateButton
from ChecklistDir import DropDown
from ChecklistDir import config
import os


class Checklist:

    def __init__(self, master, parent):
        self.master = master
        self.master.title("Checklisty")
        self.master.geometry("500x500")

        # self.frame = Frame(self.master)
        # self.frame.pack()
        # self.parent = parent

        # proba rozwijanego menu
        # def run():
        #  myLabel = Label(self.master, text=variable.get()).grid(row=2, column=0)

        # wyswietlanie rozwijanego menu
        def refresh():
            if hasattr(self, "menu"):
                self.menu.destroy()
            if config.ChecklistNames:
                global variable
                variable = StringVar(master)
                variable.set(config.ChecklistNames[0])

                self.menu = OptionMenu(self.master, variable, *config.ChecklistNames)
                self.menu.grid(row=5, column=1)

        # deklaracja przycisków
        self.MakeChecklist = Button(self.master, text="Utworz nowa checklistę", bg = "deep sky blue",padx=30, pady=50,
                                    command=self.OpenMakeChecklist)
        self.DropDown = Button(self.master, text="Zatwierdz wybór checklisty", bg="orange" , padx=10, pady=50,
                               command=self.OpenSelectedChecklist)  # command=run) command=self.new_window2
        self.Refresh = Button(self.master, text="Odswież checklistę", bg="green yellow" ,padx=30, pady=50, command=refresh)
        self.quitButton = Button(self.master, text='Wyjście', padx=80, pady=10, bg="DarkRed",
                                 command=self.close_windows)
        self.deleteChecklistButton = Button(self.master, text='Usuń wybraną Checklistę', bg="#CCFF00", padx=30, pady=50, command=self.deleteChecklist)


        # tworzenie rozwijanego menu
        if config.ChecklistNames:
            global variable
            variable = StringVar(master)
            variable.set(config.ChecklistNames[0])

            self.menu = OptionMenu(self.master, variable, *config.ChecklistNames)
            self.menu.grid(row=5, column=1)

        # ustawienie w oknie
        self.DropDown.grid(row=0, column=1, padx=5, pady=10, columnspan=1, sticky=W)
        self.MakeChecklist.grid(row=0, column=0, padx=5, pady=10, columnspan=1)
        self.quitButton.grid(row=2, column=0, padx=10, pady=10)
        self.Refresh.grid(row=1, column=1, padx=10, pady=10)
        self.deleteChecklistButton.grid(row=1, column=0, padx=5, pady=10, columnspan=1)

    def close_windows(self):
        self.master.destroy()

    def deleteChecklist(self):
        for i in range(len(config.ChecklistNames)):
            if str(config.ChecklistNames[i]) == variable.get():
                checklistChoosen = variable.get()

        config.ChecklistNames.remove(checklistChoosen)
        config.n -= 1
        os.remove("ChecklistDir/lists/" + checklistChoosen)

    # wyświetlanie w nowym oknie onka od tworzenia checklisty
    def OpenMakeChecklist(self):
        new_window = Toplevel(self.master)
        CreateButton.CreateButton(new_window, self)

    # wyświetlanie wybranej checklisty
    def OpenSelectedChecklist(self):
        for i in range(len(config.ChecklistNames)):
            if str(config.ChecklistNames[i]) == variable.get():
                config.name = i
        new_window = Toplevel(self.master)
        DropDown.DropDown(new_window, self)
