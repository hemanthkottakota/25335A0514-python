import tkinter as tk

root = tk.Tk()
root.title("Geometry Methods")
root.geometry("400x250")

packLabel = tk.Label(root, text="This uses pack()", bg="lightblue")
packLabel.pack(pady=10)

gridLabel = tk.Label(root, text="Name:")
gridLabel.place(x=20, y=70)

gridEntry = tk.Entry(root)
gridEntry.place(x=80, y=70)

placeButton = tk.Button(root, text="This uses place()")
placeButton.place(x=120, y=140)

root.mainloop()
