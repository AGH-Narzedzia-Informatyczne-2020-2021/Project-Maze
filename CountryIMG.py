from tkinter import *
from PIL import Image,ImageTk
from resizeimage import resizeimage

class CountryIMG:
    def __init__(self):
        self.size = 400
        self.kosowoResized = resizeimage.resize_cover(Image.open(r'CountryImages\Europ\kosowo2-970x542.jpg'),[self.size,self.size])
        self.KosowoImage=ImageTk.PhotoImage(self.kosowoResized)
        self.kosowo=[self.KosowoImage,"Kosowo"]
        self.norwegiaResized = resizeimage.resize_cover(Image.open(r'CountryImages\Europ\lokalizacja-norwegii-na-tle-europy.gif'),[self.size,self.size])
        self.NorwegiaImage = ImageTk.PhotoImage(self.norwegiaResized)
        self.norwegia=[self.NorwegiaImage,"Norwegia"]
        self.albaniaResized = resizeimage.resize_cover(Image.open(r'CountryImages\Europ\mapa-albania.gif'),[self.size,self.size])
        self.AlbaniaImage = ImageTk.PhotoImage(self.albaniaResized)
        self.albania=[self.AlbaniaImage,"Albania"]
        self.CountryList = [self.kosowo,self.norwegia,self.albania]





