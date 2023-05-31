import re
import tkinter as tk
from tkinter import messagebox

def validate_email():
    email = email_entry.get()
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")

root = tk.Tk()

email_entry = tk.Entry(root)
email_entry.pack()

validate_button = tk.Button(root, text="Validate", command=validate_email)
validate_button.pack()

root.geometry("400x400")
root.mainloop()




