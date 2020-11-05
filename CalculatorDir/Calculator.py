from tkinter import *
from CalculatorDir import Rational


operators = {"+", "-", "*", "/"}
numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
legal_sings = operators.union(numbers)
legal_sings = legal_sings.union({"."})


def is_valid(list_of_formulas):  # sprawdza czy użytkownik nie podał błędnych znaków
    for word in list_of_formulas:
        for letter in word:
            if letter not in legal_sings:
                return False
    return True


def split_sentence(sentence):    # rozdziela dane na znaki i liczby tz 1+22 => 1, +, 22
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
    print(formulas)  # debug
    return formulas


def remove_unwanted_sings(list_of_formulas):
    # removing sings from front
    have_minus_in_front = False
    while list_of_formulas[0] in operators:  # usuwa niepotrzebne znaki z początku
        if list_of_formulas[0] == "-":
            have_minus_in_front = True
        list_of_formulas.pop(0)
    if have_minus_in_front:
        list_of_formulas.insert(0, "-")  # jeśli na początku był minus to dodaje 0-...
        list_of_formulas.insert(0, "0")

    # removing sings from end
    while list_of_formulas[-1] in operators:     # usuwa niepotrzebne znaki z końca
        list_of_formulas.pop()

    return list_of_formulas


def simple_calc(a, operator, b):     # potrafi wykonać bazowe obliczenia jak 1+3
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


def priority_calc(operators_set, formulas):  # wykonuje działania na operatorach danych w operators_set
    sth_changed = False
    i = 0
    while i < len(formulas):
        if formulas[i] in operators_set:
            result = simple_calc(formulas[i - 1], formulas[i], formulas[i + 1])
            formulas.pop(i + 1)
            formulas.pop(i)
            formulas.pop(i - 1)
            formulas.insert(i - 1, result)
            sth_changed = True
            break
        i += 1
    return formulas, sth_changed


def convert_to_rational(formulas):
    print(formulas)
    rationals = []
    for word in formulas:
        if word[0] not in operators:
            rationals.append(Rational.to_rational(word))
        else:
            rationals.append(word)
    return rationals


class Calculator:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Kalkulator")
        self.master.geometry("500x500")
        self.frame = Frame(self.master)

        sk = 5   # szerokosc przyciskow
        wk = 2    # wysokosc przyciskow

        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)

        self.calculate = Button(self.master, text="=", height=wk, width=sk, command=self.calculate)
        self.calculate.grid(row=0, column=3, rowspan=2)

        self.result = Entry(self.master, text="0")
        self.result.grid(row=1, column=0, columnspan=3, sticky=N+S+W+E)

        self.quitButton = Button(self.master, text='X', command=self.close_windows, bg="red", width=sk, height=wk)
        self.quitButton.grid(row=0, column=4, rowspan=2, sticky=N+S)

        self.nineButton = Button(self.master, text='9', height=wk, width=sk, command=lambda: self.click('9'))
        self.nineButton.grid(row=2, column=0)

        self.eightButton = Button(self.master, text='8', height=wk, width=sk, command=lambda: self.click('8'))
        self.eightButton.grid(row=2, column=1)

        self.sevenButton = Button(self.master, text='7', height=wk, width=sk, command=lambda: self.click('7'))
        self.sevenButton.grid(row=2, column=2)

        self.divisionButton = Button(self.master, text='/', height=wk, width=sk, command=lambda: self.click("/"))
        self.divisionButton.grid(row=2, column=3)

        self.sixButton = Button(self.master, text='6', height=wk, width=sk, command=lambda: self.click('6'))
        self.sixButton.grid(row=3, column=0)

        self.fiveButton = Button(self.master, text='5', height=wk, width=sk, command=lambda: self.click('5'))
        self.fiveButton.grid(row=3, column=1)

        self.fourButton = Button(self.master, text='4', height=wk, width=sk, command=lambda: self.click('4'))
        self.fourButton.grid(row=3, column=2)

        self.multiplicationButton = Button(self.master, text='*', height=wk, width=sk, command=lambda: self.click("*"))
        self.multiplicationButton.grid(row=3, column=3)

        self.treeButton = Button(self.master, text='3', height=wk, width=sk, command=lambda: self.click('3'))
        self.treeButton.grid(row=4, column=0)

        self.twoButton = Button(self.master, text='2', height=wk, width=sk, command=lambda: self.click('2'))
        self.twoButton.grid(row=4, column=1)

        self.oneButton = Button(self.master, text='1', height=wk, width=sk, command=lambda: self.click('1'))
        self.oneButton.grid(row=4, column=2)

        self.subtractionButton = Button(self.master, text='-', height=wk, width=sk, command=lambda: self.click("-"))
        self.subtractionButton.grid(row=4, column=3)

        self.clearButton = Button(self.master, text='C', height=wk, width=sk, command=self.clear)
        self.clearButton.grid(row=5, column=0)

        self.zeroButton = Button(self.master, text='0', height=wk, width=sk, command=lambda: self.click('0'))
        self.zeroButton.grid(row=5, column=1)

        self.dotButton = Button(self.master, text='.', height=wk, width=sk, command=lambda: self.click("."))
        self.dotButton.grid(row=5, column=2)

        self.additionButton = Button(self.master, text='+', height=wk, width=sk, command=lambda: self.click("+"))
        self.additionButton.grid(row=5, column=3)

        self.result.delete(0, "end")

    def clear(self):             # komenda czyszczenia
        self.entry.delete(0, 'end')
        self.result.delete(0, 'end')

    def close_windows(self):    # komenda zamykania
        self.master.destroy()

    def click(self, nmbr):  # wypisywanie cyfr po kliknieciu przycisku

        if self.entry.get() == '0':
            if nmbr != '+' and nmbr != '-' and nmbr != '*' and nmbr != '/':
                self.entry.delete(0, 'end')

        self.result.delete(0, 'end')
        current = self.entry.get()
        self.entry.delete(0, 'end')
        self.entry.insert(0, str(current) + str(nmbr))

        if len(self.entry.get()) == 1:
            if nmbr == '+' or nmbr == '-' or nmbr == '*' or nmbr == '/':
                self.entry.delete(0, 'end')

        if len(self.entry.get()) > 2:
            current = self.entry.get()
            if current[-2] == '+' or current[-2] == '-' or current[-2] == '*' or current[-2] == '/':
                if current[-1] == '+' or current[-1] == '-' or current[-1] == '*' or current[-1] == '/':
                    self.entry.delete(0, 'end')
                    self.entry.insert(0, current[0:-2] + nmbr)

    def calculate(self):

        self.result.delete(0, 'end')
        formulas = split_sentence(self.entry.get())
        formulas = remove_unwanted_sings(formulas)

        if not is_valid(formulas):
            self.result.insert(0, "Error")
            return

        formulas = convert_to_rational(formulas)
        print(formulas)

        should_continue = True
        while should_continue:
            formulas, should_continue = priority_calc({"*", "/"}, formulas)
        should_continue = True
        while should_continue:
            formulas, should_continue = priority_calc({"+", "-"}, formulas)

        print(formulas)
        result = formulas[0]

        self.result.insert(0, result)
