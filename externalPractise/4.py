import tkinter as tk

root = tk.Tk()
root.title("Listbox with Scrollbar")
root.geometry("300x300")

# Function to show selected item
def show():
    selected = listbox.get(listbox.curselection())
    label.config(text="Selected: " + selected)

# Create Listbox
listbox = tk.Listbox(root, height=10)

# Insert items
items = ["Python", "Java", "C", "C++", "JavaScript",
         "HTML", "CSS", "SQL", "React", "Node"]

for item in items:
    listbox.insert(tk.END, item)

# Create Scrollbar
scrollbar = tk.Scrollbar(root)

# Link Listbox and Scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Pack widgets
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Button to display selection
btn = tk.Button(root, text="Show Selected", command=show)
btn.pack(pady=10)

# Label to display output
label = tk.Label(root, text="")
label.pack()

root.mainloop()