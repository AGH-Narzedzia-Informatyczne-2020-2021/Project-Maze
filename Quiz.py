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
        #self.quitButton = Button(self.frame, text = 'X', padx=15,pady=10, bg = "red",command=self.close_windows)
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


    def Start(self):
        self.frame.destroy()
        #self.startButton.destroy()
        #self.startLabel.destroy()
        #self.startImageLabel.destroy()
        self.master.geometry("500x600")
        self.Quiz_work()

    def Quiz_work(self):
        self.QuizList = random.sample(self.countryList.Country, self.numberOfQuestion)
        self.QuizFrame = Frame(self.master)
        self.QuizFrame.pack()
        self.QuestionNumber = -1
        self.points = 0

        self.tmpName=self.QuizList[0][1]

        self.Question = Label(self.QuizFrame)
        self.Question.grid(row=0, column=0, columnspan=5)

        self.countryLabel = Label(self.QuizFrame)
        self.countryLabel.grid(row=1, column=0, columnspan=5)
        #Country name do celów debugerskich quizu
        self.countryName = Label(self.QuizFrame)
        self.countryName.grid(row=2, column=0, columnspan=5)

        self.odpA = Button(self.QuizFrame, command=lambda:self.Next_Question(self.odpA.cget('text')))
        self.odpA.grid(row=3, column=0,)
        self.odpB = Button(self.QuizFrame, command=lambda:self.Next_Question(self.odpB.cget('text')))
        self.odpB.grid(row=3, column=1)
        self.odpC = Button(self.QuizFrame, command=lambda:self.Next_Question(self.odpC.cget('text')))
        self.odpC.grid(row=3, column=2)
        self.odpD = Button(self.QuizFrame , command =lambda:self.Next_Question(self.odpD.cget("text")))
        self.odpD.grid(row =3,column =4)

        self.Wynik = Label(self.QuizFrame)
        self.Wynik.grid(row=4, column=0, columnspan=5,pady=50)

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
            self.Names =  random.sample(self.countryList.CountryName,3)
            self.Names.append(self.tmpName)
            random.shuffle(self.Names)

            self.odpA.config(text=self.Names[0])
            self.odpB.config(text=self.Names[1])
            self.odpC.config(text=self.Names[2])
            self.odpD.config(text=self.Names[3])

            self.Wynik.config(text="wynik: "+str(self.points)+"/"+str(self.numberOfQuestion))
        else:
            self.stat_window()

    def stat_window(self):
        self.QuizFrame.destroy()
        self.Statframe = Frame(self.master)
        self.Statframe.pack()
        self.StatystykaWynik = Label(self.Statframe,text="wynik: "+str(self.points)+"/"+str(self.numberOfQuestion))
        self.StatystykaWynik.grid(row=0,column=0,padx=50, pady=50)

        self.ReplayButton = Button(self.Statframe,text="Spróbuj jeszcze raz",command =self.Replay)
        self.ReplayButton.grid(row=1,pady=20)
    def Replay(self):
        self.Statframe.destroy()
        self.Quiz_work()

    def close_windows(self):
        self.master.destroy()
