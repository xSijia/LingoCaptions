# This is a sample Python script.
from functions import *

master = Tk()
master.title('LingoCaptions')

# sets the geometry of main
# root window
master.geometry("220x300")

# function to open a new window
# on a button click


label = Label(master,
              text="Select Languages")
label.pack(pady=10)

source = loadSourceDropDown(master)
frame = tk.Frame(master)
frame.pack()
outputs = []


def loadOutDropDownAndPushOutputs():
    output = loadOutDropDown(frame)
    outputs.append(output)


def loadOutDropDownAndPushOutputsEng():
    output = loadOutDropDownEng(frame)
    outputs.append(output)


loadOutDropDownAndPushOutputsEng()
addOutputBtn = Button(master,
                      text="Add an output",
                      command=loadOutDropDownAndPushOutputs)
addOutputBtn.pack()
"""
fontLabel = Label(master, text="Choose Font Size")
fontLabel.pack()
textFrame = Frame(master)
buttonExample1 = tk.Button(textFrame, text="small", width=3)
buttonExample1.pack(side=LEFT)
buttonExample2 = tk.Button(textFrame, text="mid", width=3)
buttonExample2.pack(side=LEFT)
buttonExample3 = tk.Button(textFrame, text="large", width=3)
buttonExample3.pack(side=LEFT)
textFrame.pack()
"""
loadRomanCheckbox(master)

"""listenbtn = Button(master,
                   text="Start Listening",
                   command=lambda: threading(source, outputs))
listenbtn.pack(pady=5)"""

loadListenCheckbox(master,
                   lambda: threading(source, outputs))

# a button widget which will open a
# new window on button click
captionbtn = Button(master,
                    text="Generate Caption",
                    command=lambda: openNewCapWindow(outputs, master))
captionbtn.pack(pady=5)
# mainloop, runs infinitely
print(resJSON)

mainloop()
