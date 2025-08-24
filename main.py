from tkinter import * #creating GUI 
import tkinter as tk
from tkinter.filedialog import asksaveasfilename # filedialog for creating files

#create main window
main_window = Tk()
main_window.geometry("600x600")
main_window.title("editorz")

text_area = tk.Text(main_window, wrap="word", undo=True)
text_area.pack(expand=1, fill="both")



main_window.mainloop()