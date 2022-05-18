import tkinter as tk
import tkinter.font as tkFont


# sets the text as a response
def click(x):
    if x == 1:
        labelResult["text"] = "This bus has the average rating of : 1.00"
    if x == 2:
        labelResult["text"] = "This bus has the average rating of : 2.00"
    if x == 3:
        labelResult["text"] = "This bus has the average rating of : 3.00"
    if x == 4:
        labelResult["text"] = "This bus has the average rating of : 4.00"
    if x == 5:
        labelResult["text"] = "This bus has the average rating of : 5.00"


root = tk.Tk()
# setting title
root.title("Cleanliness Rater")

# setting height of the panel
width = 600
# setting width of the panel
height = 144
# retrieve the screen width info
screenwidth = root.winfo_screenwidth()
# retrieve the screen height info
screenheight = root.winfo_screenheight()

alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
# sets the min width of the root panel
root.minsize(700, 130)
# sets the max width of the root panel
root.maxsize(900,300)
# resize the screen
root.resizable(width=True, height=True)

# setting row in the panel
root.grid_rowconfigure(3, weight=1)

# Header Label
labelHeader = tk.Label(root)
ft = tkFont.Font(family='Arial', size=15)
# adding the fonts
labelHeader["font"] = ft
# foreground color
labelHeader["fg"] = "#333333"
# text alignment
labelHeader["justify"] = "center"
# adding text
labelHeader["text"] = "Rate the cleanliness of the bus"
# positing  the label in the panel
labelHeader.place(relx=0.5, rely=0.2, anchor='s')

# response label
labelResult = tk.Label(root)
# adding the fonts
ft = tkFont.Font(family='Arial', size=15)
labelResult["font"] = ft
# foreground color
labelResult["fg"] = "#333333"
# text alignment
labelResult["justify"] = "center"
# setting label in grid
labelResult.grid(row=3, column=2)
# positing  the label in the panel
labelResult.place(relx=0.5, rely=0.5, anchor="n")


# label left :-(
labelLeft = tk.Label(root)
# adding the fonts
ft = tkFont.Font(family='Arial', size=15)
labelLeft["font"] = ft
# foreground color
labelLeft["fg"] = "#333333"
# text alignment
labelLeft["justify"] = "center"
# adding text
labelLeft["text"] = ":-("
# positing  the button in the panel
labelLeft.place(relx=0.2, rely=0.3, anchor="n")


# label right :-)
labelRight = tk.Label(root)
# adding the fonts
ft = tkFont.Font(family='Arial', size=15)
labelRight["font"] = ft
# foreground color
labelRight["fg"] = "#333333"
# text alignment
labelRight["justify"] = "center"
# adding text
labelRight["text"] = ":-)"
# positing  the button in the panel
labelRight.place(relx=0.8, rely=0.3, anchor="n")


# Button One
btnOne = tk.Button(root)

btnOne["bg"] = "#efefef"
# adding the fonts
ft = tkFont.Font(family='Arial', size=10)
btnOne["font"] = ft
# foreground color
btnOne["fg"] = "#000000"
# text alignment
btnOne["justify"] = "center"
# setting text
btnOne["text"] = "1"
# click event
btnOne["command"] = lambda: click(1)
# positing  the button in the panel
btnOne.place(relx=0.3, rely=0.3, anchor="n",width=70,height=25)

# Button Two
btnTwo = tk.Button(root)
# background color
btnTwo["bg"] = "#efefef"
# adding the fonts
ft = tkFont.Font(family='Arial', size=10)
btnTwo["font"] = ft
# foreground color
btnTwo["fg"] = "#000000"
# text alignment
btnTwo["justify"] = "center"
# setting text
btnTwo["text"] = "2"
# click event
btnTwo["command"] = lambda: click(2)
# positing  the button in the panel
btnTwo.place(relx=0.4, rely=0.3, anchor="n",width=70,height=25)

# Button Three
btnThree = tk.Button(root)
# background color
btnThree["bg"] = "#efefef"
# adding the fonts
ft = tkFont.Font(family='Arial', size=10)
btnThree["font"] = ft
# foreground color
btnThree["fg"] = "#000000"
# text alignment
btnThree["justify"] = "center"
# setting text
btnThree["text"] = "3"
# click event performed
btnThree["command"] = lambda: click(3)
# positing  the button in the panel
btnThree.place(relx=0.5, rely=0.3, anchor="n",width=70,height=25)

# Button Four
btnFour = tk.Button(root)
# background color
btnFour["bg"] = "#efefef"
# adding the fonts
ft = tkFont.Font(family='Arial', size=10)
btnFour["font"] = ft
# foreground color
btnFour["fg"] = "#000000"
# text alignment
btnFour["justify"] = "center"
# setting text
btnFour["text"] = "4"
# click event performed
btnFour["command"] = lambda: click(4)
# positing  the button in the panel
btnFour.place(relx=0.6, rely=0.3, anchor="n",width=70,height=25)

# Button Five
btnFive = tk.Button(root)
# background color
btnFive["bg"] = "#efefef"
# adding the fonts
ft = tkFont.Font(family='Arial', size=10)
btnFive["font"] = ft
# foreground color
btnFive["fg"] = "#000000"
# text alignment
btnFive["justify"] = "center"
# setting text
btnFive["text"] = "5"
# click event performed
btnFive["command"] = lambda: click(5)
# positing  the button in the panel
btnFive.place(relx=0.7, rely=0.3, anchor="n",width=70,height=25)

root.mainloop()
