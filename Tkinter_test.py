from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

global path
top = Tk()
# Code to add widgets will go here...
def helloCallBack():
   path = filedialog.askopenfilename()
   with open(path, "w") as filepath:
      filepath.write("test")
   messagebox.showinfo( "Python Window Header", "Success!")
top.geometry("400x300")
TEXT = Text(top)
TEXT.insert(INSERT, "test")
TEXT.place(x=0,y=0)
TEXT.configure(state=DISABLED)
B = Button(top, text="Button Text", command=helloCallBack)
B.place(x=50,y=250)

top.mainloop()