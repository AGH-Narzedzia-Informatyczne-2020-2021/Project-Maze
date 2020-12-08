from tkinter import *
from PIL import Image,ImageTk
from resizeimage import resizeimage
#import os

class CountryIMG:
    def __init__(self):
        self.size = 400
        self.TXT =open('CountryImages\Europ\Panstwa.txt',"r",encoding="utf-8")

        self.CountryName=[]
        self.CountryImage = []

        for line in self.TXT:
            line = line.replace('\n','')
            self.name=line
            line = line.lower()
            line = self.removeAccents(line)
            try:
                self.PATH= "CountryImages\Europ\mapa-"+line+".gif"

                self.IMG = Image.open(self.PATH)
                self.ImageResized = resizeimage.resize_cover(self.IMG,[self.size, self.size])
                self.countryImage = ImageTk.PhotoImage(self.ImageResized)
                self.CountryName.append(self.name)
                self.CountryImage.append(self.countryImage)
            except:
                line = line.upper()

        self.Country= [list(a) for a in zip(self.CountryImage, self.CountryName)]

    def removeAccents(self,input_text):
        self.strange='ąćęłńóśżź '
        self.ascii_replacements='acelnoszz-'
        self.translator=str.maketrans(self.strange,self.ascii_replacements)

        return input_text.translate(self.translator)