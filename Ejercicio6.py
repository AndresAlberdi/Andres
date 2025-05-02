import tkinter as tk
from tkinter import messagebox

class ListaTareas:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x500")
        self.root.title("Lista de Tareas")

        # Lista para almacenar tareas (formato: [completada, texto])
        self.tareas = []

        # Etiqueta y campo para ingresar nueva tarea
        tk.Label(root, text="Nueva tarea:", font=("Arial", 12)).pack(pady=5)
        self.entry_tarea = tk.Entry(root, width=30)
        self.entry_tarea.pack(pady=5)

        # Botones para acciones
        tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea).pack(pady=5)
        tk.Button(root, text="Editar Tarea", command=self.editar_tarea).pack(pady=5)
        tk.Button(root, text="Marcar como Completada", command=self.marcar_completada).pack(pady=5)
        tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea).pack(pady=5)
        tk.Button(root, text="Salir", command=root.destroy).pack(pady=5)

        # Listbox para mostrar tareas
        self.listbox_tareas = tk.Listbox(root, width=40, height=15)
        self.listbox_tareas.pack(pady=10)

    def agregar_tarea(self):
        # Obtener texto de la entrada
        texto = self.entry_tarea.get().strip()
        if not texto:
            messagebox.showwarning("Error", "Por favor, ingresa una tarea.")
            return

        # Agregar tarea (no completada por defecto)
        self.tareas.append([False, texto])
        self.actualizar_listbox()
        self.entry_tarea.delete(0, tk.END)  # Limpiar campo

    def editar_tarea(self):
        # Verificar si hay una tarea seleccionada
        try:
            indice = self.listbox_tareas.curselection()[0]
        except IndexError:
            messagebox.showwarning("Error", "Selecciona una tarea para editar.")
            return

        # Crear ventana para editar
        ventana_editar = tk.Toplevel(self.root)
        ventana_editar.geometry("300x150")
        ventana_editar.title("Editar Tarea")

        tk.Label(ventana_editar, text="Nuevo texto:", font=("Arial", 12)).pack(pady=5)
        entry_nuevo = tk.Entry(ventana_editar, width=30)
        entry_nuevo.pack(pady=5)
        entry_nuevo.insert(0, self.tareas[indice][1])  # Cargar texto actual

        def guardar_cambio():
            nuevo_texto = entry_nuevo.get().strip()
            if not nuevo_texto:
                messagebox.showwarning("Error", "El texto no puede estar vacío.")
                return
            self.tareas[indice][1] = nuevo_texto
            self.actualizar_listbox()
            ventana_editar.destroy()

        tk.Button(ventana_editar, text="Guardar", command=guardar_cambio).pack(pady=5)

    def marcar_completada(self):
        # Verificar si hay una tarea seleccionada
        try:
            indice = self.listbox_tareas.curselection()[0]
        except IndexError:
            messagebox.showwarning("Error", "Selecciona una tarea para marcar.")
            return

        # Cambiar estado de completada
        self.tareas[indice][0] = not self.tareas[indice][0]
        self.actualizar_listbox()

    def eliminar_tarea(self):
        # Verificar si hay una tarea seleccionada
        try:
            indice = self.listbox_tareas.curselection()[0]
        except IndexError:
            messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")
            return

        # Eliminar tarea
        del self.tareas[indice]
        self.actualizar_listbox()

    def actualizar_listbox(self):
        # Limpiar Listbox
        self.listbox_tareas.delete(0, tk.END)
        # Agregar tareas con indicador de estado
        for completada, texto in self.tareas:
            prefijo = "[X]" if completada else "[ ]"
            self.listbox_tareas.insert(tk.END, f"{prefijo} {texto}")

# Crear la ventana principal
root = tk.Tk()
app = ListaTareas(root)
root.mainloop()
