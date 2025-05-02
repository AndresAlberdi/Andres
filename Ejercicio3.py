import tkinter as tk
from tkinter import messagebox

def dibujar_rombo():
    # Obtener los datos de los campos
    caracter = entry_caracter.get().strip()
    try:
        lineas = int(entry_lineas.get().strip())
    except ValueError:
        messagebox.showwarning("Error", "El número de líneas debe ser un número entero.")
        return

    # Validaciones
    if len(caracter) != 1 or not caracter.isascii() or caracter.isspace():
        messagebox.showwarning("Error", "Ingresa un solo carácter estándar (no espacio).")
        return
    if lineas < 1 or lineas % 2 == 0 or lineas > 19:
        messagebox.showwarning("Error", "El número de líneas debe ser un número impar positivo (menor a 20).")
        return

    # Crear la ventana para mostrar el rombo
    ventana_rombo = tk.Toplevel()
    ventana_rombo.geometry("400x400")
    ventana_rombo.title("Rombo")

    # Calcular el rombo
    rombo_texto = ""
    mitad = lineas // 2
    for i in range(mitad + 1):
        espacios = " " * (mitad - i)
        caracteres = caracter * (2 * i + 1)
        rombo_texto += espacios + caracteres + "\n"
    for i in range(mitad - 1, -1, -1):
        espacios = " " * (mitad - i)
        caracteres = caracter * (2 * i + 1)
        rombo_texto += espacios + caracteres + "\n"

    # Mostrar el rombo en un Label con fuente monoespaciada
    label_rombo = tk.Label(ventana_rombo, text=rombo_texto, font=("DejaVu Sans Mono Book", 12))
    label_rombo.pack(expand=True)

# Crear la ventana principal
window = tk.Tk()
window.geometry("300x250")
window.title("Parámetros del Rombo")

# Etiqueta y campo para el carácter
tk.Label(window, text="Carácter:", font=("Arial", 12)).pack(pady=5)
entry_caracter = tk.Entry(window, width=5)
entry_caracter.pack(pady=5)

# Etiqueta y campo para el número de líneas
tk.Label(window, text="Número de líneas (impar):", font=("Arial", 12)).pack(pady=5)
entry_lineas = tk.Entry(window, width=10)
entry_lineas.pack(pady=5)

# Botón para dibujar el rombo
button_dibujar = tk.Button(window, text="Dibujar Rombo", command=dibujar_rombo)
button_dibujar.pack(pady=10)

# Botón para salir
button_salir = tk.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Iniciar el bucle principal
window.mainloop()
