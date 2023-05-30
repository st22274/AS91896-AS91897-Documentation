import tkinter as tk
from tkinter import messagebox

def validate_number():
    try:
        number = int(entry.get())
        if number < 1 or number > 500:
            raise ValueError
        return True
    except ValueError:
        messagebox.showerror("Error", "Please enter a number of hired item between 1 and 500.")

root = tk.Tk()

label = tk.Label(root, text="No. of Item Hired:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=validate_number)
button.pack()

root.geometry("400x400")
root.mainloop()