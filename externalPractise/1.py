import tkinter as tk
import math
# root = tk.Tk()
# root.title("Hello World")
# root.geometry("300x200")

# def show():
#     # b.config(tk.END,0)
#     res.delete(0, tk.END)
#     res.insert(0,b.get())
#     l.config(text = "you clicked"+b.get())
    

# tk.Label(root ,text = "Hello World").pack()


# tk.Button(root,text="sumbit" ,command=show).pack()
# b = tk.Entry(root)
# b.pack()
# l = tk.Label(root)
# l.pack()

# res = tk.Entry(root)
# res.pack()

# root.mainloop()



parent = tk.Tk()
parent.title("factorial")
parent.geometry("300x300")


def fact():
    res = str(math.factorial(int(inp.get())))
    resultLabel.config(text = res)
    resultEntry.delete(0,tk.END)
    resultEntry.insert(0,res)
    

lb = tk.Label(parent,text = "enter a number:")
lb.grid(row=0, column=0)
inp = tk.Entry(parent)
inp.grid(row=0,column=1)

resultLabel = tk.Label(parent,text = "your result is displayed here")
resultLabel.grid(row = 2,column=0)


resultEntry = tk.Entry(parent)
resultEntry.grid(row=2,column=1)

but = tk.Button(parent,text = "submit",command=fact)
but.grid(row=1,column=0)

parent.mainloop()
