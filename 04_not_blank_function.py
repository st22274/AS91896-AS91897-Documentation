from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def validate_selection():
    selection = combobox.get()
    if selection == "":
        messagebox.showerror("Error", "Please select an item hired.")
    else:
        return True

root = tk.Tk()

combobox = ttk.Combobox(root, values=["Plates", "Tables", "LED twinkle lights"])
combobox.pack()

button = tk.Button(root, text="Save", command=validate_selection)
button.pack()

root.geometry("400x400")
root.mainloop()