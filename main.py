import tkinter as tk
import tkinter.font as tkFont

response = ""

root = tk.Tk()
# setting title
root.title("Cleanliness Rater")
# setting height of the panel
width = 485
height = 144
# retrieve the screen width info
screenwidth = root.winfo_screenwidth()
# retrieve the screen height info
screenheight = root.winfo_screenheight()

alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)


# resize the screen
# root.resizable(width=False, height=True)


def clickBtnOne():
    response = "This bus has the average rating of : 1"


btnOne = tk.Button(root)
btnOne["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnOne["font"] = ft
btnOne["fg"] = "#000000"
btnOne["justify"] = "center"
btnOne["text"] = "1"
btnOne.place(x=30, y=60, width=70, height=25)
btnOne["command"] = clickBtnOne()


def clickBtnTwo():
   response = "This bus has the average rating of : 2"


btnTwo = tk.Button(root)
btnTwo["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnTwo["font"] = ft
btnTwo["fg"] = "#000000"
btnTwo["justify"] = "center"
btnTwo["text"] = "2"
btnTwo.place(x=110, y=60, width=70, height=25)
btnTwo["command"] = clickBtnTwo()


def clickBtnThree():
    response = "This bus has the average rating of : 3"


btnThree = tk.Button(root)
btnThree["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnThree["font"] = ft
btnThree["fg"] = "#000000"
btnThree["justify"] = "center"
btnThree["text"] = "3"
btnThree.place(x=190, y=60, width=70, height=25)
btnThree["command"] = clickBtnThree()


def clickBtnFour():
    response = "This bus has the average rating of : 4"


btnFour = tk.Button(root)
btnFour["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnFour["font"] = ft
btnFour["fg"] = "#000000"
btnFour["justify"] = "center"
btnFour["text"] = "4"
btnFour["command"] = clickBtnFour()

btnFour.place(x=270, y=60, width=70, height=25)


def clickBtnFive():
    response = "This bus has the average rating of : 4"


btnFive = tk.Button(root)
btnFive["bg"] = "#efefef"
ft = tkFont.Font(family='Arial', size=10)
btnFive["font"] = ft
btnFive["fg"] = "#000000"
btnFive["justify"] = "center"
btnFive["text"] = "5"
btnFive.place(x=350, y=60, width=70, height=25)
btnFive["command"] = clickBtnFive()

labelHeader = tk.Label(root)
ft = tkFont.Font(family='Arial', size=12)
labelHeader["font"] = ft
labelHeader["fg"] = "#333333"
labelHeader["justify"] = "center"
labelHeader["text"] = "Rate the cleanliness of the bus"
labelHeader.place(x=70, y=10, width=320, height=30)

labelResult = tk.Label(root)
ft = tkFont.Font(family='Arial', size=12)
labelResult["font"] = ft
labelResult["fg"] = "#333333"
labelResult["justify"] = "center"
labelHeader["text"] = response
labelResult.place(x=90, y=90, width=282, height=30)
root.mainloop()
