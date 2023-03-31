import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Selecciona un elemento:")

listbox = tk.Listbox(root)
listbox.insert(1, "Elemento 1")
listbox.insert(2, "Elemento 2")
listbox.insert(3, "Elemento 3")

label.pack()
listbox.pack()

root.mainloop()
