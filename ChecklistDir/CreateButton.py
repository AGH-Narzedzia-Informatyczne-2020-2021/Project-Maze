from tkinter import *
from ChecklistDir import config



class CreateButton:


    def __init__(self, master, parent):
        self.master = master
        self.master.title("Nowa Checklista")
        self.master.geometry("170x220")

        # wyświetlanie tekstu
        NewChecklistText = Label(self.master, text="Podaj nazwę nowej checklisty:")
        AddTaskText = Label(self.master, text="Dodaj nowe zadanie:")

        # Lista zadań
        Tasks = []
        # Magiczny globalny Label w jednoelementowej tablicy, bo inczej nie działa, ja też nie wiem o co chodzi, a tez sobie zastosuje ta sztuczke
        TaskText = [Label(self.master)]
        TaskAdded = [Label(self.master)]
        # self.frame = Frame(self.master)
        # self.frame.pack()
        # self.parent = parent

        # pobieranie testu
        self.NewChecklistName = Entry(self.master, width=25)
        self.Task = Entry(self.master, width=25)

        # tworzenie nowej checklisty
        def Make():
            global ListName

            ListName = self.NewChecklistName.get() +".txt"
            file = open("ChecklistDir/lists/" + str(ListName), "w")
            config.ChecklistNames.append(ListName)
            config.n+=1

            Tasks.clear()
            TaskText[0].destroy()
            TaskAdded[0].destroy()
            self.NewChecklistName.delete(0, 'end')
            file.close()

        #dodanie zadnia
        def Add():
            TaskText[0].destroy()
            TaskAdded[0].destroy()
            a = self.Task.get()
            Tasks.append(a)

            TaskAdded[0] = Label(master,text="Dodano zadanie nr "+  str(len(Tasks))+"\n do checklisty \""+str(config.ChecklistNames[config.n-1])+"\": ")
            TaskAdded[0].grid(row=4, column=0)
            self.Task.delete(0, 'end')

            file = open(("ChecklistDir/lists/" + str(config.ChecklistNames[config.n-1])), "w")
            for i in Tasks:
                file.write(i)
                file.write("\n")

            TaskText[0] = Label(master, text=a)
            TaskText[0].grid(row=5, column=0)
            file.close()


        def close_windows():
            self.master.destroy()

        # deklaracja przycisków
        self.AddButton = Button(self.master, text="Dodaj", padx=40, pady=4, command=Add)
        self.MakeButton = Button(self.master, text="Stworz", padx=38, pady=4, command=Make)
        self.cancelButton = Button(self.master, text="Anuluj", bg="DarkRed", padx=38, pady=4, command=close_windows)

        # ustawienie w oknie
        NewChecklistText.grid(row=0, column=0)
        self.NewChecklistName.grid(row=1, column=0)
        AddTaskText.grid(row=2, column=0)
        self.Task.grid(row=3, column=0)
        self.AddButton.grid(row=6, column=0)
        self.MakeButton.grid(row=7, column=0)
        self.cancelButton.grid(row=8, column=0)
