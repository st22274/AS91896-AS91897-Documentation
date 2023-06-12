from tkinter import *
import tkinter as ttk

root = Tk()
root.geometry("400x400")

def close():
    root.destroy()
    root.quit()
    
exit_button = Button(text = "Exit", comman = close)
exit_button.pack()

root.mainloop()