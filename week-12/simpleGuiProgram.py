import tkinter as tk
from tkinter import filedialog, messagebox


def showMessage():
    messagebox.showinfo("Message", "Hello Student")


def openFile():
    filePath = filedialog.askopenfilename()
    if filePath:
        resultLabel.config(text=filePath)


def showItem(event):
    selectedItem = listBox.get(tk.ACTIVE)
    resultLabel.config(text="Selected: " + selectedItem)


def showColor(color):
    resultLabel.config(text="Color: " + color)


root = tk.Tk()
root.title("Simple GUI Program")
root.geometry("400x300")

menuBar = tk.Menu(root)
fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Message", command=showMessage)
menuBar.add_cascade(label="File", menu=fileMenu)
root.config(menu=menuBar)

listFrame = tk.Frame(root)
listFrame.pack(pady=10)

scrollbar = tk.Scrollbar(listFrame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listBox = tk.Listbox(listFrame, height=5, yscrollcommand=scrollbar.set)
for item in ["Apple", "Mango", "Orange", "Grapes", "Banana"]:
    listBox.insert(tk.END, item)
listBox.pack(side=tk.LEFT)
listBox.bind("<<ListboxSelect>>", showItem)

scrollbar.config(command=listBox.yview)

menuButton = tk.Menubutton(root, text="Choose Color", relief=tk.RAISED)
menuButton.pack(pady=10)

colorMenu = tk.Menu(menuButton, tearoff=0)
colorMenu.add_command(label="Red", command=lambda: showColor("Red"))
colorMenu.add_command(label="Blue", command=lambda: showColor("Blue"))
colorMenu.add_command(label="Green", command=lambda: showColor("Green"))
menuButton.config(menu=colorMenu)

resultLabel = tk.Label(root, text="Select an item")
resultLabel.pack(pady=20)

root.mainloop()
