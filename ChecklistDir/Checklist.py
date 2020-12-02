from tkinter import *
from ChecklistDir import CreateButton
from ChecklistDir import DropDown
from ChecklistDir import config





class Checklist:

    def __init__(self, master, parent):
        self.master = master
        self.master.title("Checklisty")
        self.master.geometry("500x500")
        #self.frame = Frame(self.master)
        #self.frame.pack()
        #self.parent = parent

      #proba rozwijanego menu
       # def run():
        #  myLabel = Label(self.master, text=variable.get()).grid(row=2, column=0)

        #wyswietlanie rozwijanego menu
        def refresh():
             if config.ChecklistNames:
                global  variable
                variable = StringVar(master)
                variable.set(config.ChecklistNames[0])

                self.menu = OptionMenu(self.master, variable, *config.ChecklistNames)
                self.menu.grid(row=5, column=1)

        #deklaracja przycisków
        self.MakeChecklist = Button(self.master, text="Utworz nowa checklistę", padx=30, pady=50, command=self.OpenMakeChecklist)
        self.DropDown = Button(self.master, text="Zatwierdz wybór checklisty", padx=10, pady=50,  command=self.OpenSelectedChecklist) #command=run) #xcommand=self.new_window2
        self.Refresh = Button(self.master, text="Odswież checklistę", padx=30, pady=50) #na razie zeby odswiezyc checkliste trzeba wyjsc z progrmau do menu
        self.quitButton = Button(self.master, text='Wyjście', padx=80, pady= 10, bg="DarkRed",  command=self.close_windows)

        #tworzenie rozwijanego menu
        refresh()


        #ustawienie w oknie
        self.DropDown.grid(row=0, column=1,  padx=5, pady=10, columnspan=1, sticky= W )
        self.MakeChecklist.grid(row=0, column=0, padx=5, pady=10, columnspan=1)
        self.quitButton.grid(row=1, column=0, padx=10, pady=10)
        self.Refresh.grid(row=1, column=1, padx=10, pady=10)


    def close_windows(self):
        self.master.destroy()

    #wyświetlanie w nowym oknie onka od tworzenia checklisty
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






