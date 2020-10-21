from tkinter import *
from PIL import Image, ImageTk
import MenuLib


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300")
    app = MenuLib.Menu(root)
    root.mainloop()
