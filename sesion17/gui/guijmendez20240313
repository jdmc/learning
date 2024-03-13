import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Lógica para agregar una nueva tarea >>>> PROBANDO 1 2 3 TEST"
def agregar_tarea():
    # Obtener los valores ingresados por el usuario
    descripcion = entry_descripcion.get()
    fecha_vencimiento = entry_fecha.get()
    prioridad = entry_prioridad.get()

    # Validar que se haya ingresado una descripción
    if not descripcion:
        messagebox.showerror("Error", "Por favor, ingresa una descripción para la tarea.")
        return     # Agregar la tarea a la lista (puedes usar una lista o una base de datos

    print(f"Tarea agregada:\nDescripción: {descripcion}\nFecha de vencimiento: {fecha_vencimiento}\nPrioridad: {prioridad}")

    # Limpiar los campos de entrada después de agregar la tarea
    entry_descripcion.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_prioridad.delete(0, tk.END)


def marcar_completada():
    # Lógica para marcar una tarea como completada
    pass

def eliminar_tarea():
    # Lógica para eliminar una tarea
    pass

# Crear la ventana principal
root = tk.Tk()
root.geometry("300x300")
root.title("Task Manager; Gestión de Tareas")

# Widgets
label_descripcion = tk.Label(root, text="Descripción:")
entry_descripcion = tk.Entry(root)

label_fecha = tk.Label(root, text="Fecha de vencimiento:")
entry_fecha = tk.Entry(root)

label_prioridad = tk.Label(root, text="Prioridad:")
entry_prioridad = tk.Entry(root)

boton_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea, bg="green", fg="white",padx=3, pady=3)
boton_completada = tk.Button(root, text="Marcar como Completada", command=marcar_completada,padx=3, pady=3)
boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea, bg="red", fg="white", padx=3, pady=3)

# Posicionamiento de widgets
label_descripcion.grid(row=0, column=0, pady=10)
entry_descripcion.grid(row=0, column=1, pady=10)

label_fecha.grid(row=1, column=0, pady=10)
entry_fecha.grid(row=1, column=1, pady=10)

label_prioridad.grid(row=2, column=0, pady=10)
entry_prioridad.grid(row=2, column=1, pady=10)


boton_agregar.grid(row=3, column=0, columnspan=2,padx=10, pady=5)
boton_completada.grid(row=4, column=0, columnspan=2,padx=10, pady=5)
boton_eliminar.grid(row=5, column=0, columnspan=2,padx=10, pady=5)

# Ejecutar la aplicación
root.mainloop()
