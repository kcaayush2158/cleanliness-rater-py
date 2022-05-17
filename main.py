import tkinter as tk
import tkinter.font as tkFont
from tkinter import X, Y


def clickBtnOne():
    labelResult["text"] = "This bus has the average rating of : 1"


def clickBtnTwo():
    labelResult["text"] = "This bus has the average rating of : 2"


def clickBtnThree():
    labelResult["text"] = "This bus has the average rating of : 3"


def clickBtnFour():
    labelResult["text"] = "This bus has the average rating of : 4"


def clickBtnFive():
    labelResult["text"] = "This bus has the average rating of : 5"


root = tk.Tk()
# setting title
root.title("Cleanliness Rater")


# setting height of the panel
width = 600
height = 144
# retrieve the screen width info
screenwidth = root.winfo_screenwidth()
# retrieve the screen height info
screenheight = root.winfo_screenheight()

alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)

# resize the screen
root.resizable(width=True, height=True)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(3, weight=1)

# Header Label
labelHeader = tk.Label(root)
ft = tkFont.Font(family='Arial', size=12)
labelHeader["font"] = ft
labelHeader["fg"] = "#333333"
labelHeader["justify"] = "center"
labelHeader["text"] = "Rate the cleanliness of the bus"
labelHeader.place(relx=0.5, rely=0.2, anchor='s')

labelResult = tk.Label(root)
ft = tkFont.Font(family='Arial', size=12)
labelResult["font"] = ft
labelResult["fg"] = "#333333"
labelResult["justify"] = "center"
labelResult.place(x=90, y=90, width=282, height=30)
labelResult.grid(row=3, column=2)
labelResult.place(relx=0.5, rely=0.5, anchor="n")


# Button One
btnOne = tk.Button(root)
btnOne["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnOne["font"] = ft
btnOne["fg"] = "#000000"
btnOne["justify"] = "center"
btnOne["text"] = "1"
btnOne["command"] = clickBtnOne()

btnOne.place(relx=0.3, rely=0.3, anchor="n")

# Button Two
btnTwo = tk.Button(root)
btnTwo["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnTwo["font"] = ft
btnTwo["fg"] = "#000000"
btnTwo["justify"] = "center"
btnTwo["text"] = "2"
btnTwo["command"] = clickBtnTwo()
btnTwo.place(relx=0.4, rely=0.3, anchor="n")
# Button Three
btnThree = tk.Button(root)
btnThree["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)

btnThree["font"] = ft
btnThree["fg"] = "#000000"
btnThree["justify"] = "center"
btnThree["text"] = "3"
btnThree["command"] = clickBtnThree()
btnThree.place(relx=0.5, rely=0.3, anchor="n")

# Button Four
btnFour = tk.Button(root)
btnFour["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnFour["font"] = ft
btnFour["fg"] = "#000000"
btnFour["justify"] = "center"
btnFour["text"] = "4"
btnFour["command"] = clickBtnFour()
btnFour.place(relx=0.6, rely=0.3, anchor="n")

# Button Five
btnFive = tk.Button(root)
btnFive["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnFive["font"] = ft
btnFive["fg"] = "#000000"
btnFive["justify"] = "center"
btnFive["text"] = "5"
btnFive["command"] = clickBtnFive()
btnFive.place(relx=0.7, rely=0.3, anchor="n")

root.mainloop()
