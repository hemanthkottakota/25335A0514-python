import tkinter as tk

root = tk.Tk()
root.title("Menu Example")
root.geometry("300x200")

# # Create menu bar
# menubar = tk.Menu(root)

# # Create File menu
# file_menu = tk.Menu(menubar, tearoff=0)

# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)

# # Add File menu to menubar
# menubar.add_cascade(label="File", menu=file_menu)

# # Attach menu bar to window
# root.config(menu=menubar)

# root.mainloop()


menubar = tk.Menu(root)

fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="open")
fileMenu.add_command(label="edit")
fileMenu.add_command(label="exit",command=root.quit)
fileMenu.add_separator()
menubar.add_cascade(label="file", menu=fileMenu)



helpMenu = tk.Menu(menubar)
helpMenu.add_command(label="hi", )
helpMenu.add_command(label="hello",)
menubar.add_cascade(label="help", menu=helpMenu)



root.config(menu=menubar)
root.mainloop()



# # import tkinter as tk

# # root = tk.Tk()
# # root.title("Menubutton Example")
# # root.geometry("300x200")

# # Create menubutton
# mb = tk.Menubutton(root, text="Options", relief="raised")

# # Create menu for button
# menu = tk.Menu(mb)

# menu.add_command(label="Option 1")
# menu.add_command(label="Option 2")

# # Attach menu to button
# mb.config(menu=menu)

# mb.pack()

# root.mainloop()