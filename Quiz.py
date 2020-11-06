from tkinter import *
from PIL import Image,ImageTk
from resizeimage import resizeimage
import CountryIMG



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
        self.tmpImage = self.countryList.CountryImage[0]

    def Start(self):
        self.startButton.destroy()
        self.startLabel.destroy()
        self.startImageLabel.destroy()
        self.master.geometry("500x600")
        self.Quiz_work()

    def Quiz_work(self):
        self.countryLabel = Label(self.frame,image = self.tmpImage)
        self.countryLabel.grid(row = 0 , column=0)


    def close_windows(self):
        self.master.destroy()
