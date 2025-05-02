import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    # Obtener los datos de los campos
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    edad = entry_edad.get().strip()
    ciudad = entry_ciudad.get().strip()

    # Validar que los campos no estén vacíos
    if not nombre or not apellido or not edad or not ciudad:
        messagebox.showwarning("Error", "Por favor, completa todos los campos.")
        return

    # Validar que la edad sea un número entero positivo
    try:
        edad = int(edad)
        if edad <= 0:
            messagebox.showwarning("Error", "La edad debe ser un número positivo.")
            return
    except ValueError:
        messagebox.showwarning("Error", "La edad debe ser un número válido.")
        return

    # Mostrar los datos en la etiqueta
    resultado = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nCiudad: {ciudad}"
    label_resultado.config(text=resultado)

# Crear la ventana principal
window = tk.Tk()
window.geometry("400x500")
window.title("Formulario de Datos")

# Etiquetas y campos de entrada
tk.Label(window, text="Nombre:", font=("Arial", 12)).pack(pady=5)
entry_nombre = tk.Entry(window)
entry_nombre.pack(pady=5)

tk.Label(window, text="Apellido:", font=("Arial", 12)).pack(pady=5)
entry_apellido = tk.Entry(window)
entry_apellido.pack(pady=5)

tk.Label(window, text="Edad:", font=("Arial", 12)).pack(pady=5)
entry_edad = tk.Entry(window)
entry_edad.pack(pady=5)

tk.Label(window, text="Ciudad:", font=("Arial", 12)).pack(pady=5)
entry_ciudad = tk.Entry(window)
entry_ciudad.pack(pady=5)

# Botón para mostrar los datos
button_mostrar = tk.Button(window, text="Mostrar Datos", command=mostrar_datos)
button_mostrar.pack(pady=10)

# Botón para salir
button_salir = tk.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(window, text="", font=("Arial", 12), justify="left")
label_resultado.pack(pady=10)

# Iniciar el bucle principal
window.mainloop()
