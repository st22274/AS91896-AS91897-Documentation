from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
from tkinter.ttk import Treeview
from tkinter import Frame
import tkinter.font as font

root=Tk()

# FONTS
title_font = font.Font(family="MV Boli", size=15, weight = "bold")
font2 = font.Font(family="MV Boli", size=10)

root.title("Julie's Party Hire")
root.geometry('800x450')



# FUNCTIONS
def input_record():
    
    global count
   
    set.insert(parent='',index='end',iid = count,text='',values=(lblname_entry.get(),lblreceipt_entry.get(),lblitem_entry.get(), lblnum_entry.get(), lblemail_entry.get()))
    count += 1

   
    lblname_entry.delete(0,END)
    lblreceipt_entry.delete(0,END)
    lblitem_entry.delete(0,END)
    lblnum_entry.delete(0,END)
    lblemail_entry.delete(0,END)
    
def validate_name():
    name = lblname_entry.get()

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


def validate_receipt_number():
    receipt_number = lblreceipt_entry.get()

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

def validate_selection():
    selection = combobox.get()
    if selection == "":
        messagebox.showerror("Error", "Please select an item hired.")
    else:
    # Item Hired is selected 
        return True

def validate_number():
    try:
        number = int(lblnum_entry.get())
        if number < 1 or number > 500:
            raise ValueError
        return True
    except ValueError:
        messagebox.showerror("Error", "Please enter a number of hired item between 1 and 500.")


def validate_email():
    email = lblemail_entry.get()
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")

def delete_key(event):
    selected_item = set.selection()

    if selected_item:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this row?")
        
        if confirmation:
            set.delete(selected_item)

# Bind the delete event to the delete_key function
root.bind_class('Treeview', '<Delete>', delete_key)
            
def delete_button():
    selected_item = set.selection()

    if selected_item:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this row?")
        
        if confirmation:
            set.delete(selected_item)

def submit():
    if validate_name() and validate_receipt_number() and validate_selection() and validate_number() and validate_email():
        input_record()

def add_button():
    submit()

def search(event):
    set.selection_remove(set.get_children())

    # The search query from the entry widget
    query = search_entry.get().lower()

    # Iterate over the items in the Treeview
    for item in set.get_children():
        item_values = set.item(item)['values']
        if any(query in str(value).lower() for value in item_values):
            set.selection_add(item)


def close():
    root.destroy()
    root.quit()

# DATA
data  = []

global count
count=0
    
for record in data:
      
    set.insert(parent='',index='end',iid = count,text='',values=(record[0],record[1],record[2], record[3], record[4]))
       
    count += 1

Input_frame = Frame(root)
Input_frame.pack()

# LABELS
lbltitle = Label(Input_frame, text="Julie's Party Hire")
lbltitle.grid(row=0, column=2)
lbltitle['font'] = title_font

lblname = Label(Input_frame,text="Customer Name")
lblname.grid(row=3,column=0)
lblname['font'] = font2

lblreceipt= Label(Input_frame,text="Receipt Number")
lblreceipt.grid(row=3,column=1)
lblreceipt['font'] = font2

lblitem= Label(Input_frame,text="Item Hired")
lblitem.grid(row=4,column=2)
lblitem['font'] = font2

lblnum = Label(Input_frame, text="No. of Hired Item")
lblnum.grid(row=3,column=3)
lblnum['font'] = font2

lblemail  = Label(Input_frame, text="Email Address")
lblemail.grid(row=3, column=4)
lblemail['font'] = font2

# ENTIRES
lblname_entry = Entry(Input_frame)
lblname_entry.grid(row=4,column=0)

lblreceipt_entry = Entry(Input_frame)
lblreceipt_entry.grid(row=4,column=1)

lblnum_entry = Entry(Input_frame)
lblnum_entry.grid(row=4, column=3)

lblemail_entry = Entry(Input_frame)
lblemail_entry.grid(row=4, column=4)


def on_select(event):
    selected_value = combobox.get()
    lblitem_entry.delete(0, END)  # Clear the entry widget
    lblitem_entry.insert(0, selected_value)  # Insert selected value into the entry widget


# Create a combobox
items = ['Plates', 'Chairs', 'Tables', 'Hats', 'Signs', 'Toys', 'Bouncy Castle', 'Party Games', 'Rug','LED Twinkle Lights']
combobox = ttk.Combobox(root, values=items)
combobox.pack()

# Create an entry widget
lblitem_entry = Entry(root)

lblitem_entry.pack()

combobox.bind('<<ComboboxSelected>>', on_select)

# BUTTONS OVER TREEVIEW
Input_button = Button(root,text = "Add", bg = "lightcyan", command = add_button, width = 10)
Input_button['font'] = font2
Input_button.pack()


# SETS
set = Treeview(root)
set.pack()

set['columns']= ('Customer Name', 'Receipt Number','Item Hired', 'No. of Hired Item', 'Email Address')
set.column("#0", width=0,  stretch=NO)
set.column("Customer Name",anchor=CENTER, width=100)
set.column("Receipt Number",anchor=CENTER, width=100)
set.column("Item Hired",anchor=CENTER, width=100)
set.column("No. of Hired Item",anchor=CENTER, width=100)
set.column("Email Address",anchor=CENTER, width=100)

set.heading("#0",text="",anchor=CENTER)
set.heading("Customer Name",text="Customer Name",anchor=CENTER)
set.heading("Receipt Number",text="Receipt Number",anchor=CENTER)
set.heading("Item Hired",text="Item Hired",anchor=CENTER)
set.heading("No. of Hired Item", text="No. of Hired Item", anchor=CENTER)
set.heading("Email Address", text="Email Address", anchor=CENTER)


# Entry for search bar
search_entry = Entry(root)
search_entry.pack()

search_entry.bind('<KeyRelease>', search)

# BUTTONS UNDER TREEVIEW
delete_button = Button(root, text = "Delete", bg = "lightpink", command = delete_button, width = 10)
delete_button['font'] = font2
delete_button.pack()

exit_button = Button(text = "Exit", bg = "lightgray", command = close, width = 10)
exit_button['font'] = font2
exit_button.pack()


root.mainloop()