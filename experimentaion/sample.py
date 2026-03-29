import tkinter as tk

root = tk.Tk()
root.title("Menu Example")

# ---------------- MENU BAR ----------------
menubar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

menubar.add_cascade(label="Edit", menu=edit_menu)

# Display menu
root.config(menu=menubar)

# ---------------- MENUBUTTON ----------------
mb = tk.Menubutton(root, text="Options", relief="raised")
mb.pack(pady=20)

mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1")
mb.menu.add_command(label="Option 2")
mb.menu.add_command(label="Option 3")

root.mainloop()