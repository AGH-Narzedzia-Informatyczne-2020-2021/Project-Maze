from tkinter import *
from PIL import Image,ImageTk
from resizeimage import resizeimage
import os

class CountryIMG:
    def __init__(self):
        self.size = 400
        self.files = os.listdir(r'CountryImages\Europ')
        self.CountryImage = []

        for self.f in self.files:
            self.ImageResized = resizeimage.resize_cover(Image.open(r'CountryImages\Europ\\' + self.f),[self.size, self.size])
            self.countryImage = ImageTk.PhotoImage(self.ImageResized)
            self.CountryImage.append(self.countryImage)

        #tymczasowo w tablicy , w przyszlosci dzialnie na pliku
        self.CountryName = ["Kosowo","Norwegia","Albania","Andora","Austria","Belgia","Bialoruś","Bośnia i Hercegowina",
                            "Bułgaria","Chorwacja","Czarnogóra","Czechy","Dania","Estonia","Finlandia","Francja","Gibraltar",
                            "Grecja","Hiszpania","Holadnia","Irlandia","Islandia","Jan Mayen","Jersey","Lichtenstein",
                            "Litwa","Łotwa","Luksemburg","Macedonia","Malta","Mołdawia","Monako","Niemcy","Polska","Portugalia",
                            "Rosja","Rumunia","San Marino","Serbia","Słowacja","Słowenia","Szwajcaria","Szwecja","Ukraina","Watykan",
                            "Węgry","Wielka Brytania","Włochy","Wyspa Man","Wyspy Owcze"]

        self.Country= [list(a) for a in zip(self.CountryImage, self.CountryName)]
