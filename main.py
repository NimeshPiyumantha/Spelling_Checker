import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

heading= Label(root,text="Spelling Checker",font=("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

root.mainloop()
