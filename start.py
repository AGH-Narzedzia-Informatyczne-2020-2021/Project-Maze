from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('test')
root.geometry("500x450")

program1 = Button(root,text="program 1",padx=40,pady=50)
program2 = Button(root,text="program 2",padx=40,pady=50)
program3 = Button(root,text="program 3",padx=40,pady=50)
program4 = Button(root,text="program 4",padx=40,pady=50)

program1.grid(row=0,column=0,padx=50,pady=50)
program2.grid(row=0,column=1,padx=50,pady=50)
program3.grid(row=1,column=0,padx=50,pady=50)
program4.grid(row=1,column=1,padx=50,pady=50)



root.mainloop()