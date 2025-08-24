from tkinter import * #creating GUI 
import tkinter as tk
from tkinter import filedialog # filedialog for creating files

#create main window
main_window = Tk()
main_window.geometry("600x600")
main_window.title("editorz")

scrollbar = tk.Scrollbar(main_window)
scrollbar.pack(side="right", fill="y")

text_area = tk.Text(main_window, yscrollcommand=scrollbar.set)
text_area.pack(expand=1, fill="both")

scrollbar.config(command=text_area.yview)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("text files", "*.txt"), ("all files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete("1.0", END)
            text_area.insert("1.0", file.read())


open_button = tk.Button(main_window, text="Open File", command=open_file)
open_button.pack()

main_window.mainloop()