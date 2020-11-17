from tkinter import *




class DropDown:

    def __init__(self, master, parent):
        self.master = master
        self.master.title("Checklisty")
        self.master.geometry("250x200")
        #self.frame = Frame(self.master)
        #self.frame.pack()
        #self.parent = parent

        var = StringVar()

        def show():
            myLabel=Label(self.master, text=var.get()).grid(row=1, column=1)


        #deklaracja checklisty
        self.c = Checkbutton(self.master, text="Pierwsze zadanie",  padx=50, pady= 4, variable=var, onvalue="  Zrobione  ", offvalue="Do zrobienia" )
        self.c.deselect()

        #deklaracja przycisków
        self.showButton = Button(self.master, text="Pokaz", padx=40, pady= 4, command=show)
        self.quitButton = Button(self.master, text='Wyjście', padx=35, pady= 4,  command=self.close_windows)

        #ustawienie w oknie
        self.c.grid(row=0, column=0,  columnspan=3, sticky= W+E+N+S)
        self.showButton.grid(row=2, column=1)
        self.quitButton.grid(row=3, column=1)

        #testowe rozwijane menu
        variable = StringVar(master)
        variable.set("one")  # Wartośc podstawowa

        self.w = OptionMenu(master, variable, "one", "two", "three")
        self.w.grid(row=5, column=1)

    def close_windows(self):
        self.master.destroy()
