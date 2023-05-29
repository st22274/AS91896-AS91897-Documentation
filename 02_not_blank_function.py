from tkinter import *
import tkinter as tk
from tkinter import messagebox
import re

def validate_name():
    name = name_entry.get()

    # Check if the name is not blank
    if not name.strip():
        messagebox.showerror("Error", "Customer Name cannot be blank.")
        return False

    # Check if the name contains only letters
    if not re.match(r'^[a-zA-Z\s]+$', name):
        messagebox.showerror("Error", "Customer Name can only contain letters.")
        return False

    # Name is valid
    return True

def submit():
    if validate_name():
        # Perform further actions with the valid name
        print("Name is valid:", name_entry.get())

root = tk.Tk()

# Create a name entry widget
name_entry = tk.Entry(root)
name_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()


root.geometry('400x400')
root.mainloop()