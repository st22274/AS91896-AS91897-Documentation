from tkinter import Tk, Frame, Entry
from tkinter.ttk import Treeview

def search(event):
    set.selection_remove(set.get_children())

    # Get the search query from the entry widget
    query = entry.get()

    # Iterate over the items in the Treeview
    for item in set.get_children():
        item_text = set.item(item)['text']
        if query.lower() in item_text.lower():
          set.selection_add(item)

root = Tk()

# Frame widget
frame = Frame(root)
frame.pack()

# Entry widget for the search bar
entry = Entry(frame)
entry.pack()

set = Treeview(frame)
set.pack()

set.insert('', 'end', text="Item 1")
set.insert('', 'end', text="Item 2")
set.insert('', 'end', text="Item 3")


entry.bind('<KeyRelease>', search)


root.mainloop()