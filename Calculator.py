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
        self.master.title("Window1")
        self.master.geometry("550x200")
        self.frame = Frame(self.master)

        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=0)

        self.calculate = Button(self.master, text="=", command=self.calculate)
        self.calculate.grid(row=0, column=1, rowspan=2, columnspan=2, sticky=N+S)

        self.result = Entry(self.master, text="0")
        self.result.grid(row=1, column=0)

        self.quitButton = Button(self.master, text='Zamknij', command=self.close_windows)
        self.quitButton.grid(row=0, column=3, rowspan=2, columnspan=2, sticky=N + S)

        self.result.delete(0, "end")

    def close_windows(self):
        self.master.destroy()

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


