import tkinter as tk
from tkinter import ttk


def saludar():
    print(f"Hola {nombre_usuario.get()}")

root = tk.Tk()
root.geometry("300x200")
root.title("Python Session GUI")


nombre_label = ttk.Label(root, text="Nombre:")
nombre_label.pack(side="left", padx=(0,10))

nombre_usuario = tk.StringVar()
nombre_texto = ttk.Entry(root, width=20, textvariable=nombre_usuario)
nombre_texto.pack(side="left")

#boton_saludar = ttk.Button(root, text="Saludar", command=lambda: print("Hola mundo"))
boton_saludar = ttk.Button(root, text="Saludar", command=saludar)
boton_saludar.pack(side="left", fill="x", expand=True)

boton_salir = ttk.Button(root, text="Salir", command=root.destroy)
boton_salir.pack(side="left", fill="x", expand=True)

root.mainloop()