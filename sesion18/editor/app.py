import os
import tkinter as tk
from tkinter import ttk

def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    
    notebook.add(text_area, text="Nuevo")
    
def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        file_name = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        
        text = text_widget.get("1.0", "end-1c")
        
        with open(file_name, "w") as file:
            file.write(text)
            
    except (AttributeError, FileNotFoundError):
        print("Guardado cancelado")
    

root = tk.Tk()
root.geometry("300x300")
root.title("Editor de texto")

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=(1), pady=(4,0))

#crear menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

#crear opcion en menu
file_menu.add_command(label="Nuevo", command=create_file)
file_menu.add_command(label="Guardar", command=save_file)

#creacion del notebook
notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()

root.mainloop()
