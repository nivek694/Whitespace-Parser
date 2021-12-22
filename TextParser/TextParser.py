
import tkinter 
from tkinter import ttk
import pyperclip
import re
global inputText, outputText

'''
Removes all newline characters and reconnects all words that are split by a -
'''
def parseText(text : str) -> str:
    text = re.sub("\S-\n", "", text)
    text = text.replace("\n", " ")
    return text

'''
Copys the text in inputText, removes all newline characters and reconnects all words that are split by a -, and
pastes this into outputText
'''
def processTextBox():
    global outputText
    outputText.delete("1.0", tkinter.END)
    print("processTextBox")
    inp = inputText.get("1.0", 'end-1c')
    print(inp)
    output = parseText(inp)
    print(output)
    outputText.insert(tkinter.INSERT, output)

'''Copies the contents of outputText to the clipboard'''
def copyToClipboard():
    text = outputText.get("1.0", tkinter.END)
    pyperclip.copy(text)


root =tkinter.Tk()
root.geometry("800x600")

frm = ttk.Frame(root, padding=10)

frm.grid()
inputText = tkinter.Text(frm, height = 10, width= 20)
inputText.grid(column = 0, row = 1)

outputText = tkinter.Text(frm, height = 10, width= 20)
outputText.grid(column = 1, row = 1)
#ttk.Text
ttk.Label(frm, text="Enter input on left, get output on right").grid(column=0, row=0)
ttk.Button(frm, text="Process", command=processTextBox).grid(column=1, row=0)
ttk.Button(frm, text="Copy to clipbord", command=copyToClipboard).grid(column=1, row=2)
root.mainloop()