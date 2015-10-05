# Simple GUI
# Demonstrates creating a window
from tkinter import *

# create the root window
root = Tk()

# modify the window
root.title("Simple GUI")
root.geometry("200x100")

app = Frame(root)
app.grid()
lbl = Label(app, text = "I am a Label!")
lbl.grid()

bttn1 = Button(app, text = "I am a button!")
bttn1.grid()
