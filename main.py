from tkinter import * #creating GUI 
import tkinter as tk
from tkinter.filedialog import asksaveasfilename # filedialog for creating files

#create main window
main_window = Tk()
main_window.geometry("600x600")
main_window.title("editorz")

scrollbar = tk.Scrollbar(main_window)
scrollbar.pack(side="right", fill="y")

text_area = tk.Text(main_window, yscrollcommand=scrollbar.set)
text_area.pack(expand=1, fill="both")

scrollbar.config(command=text_area.yview)



main_window.mainloop()