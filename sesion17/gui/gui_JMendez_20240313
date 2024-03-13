""" 
Desarrolla una aplicación de gestión de tareas con interfaz gráfica utilizando Tkinter en Python. 
La aplicación debe permitir al usuario agregar nuevas tareas con una descripción, fecha de vencimiento y prioridad. 
Además, debería ser posible marcar las tareas como completadas y eliminarlas. 
Asegúrate de proporcionar una interfaz intuitiva y agradable para una experiencia de usuario óptima. """

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class TaskManagerApp:
    def __init__(root):
        root = tk.Tk()
        root.title("Task Manager, gestión de tareas")

        root.tasks = []

        # Crear el frame principal
        main_frame = tk.Frame(root)
        main_frame.pack(padx=20, pady=20)

        # Etiqueta y entrada para la descripción de la tarea
        tk.Label(main_frame, text="Descripción:").grid(row=0, column=0, sticky="w")
        description_entry = tk.Entry(main_frame, width=30)
        description_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y entrada para la fecha de vencimiento
        tk.Label(main_frame, text="Fecha de Vencimiento:").grid(row=1, column=0, sticky="w")
        date_entry = tk.Entry(main_frame, width=15)
        date_entry.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y entrada para la prioridad
        tk.Label(main_frame, text="Prioridad:").grid(row=2, column=0, sticky="w")
        priority_entry = ttk.Combobox(main_frame, values=["Alta", "Media", "Baja"])
        priority_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para agregar tarea
        tk.Button(main_frame, text="Agregar Tarea", command=lambda: TaskManagerApp.add_task(root, description_entry, date_entry, priority_entry)).grid(row=3, column=0, columnspan=2, pady=10)

        # Crear el frame para la lista de tareas
        task_list_frame = tk.Frame(root)
        task_list_frame.pack(padx=20, pady=10)

        # Crear la lista de tareas
        task_listbox = tk.Listbox(task_list_frame, width=50, height=10)
        task_listbox.pack(side="left", fill="both", expand=True)

        # Scrollbar para la lista de tareas
        scrollbar = tk.Scrollbar(task_list_frame, orient="vertical")
        scrollbar.config(command=task_listbox.yview)
        scrollbar.pack(side="right", fill="y")

        task_listbox.config(yscrollcommand=scrollbar.set)

        # Botones para marcar como completada y eliminar tareas
        complete_button = tk.Button(root, text="Marcar como Completada", command=lambda: TaskManagerApp.mark_complete(root, task_listbox))
        complete_button.pack(pady=5)
        delete_button = tk.Button(root, text="Eliminar Tarea", command=lambda: TaskManagerApp.delete_task(root, task_listbox))
        delete_button.pack(pady=5)

    @staticmethod
    def add_task(root, description_entry, date_entry, priority_entry):
        description = description_entry.get()
        date_str = date_entry.get()
        priority = priority_entry.get()

        if description == "":
            messagebox.showerror("Error", "Por favor, introduce una descripción para la tarea.")
            return

        if date_str == "":
            messagebox.showerror("Error", "Por favor, introduce una fecha de vencimiento para la tarea.")
            return

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Utiliza YYYY-MM-DD.")
            return

        task = {"description": description, "date": date, "priority": priority}
        root.tasks.append(task)
        TaskManagerApp.update_task_list(root)

        # Limpiar campos de entrada después de agregar la tarea
        description_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

    @staticmethod
    def update_task_list(root):
        task_listbox = root.children[".!frame.!listbox"]

        task_listbox.delete(0, tk.END)
        for i, task in enumerate(root.tasks, start=1):
            task_listbox.insert(tk.END, f"{i}. {task['description']} - {task['date'].strftime('%Y-%m-%d')} - {task['priority']}")

    @staticmethod
    def mark_complete(root, task_listbox):
        selected_index = task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del root.tasks[index]
            TaskManagerApp.update_task_list(root)

    @staticmethod
    def delete_task(root, task_listbox):
        selected_index = task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del root.tasks[index]
            TaskManagerApp.update_task_list(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp()
    root.mainloop()
