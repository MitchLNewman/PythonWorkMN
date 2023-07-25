#Imports for GUI and variable for GUI window
import tkinter
from tkinter import filedialog
root = tkinter.Tk()

#Title and dimensions of interface window
root.title("File Reader")
root.geometry("500x450")

def readFile():
    with open(input1.get(), "r") as file:
        for index, line in enumerate(file):
            tkinter.Label(root, text = f"{index + 1}: {line}").grid(row = index + 2, column = 1) 

# command for text box to appear in window 
input1 = tkinter.Entry(root)
input1.grid(row=1, column=1)

# command for adding a read file button to the the GUI Window 
submit = tkinter.Button(root, text = "Read File", command = readFile)
submit.grid(row=1, column=2)

# if statement stops commands from being executed automatically 
if __name__ == "__main__":
    root.mainloop()