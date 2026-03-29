import tkinter as tk


def showChoice():
    games = "Cricket" if cricketVar.get() else "No Cricket"
    color = colorVar.get()
    resultLabel.config(text=f"{games}, Favorite color: {color}")


root = tk.Tk()
root.title("Checkbutton and Radiobutton")
root.geometry("320x250")

cricketVar = tk.IntVar()
colorVar = tk.StringVar(value="Red")

tk.Checkbutton(root, text="I like Cricket", variable=cricketVar).pack(pady=5)

tk.Label(root, text="Choose a color:").pack()
tk.Radiobutton(root, text="Red", variable=colorVar, value="Red").pack()
tk.Radiobutton(root, text="Blue", variable=colorVar, value="Blue").pack()
tk.Radiobutton(root, text="Green", variable=colorVar, value="Green").pack()

tk.Button(root, text="Show", command=showChoice).pack(pady=10)

resultLabel = tk.Label(root, text="")
resultLabel.pack()

root.mainloop()
