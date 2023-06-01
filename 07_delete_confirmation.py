from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import tkinter as ttk

def delete_key(event):
    selected_item = set.selection()

    if selected_item:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this item?")
        
        if confirmation:
            set.delete(selected_item)
            
def delete_button():
    selected_item = set.selection()

    if selected_item:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this row?")
        
        if confirmation:
            set.delete(selected_item)

root = Tk()

set = Treeview(root)
set.pack()

delete_button = ttk.Button(root, text="Delete", command=delete_button)
delete_button.pack()
# Bind the delete event to the delete_key function
set.bind('<Delete>', delete_key)

# Items for demonstration
set.insert('', 'end', text="Item 1")
set.insert('', 'end', text="Item 2")
set.insert('', 'end', text="Item 3")

root.geometry("400x400")
root.mainloop()