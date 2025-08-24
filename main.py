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


#save-file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text files", "*.txt"), ("all files", "*.*")])
    if file_path:
        with open (file_path, "w") as file:
            file.write(text_area.get("1.0", END))

#new file
def new_file():
    text_area.delete("1.0", END)


#buttons - open, save, new
open_button = tk.Button(main_window, text="Open File", command=open_file)
open_button.pack()

save_button = tk.Button(main_window, text = "save file", command=save_file)
save_button.pack()

new_button = tk.Button(main_window, text="new file", command = new_file)
new_button.pack()



# key-bindings
main_window.bind("<Control-o>", lambda event: open_file())
main_window.bind("<Control-s>", lambda event: save_file())
main_window.bind("<Control-n>", lambda event : new_file())


#menu
menu_bar = tk.Menu(main_window)
file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label="open", command= open_file)
file_menu.add_command(label="save", command = save_file)
file_menu.add_command(label="new", command= new_file)
file_menu.add_separator()
file_menu.add_command(label="exit", command= main_window.quit)


menu_bar.add_cascade(label="file", menu = file_menu)
main_window.config(menu=menu_bar)





main_window.mainloop()