# parent function for GUI 
import tkinter

# function to call to strip vowels from text box when user enters a message
def stripVowels():
    global label
    label.destroy()
    string = input1.get()
    label = tkinter.Label(root, text = ''.join(char for char in string if char not in 'aeiouAEIOU'))

# command for the GUI window
root = tkinter.Tk()

# commands for adding a label and text box to GUI
label = tkinter.Label(root, text = "")
input1 = tkinter.Entry(root)
input1.grid(row=1, column=1)

# commands for adding a submittable button to GUI
submit = tkinter.Button(root, text = "Strip Vowels", command = stripVowels)
submit.grid(row=1, column=2)

# Statement to avoid statements being automatically executed during process 
if __name__ == "__main__":
    root.mainloop()



