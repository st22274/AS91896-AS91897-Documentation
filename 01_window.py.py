from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

root=Tk()

root.title("Julie's Party Hire")
root.geometry('800x400')

# FUNCTIONS
def delete():
    selected_item = set.selection()[0] ## get selected item
    set.delete(selected_item)


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

def submit():
    if validate_name() and validate_receipt_number():
        input_record()

def add_button():
    validate_name()
    validate_receipt_number()
    submit()
    

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

lblname = Label(Input_frame,text="Customer Name")
lblname.grid(row=2,column=0)

lblreceipt= Label(Input_frame,text="Receipt Number")
lblreceipt.grid(row=2,column=1)

lblitem= Label(Input_frame,text="Item Hired")
lblitem.grid(row=3,column=2)

lblnum = Label(Input_frame, text="No. of Hired Item")
lblnum.grid(row=2,column=3)

lblemail  = Label(Input_frame, text="Email Address")
lblemail.grid(row=2, column=4)

# ENTIRES
lblname_entry = Entry(Input_frame)
lblname_entry.grid(row=3,column=0)

lblreceipt_entry = Entry(Input_frame)
lblreceipt_entry.grid(row=3,column=1)

lblnum_entry = Entry(Input_frame)
lblnum_entry.grid(row=3, column=3)

lblemail_entry = Entry(Input_frame)
lblemail_entry.grid(row=3, column=4)


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
Input_button = Button(root,text = "Add to list",command = add_button)

Input_button.pack()


# SETS
set = ttk.Treeview(root)
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



# BUTTONS UNDER TREEVIEW
delete_button = Button(root, text = "Delete Row", command = delete)

delete_button.pack()



root.mainloop()