import tkinter as tk

def showText():
    outputLabel.config(text="Hello " + nameEntry.get())

root = tk.Tk()
root.title("Label Entry Button")
root.geometry("300x300")

nameLabel = tk.Label(root, text="Enter your name:")
nameLabel.pack()

nameEntry = tk.Entry(root)
nameEntry.pack()

showButton = tk.Button(root, text="Show", command=showText)
showButton.pack()

outputLabel = tk.Label(root, text="")
outputLabel.pack()

root.mainloop()
