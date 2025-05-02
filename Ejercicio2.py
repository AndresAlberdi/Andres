import tkinter as tk
from tkinter import messagebox

def contar_caracteres():
    # Obtener la frase del campo de entrada
    frase = entry_frase.get().strip()
    
    # Validar que la frase no esté vacía
    if not frase:
        messagebox.showwarning("Error", "Por favor, ingresa una frase.")
        return
    
    # Contar los caracteres (incluye espacios)
    conteo = len(frase)
    
    # Mostrar el resultado en la etiqueta
    label_resultado.config(text=f"La frase tiene {conteo} caracteres\n (se exceptúan caracteres espacio antes y después\n de los caracteres especiales).")

# Crear la ventana principal
window = tk.Tk()
window.geometry("400x300")
window.title("Conteo de Caracteres Estándar")

# Etiqueta y campo de entrada para la frase
tk.Label(window, text="Ingresa una frase de caracteres estándar:", font=("Arial", 12)).pack(pady=10)
entry_frase = tk.Entry(window, width=30)
entry_frase.pack(pady=5)

# Botón para contar caracteres
button_contar = tk.Button(window, text="Contar Caracteres", command=contar_caracteres)
button_contar.pack(pady=10)

# Botón para salir
button_salir = tk.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(window, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Iniciar el bucle principal
window.mainloop()
