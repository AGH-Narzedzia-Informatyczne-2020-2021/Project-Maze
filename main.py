from tkinter import *
from PIL import Image,ImageTk

#root
root = Tk()
root.title('main')
root.iconbitmap(r'Images\cube_icon_.ico')
root.geometry("500x450")

#programy

def open_program1():
    return

def open_program2():
    return

def open_program3():
    return

def open_program4():
    return


# deklaracja przyciskow do programow
program1 = Button(root,text="program 1",padx=40,pady=50)
program2 = Button(root,text="program 2",padx=40,pady=50)
program3 = Button(root,text="program 3",padx=40,pady=50)
program4 = Button(root,text="program 4",padx=40,pady=50)

# umiejscowienie w main
program1.grid(row=0,column=0,padx=50,pady=50,command= open_program1)
program2.grid(row=0,column=1,padx=50,pady=50,command= open_program2)
program3.grid(row=1,column=0,padx=50,pady=50,command= open_program3)
program4.grid(row=1,column=1,padx=50,pady=50,command= open_program4)


root.mainloop()
