from tkinter import *


operators = {"+", "-", "*", "/"}


def split(sentence):
    formulas = []
    index = 0
    last_sing_index = -1
    for letter in sentence:
        if letter in operators:
            formulas.append(sentence[last_sing_index+1:index])
            formulas.append(sentence[index:index+1])
            last_sing_index = index
        index += 1
    formulas.append(sentence[last_sing_index+1:])

    while "" in formulas:
        formulas.remove("")
    # print(formulas)  # debug
    return formulas


def remove_unwanted_sings(list_of_formulas):
    # removing sings from front
    have_minus_in_front = False
    while list_of_formulas[0] in operators:
        if list_of_formulas[0] == "-":
            have_minus_in_front = True
        list_of_formulas.pop(0)
    if have_minus_in_front:
        list_of_formulas.insert(0, "-")

    # removing sings from end
    while list_of_formulas[-1] in operators:
        list_of_formulas.pop()

    return list_of_formulas


def simple_calc(a, operator, b):
    a = int(a)
    b = int(b)
    if operator == "+":
        return a+b
    if operator == "-":
        return a-b
    if operator == "*":
        return a*b
    if operator == "/":
        return a/b
    print("Error in simple_calc")
    return 0


def priority_calc(operators_set, formulas):
    i = 0
    while i < len(formulas):
        if formulas[i] in operators_set:
            result = simple_calc(formulas[i - 1], formulas[i], formulas[i + 1])
            formulas.pop(i + 1)
            formulas.pop(i)
            formulas.pop(i - 1)
            formulas.insert(i - 1, result)
            break
        i += 1
    return formulas


class Calculator:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Kalkulator")
        self.master.geometry("500x500")
        self.frame = Frame(self.master)

        sk=5   #szerokosc przyciskow
        wk=2    #wysokosc przyciskow

        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=0, columnspan=3,sticky=N+S+W+E)

        self.calculate = Button(self.master, text="=", height=wk, width=sk, command=self.calculate)
        self.calculate.grid(row=0, column=3, rowspan=2)

        self.result = Entry(self.master, text="0")
        self.result.grid(row=1, column=0, columnspan=3, sticky=N+S+W+E)

        self.quitButton = Button(self.master, text='X', command=self.close_windows, bg="red", width=sk, height=wk)
        self.quitButton.grid(row=0, column=4, rowspan=2, sticky=N+S)

        self.nineButton = Button(self.master, text='9', height=wk, width=sk, command=lambda: self.click(9))
        self.nineButton.grid(row=2, column=0)

        self.eightButton = Button(self.master, text='8', height=wk, width=sk, command=lambda: self.click(8))
        self.eightButton.grid(row=2, column=1)

        self.sevenButton = Button(self.master, text='7', height=wk, width=sk, command=lambda: self.click(7))
        self.sevenButton.grid(row=2, column=2)

        self.divisionButton = Button(self.master, text='/', height=wk, width=sk)
        self.divisionButton.grid(row=2, column=3)

        self.sixButton = Button(self.master, text='6', height=wk, width=sk, command=lambda: self.click(6))
        self.sixButton.grid(row=3, column=0)

        self.fiveButton = Button(self.master, text='5', height=wk, width=sk, command=lambda: self.click(5))
        self.fiveButton.grid(row=3, column=1)

        self.fourButton = Button(self.master, text='4', height=wk, width=sk, command=lambda: self.click(4))
        self.fourButton.grid(row=3, column=2)

        self.multiplicationButton = Button(self.master, text='*', height=wk, width=sk)
        self.multiplicationButton.grid(row=3, column=3)

        self.treeButton = Button(self.master, text='3', height=wk, width=sk, command=lambda: self.click(3))
        self.treeButton.grid(row=4, column=0)

        self.twoButton = Button(self.master, text='2', height=wk, width=sk, command=lambda: self.click(2))
        self.twoButton.grid(row=4, column=1)

        self.oneButton = Button(self.master, text='1', height=wk, width=sk, command=lambda: self.click(1))
        self.oneButton.grid(row=4, column=2)

        self.subtractionButton = Button(self.master, text='-', height=wk, width=sk)
        self.subtractionButton.grid(row=4, column=3)

        self.emptyButton = Button(self.master, text='', height=wk, width=sk)
        self.emptyButton.grid(row=5, column=0)

        self.zeroButton = Button(self.master, text='0', height=wk, width=sk)
        self.zeroButton.grid(row=5, column=1)

        self.dotButton = Button(self.master, text='.', height=wk, width=sk)
        self.dotButton.grid(row=5, column=2)

        self.additionButton = Button(self.master, text='+', height=wk, width=sk)
        self.additionButton.grid(row=5, column=3)


        self.result.delete(0, "end")

    def close_windows(self):    #komenda zamykania
        self.master.destroy()

    def click(self, nmbr, i=100):            #wypisywanie cyfr po kliknieciu przycicku
        self.entry.insert(i, nmbr)

    def calculate(self):
        self.result.delete(0, 'end')
        formulas = split(self.entry.get())
        formulas = remove_unwanted_sings(formulas)

        if formulas[0] == "-":
            formulas.insert(0, "0")
        print(formulas)

        ##### odtąd kod do poprawki
        for i in range(10):
            formulas = priority_calc({"*", "/"}, formulas)
        for i in range(10):
            formulas = priority_calc({"+", "-"}, formulas)
        print(formulas)
        result = formulas[0]

        self.result.insert(0, result)


