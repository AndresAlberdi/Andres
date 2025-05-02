import tkinter

def imprimir_nombre():
    nombre = entry.get()
    print("Hola " + nombre)

# Crear la ventana principal
window = tkinter.Tk()
window.geometry("400x300")
window.title("Mi Aplicación AA")

# Crear el campo de entrada
entry = tkinter.Entry(window)
entry.pack(pady=10)  # Añadir espacio vertical

# Crear el botón para imprimir el nombre
button_imprimir = tkinter.Button(window, text="Imprimir nombre", command=imprimir_nombre)
button_imprimir.pack(pady=5)

# Crear el botón para salir, usando destroy en lugar de exit
button_salir = tkinter.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Iniciar el bucle principal
window.mainloop()
