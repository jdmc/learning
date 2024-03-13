import os
import tkinter as tk
from tkinter import ttk

def create_file(content="", title="Sin titulo"):
    text_area = tk.Text(notebook)
    text_area.insert("end", content)
    text_area.pack(fill="both", expand=True)
    
    notebook.add(text_area, text=title)
    notebook.select(text_area)

def open_file():
    file_path = filedialog.askopenfilename()
    try:
        file_name = os.path.basename(file_path)
        with open(file_path, "r") as file:
            text = file.read()

    except (AttributeError, FileNotFoundError):
        print("Carga cancelada")
        return
    
    create_file(content=text, title=file_name)
    
def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        file_name = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        
        text = text_widget.get("1.0", "end-1c")
        
        with open(file_path, "w") as file:
            file.write(text)
            
    except (AttributeError, FileNotFoundError):
        print("Guardado cancelado")
        return
    
    notebook.tab("current", text=file_name)

root = tk.Tk()
root.geometry("300x300")
root.title("Editor de texto")
root.option_add("tearOff", False)

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=(1), pady=(4,0))

#crear menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

#crear opcion en menu
file_menu.add_command(label="Nuevo", command=create_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)


#creacion del notebook
notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()

root.mainloop()
