from tkinter import *
from ChecklistDir import config



class DropDown:

    def __init__(self, master, parent ):
        self.master = master
        self.master.title("Checklisty")
        self.master.geometry("250x200")
        #self.frame = Frame(self.master)
        #self.frame.pack()
        #self.parent = parent

        #var = StringVar()
        #przepisywaie pliku(chechlisty) do tablicy
        file = open(("ChecklistDir/lists/" + str(config.ChecklistNames[config.name])), "r")
        todo=[i for i in file.readlines()]
        file.close()

        #wyswitlanie zawartosci checklisty
        config.line = 0
        def show(line):
            #global line
            if line !=0 and line <= len(todo):
                 myLablel = Label(self.master, text="Zadanie "+ str(line) + " z "+str(len(todo)) + ":\n" + todo[line-1], fg="Lightgrey").grid(row=config.line, column=0, columnspan=2)
            if line < len(todo):
                myLablel2 = Label(self.master, text="Zadanie "+str(line+1) + " z "+str(len(todo)) + ":\n" + todo[line], fg="Magenta").grid(row=config.line+1, column=0, columnspan=2)
            if line == len(todo):
                myLablel3 = Label(self.master,text="Gratulacje zrobiłeś wszystko", fg="Gold", font=" bold", bg="black").grid(row=config.line+2, column=0, columnspan=2)
            config.line+=1


        #deklaracja przycisków
        self.showButton = Button(self.master, text="Zrobione", padx=40, pady= 4, command=lambda: show(config.line))
        self.quitButton = Button(self.master, text='Wyjście', padx=35, pady= 4,  bg="DarkRed", command=self.close_windows)

        #ustawienie w oknie
         # self.c.grid(row=0, column=0,  columnspan=3, sticky= W+E+N+S)
        self.showButton.grid(row=0, column=0)
        self.quitButton.grid(row=0, column=1)

        #testowe
        #deklaracja testowej checklisty
        # self.c = Checkbutton(self.master, text="Pierwsze zadanie",  padx=50, pady= 4, variable=var, onvalue="  Zrobione  ", offvalue="Do zrobienia" )
        # self.c.deselect()
        #testowe rozwijane menu
        #variable = StringVar(master)
        #variable.set("one")  # Wartośc podstawowa
         #self.w = OptionMenu(master, variable, "one", "two", "three")
        #self.w.grid(row=5, column=1)

    def close_windows(self):
        self.master.destroy()






