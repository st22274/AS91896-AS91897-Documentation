from tkinter import *
import tkinter as tk
from tkinter import messagebox

def validate_receipt_number():
    receipt_number = receipt_entry.get()

    # Check if the receipt number is exactly 6 digits
    if len(receipt_number) != 6:
        messagebox.showerror("Error", "Receipt number should be 6 digits.")
        return False

    # Check if the receipt number consists only of digits
    if not receipt_number.isdigit():
        messagebox.showerror("Error", "Receipt number should contain only digits.")
        return False

    # Receipt number is valid
    return True

def submit():
    if validate_receipt_number():
        # Perform further actions with the valid receipt number
        print("Receipt number is valid:", receipt_entry.get())

root = tk.Tk()

receipt_entry = tk.Entry(root)
receipt_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()