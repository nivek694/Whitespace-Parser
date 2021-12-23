
import PyInstaller
import tkinter 
from tkinter import ttk
import pyperclip
import re
global inputText, outputText

'''
Removes all newline characters and reconnects all words that are split by a -
'''
def parseText(text : str) -> str:
    
    pattern = re.findall("\S-\n", text)
    for i in pattern:
        text = re.sub(i, i[0], text)
    
    
    text = text.replace("\n", " ")
    return text

'''
Copys the text in inputText, removes all newline characters and reconnects all words that are split by a -, and
pastes this into outputText
'''
def processTextBox():
    global inputText
    #print("processTextBox")
    inp = inputText.get("1.0", 'end-1c')
    inputText.delete("1.0", tkinter.END)
    #print(inp)
    output = parseText(inp)
    #print(output)
    inputText.insert(tkinter.INSERT, output)

'''Copies the contents of outputText to the clipboard'''
def copyToClipboard():
    text = inputText.get("1.0", tkinter.END)
    pyperclip.copy(text)


root =tkinter.Tk()
root.geometry("800x600")

frm = ttk.Frame(root, padding=10)

frm.grid()
inputText = tkinter.Text(frm, height = 20, width= 40)
inputText.grid(column = 0, row = 1)

#outputText = tkinter.Text(frm, height = 20, width= 40)
#outputText.grid(column = 1, row = 1)
#ttk.Text
ttk.Button(frm, text="Process", command=processTextBox).grid(column=0, row=0)
ttk.Button(frm, text="Copy to clipbord", command=copyToClipboard).grid(column=0, row=2)
root.mainloop()