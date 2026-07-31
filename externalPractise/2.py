import tkinter as tk


root = tk.Tk()
root.geometry("500x500")
root.title("checkbox and radiobutton")


def show():
    res = rch.get()
    resLabel.config(text = res + str(v1.get()) + str(v2.get()) + str(v3.get()))

    
 
rch = tk.StringVar()
rch.set("Male")


m = tk.Radiobutton(root,value="Male",text = "Male",variable=rch)
m.grid(row = 0,column=0)
f = tk.Radiobutton(root,value="Female",text = "Female",variable=rch)
f.grid(row = 1,column=0)
t = tk.Radiobutton(root,value="trans",text = "Trans",variable=rch)
t.grid(row = 2,column=0)

v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()

a = tk.Checkbutton(root,text="apple",variable=v1)
a.grid(row = 3,column=0)
b = tk.Checkbutton(root,text="Banana",variable=v2)
b.grid(row = 4,column=0)
c = tk.Checkbutton(root,text="Mango",variable=v3)
c.grid(row = 5,column=0)




btn = tk.Button(root,text = "Show",command=show)
btn.grid(row=6, column=0)


resLabel = tk.Label(root,text = "result will be displaayed here")
resLabel.grid(row=6, column=1)






root.mainloop()