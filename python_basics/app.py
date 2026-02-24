#Name :Ethan Mbila
#Date :24/02/2026

from tkinter import *
root = Tk()
root.geometry("640x400")

frame1 = Frame(root)
frame1.pack()

button1 = Button(frame1, text="say hello", command= print("hello"))
button1.pack()

root.mainloop()