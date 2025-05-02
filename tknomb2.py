import tkinter

def imprimir_nombre():
    nombre = entry.get()
    if nombre.strip() == "":
        label_resultado.config(text="Por favor, ingresa un nombre.")
    else:
        label_resultado.config(text="Hola " + nombre)

# Crear la ventana principal
window = tkinter.Tk()
window.geometry("400x300")
window.title("Mi Aplicación AA")

# Crear el campo de entrada
entry = tkinter.Entry(window)
entry.pack(pady=10)

# Crear el botón para imprimir el nombre
button_imprimir = tkinter.Button(window, text="Imprimir nombre", command=imprimir_nombre)
button_imprimir.pack(pady=5)

# Crear el botón para salir
button_salir = tkinter.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Crear una etiqueta para mostrar el resultado
label_resultado = tkinter.Label(window, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Iniciar el bucle principal
window.mainloop()
