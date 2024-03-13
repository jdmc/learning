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
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager, gestión de tareas")

        self.tasks = []

        # Crear el frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)

        # Etiqueta y entrada para la descripción de la tarea
        tk.Label(self.main_frame, text="Descripción:").grid(row=0, column=0, sticky="w")
        self.description_entry = tk.Entry(self.main_frame, width=30)
        self.description_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y entrada para la fecha de vencimiento
        tk.Label(self.main_frame, text="Fecha de Vencimiento:").grid(row=1, column=0, sticky="w")
        self.date_entry = tk.Entry(self.main_frame, width=15)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y entrada para la prioridad
        tk.Label(self.main_frame, text="Prioridad:").grid(row=2, column=0, sticky="w")
        self.priority_entry = ttk.Combobox(self.main_frame, values=["Alta", "Media", "Baja"])
        self.priority_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para agregar tarea
        tk.Button(self.main_frame, text="Agregar Tarea", command=self.add_task).grid(row=3, column=0, columnspan=2, pady=10)

        # Crear el frame para la lista de tareas
        self.task_list_frame = tk.Frame(root)
        self.task_list_frame.pack(padx=60, pady=40)

        # Crear la lista de tareas
        self.task_listbox = tk.Listbox(self.task_list_frame, width=60, height=40)
        self.task_listbox.pack(side="left", fill="both", expand=True)

        # Scrollbar para la lista de tareas
        self.scrollbar = tk.Scrollbar(self.task_list_frame, orient="vertical")
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Botones para marcar como completada y eliminar tareas
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_complete)
        self.complete_button.pack(pady=5)
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Dictionary para almacenar los checkbox asociados a cada tarea
        self.task_checkboxes = {}

    def add_task(self):
        description = self.description_entry.get()
        date_str = self.date_entry.get()
        priority = self.priority_entry.get()

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

        task = {"description": description, "date": date, "priority": priority, "completed": False}
        self.tasks.append(task)
        self.update_task_list()

        # Limpiar campos de entrada después de agregar la tarea
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        self.task_checkboxes = {}

        for i, task in enumerate(self.tasks, start=1):
            checkbox_text = f"{i}. {task['description']} - {task['date'].strftime('%Y-%m-%d')} - {task['priority']}"
            if task["completed"]:
                checkbox_text = f"\u2713 {checkbox_text}"
            self.task_checkboxes[i] = tk.BooleanVar()
            tk.Checkbutton(self.task_listbox, text=checkbox_text, variable=self.task_checkboxes[i]).grid(row=i-1, column=0, sticky="w")

    def mark_complete(self):
        for index, task in enumerate(self.tasks):
            if self.task_checkboxes[index + 1].get():
                self.tasks[index]["completed"] = True
        self.update_task_list()

    def delete_task(self):
        updated_tasks = []
        for index, task in enumerate(self.tasks):
            if not self.task_checkboxes[index + 1].get():
                updated_tasks.append(task)
        self.tasks = updated_tasks
        self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


