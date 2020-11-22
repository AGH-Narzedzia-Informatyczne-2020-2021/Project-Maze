from tkinter import *


class CreateButton:

    def __init__(self, master, parent):
        self.master = master
        self.master.title("Checklisty")
        self.master.geometry("250x200")
        # self.frame = Frame(self.master)
        # self.frame.pack()
        # self.parent = parent

        #pobieranie testu
        self.Task = Entry(self.master)

        def Add():
            a = self.Task.get()
            MyLabel = Label(self.master, text=a)
            MyLabel.grid(row =0, column=0)
            self.Task.delete(0, 'end')

        def Make():
            a = self.Task.get()
            MyLabel = Label(self.master, text=a)
            MyLabel.grid(row=4, column=0)

        # deklaracja przycisków
        self.AddButton = Button(self.master, text="Dodaj", padx=40, pady=4, command=Make)
        self.MakeButton = Button(self.master, text='Stworz', padx=35, pady=4, command=Add)

        # ustawienie w oknie
        self.Task.grid(row =1, column=0)
        self.AddButton.grid(row =2, column=0)
        self.MakeButton.grid(row =3, column=0)

        def close_windows(self):
            self.master.destroy()
