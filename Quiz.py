from tkinter import *
from PIL import Image,ImageTk
from resizeimage import resizeimage
import CountryIMG
import random



class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz")
        self.master.geometry("500x400")
        self.master.iconbitmap(r'Images\earth_icon.ico')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.quitButton = Button(self.frame, text = 'X', padx=15,pady=10, bg = "red",command=self.close_windows)
        #self.quitButton.grid(row =0, column=2)
        self.startLabel = Label(self.frame, text="Aby rozpocząć kliknij przycisk Start")
        self.startLabel.grid(row=1,column=0)
        self.startButton = Button(self.frame,text="START",padx=30,pady=10,bg = "green",command=self.Start)
        self.startButton.grid(row=2,column=0)
        self.startImageResized = resizeimage.resize_cover(Image.open(r'Images\StartQuiz.png'),[500,300])
        self.startImage = ImageTk.PhotoImage(self.startImageResized)
        self.startImageLabel = Label(self.frame,image = self.startImage)
        self.startImageLabel.grid(row =0,column=0)

        self.countryList = CountryIMG.CountryIMG()
        self.numberOfQuestion = 10
        self.QuizList = random.sample(self.countryList.County,self.numberOfQuestion)

    def Start(self):
        self.startButton.destroy()
        self.startLabel.destroy()
        self.startImageLabel.destroy()
        self.master.geometry("500x600")
        self.Quiz_work()

    def Quiz_work(self):
        self.QuestionNumber = -1
        self.points = 0

        self.tmpName=self.QuizList[0][1]

        self.Question = Label(self.frame)
        self.Question.grid(row=0, column=0, columnspan=3)

        self.countryLabel = Label(self.frame)
        self.countryLabel.grid(row=1, column=0, columnspan=3)
        #Countyr name do celuw debugerskich quizu
        self.countryName = Label(self.frame)
        self.countryName.grid(row=2, column=0, columnspan=3)

        self.odpA = Button(self.frame, command=lambda:self.Next_Question(self.odpA.cget('text')))
        self.odpA.grid(row=3, column=0,)
        self.odpB = Button(self.frame, command=lambda:self.Next_Question(self.odpB.cget('text')))
        self.odpB.grid(row=3, column=1)
        self.odpC = Button(self.frame, command=lambda:self.Next_Question(self.odpC.cget('text')))
        self.odpC.grid(row=3, column=2)

        self.Wynik = Label(self.frame)
        self.Wynik.grid(row=4, column=0, columnspan=3,pady=50)

        self.Next_Question()

    def Next_Question(self, odp = ""):
        #sprawdzenie odpowiedzi i przyznanie punktow
        if (odp == self.tmpName):
            self.points +=1
        self.QuestionNumber +=1
        #jeżeli jeszcze są państwa ustaw pytanie i odpowiedzi
        if (self.QuestionNumber < len(self.QuizList)):        
            self.tmpImage = self.QuizList[self.QuestionNumber][0]
            self.tmpName = self.QuizList[self.QuestionNumber][1]

            self.Question.config(text=str(self.QuestionNumber+1)+"/"+str(self.numberOfQuestion))
            self.countryLabel.config(image=self.tmpImage)
            self.countryName.config(text=self.tmpName)
            #tworzenie odpowiedzi
            self.Names =  random.sample(self.countryList.CountryName,2)
            self.Names.append(self.tmpName)
            random.shuffle(self.Names)

            self.odpA.config(text=self.Names[0])
            self.odpB.config(text=self.Names[1])
            self.odpC.config(text=self.Names[2])

            self.Wynik.config(text="wynik: "+str(self.points)+"/"+str(self.QuestionNumber))
        else:
            self.close_windows()
            #wyświetlenie ekranu końcowego


    def close_windows(self):
        self.master.destroy()
