import tkinter as tk
from tkinter import messagebox

def realizar_calculo():
    # Obtener los valores de los campos
    try:
        num1 = float(entry_num1.get().strip())
        num2 = float(entry_num2.get().strip())
    except ValueError:
        messagebox.showwarning("Error", "Por favor, ingresa números válidos.")
        return

    # Obtener la operación seleccionada
    operacion = opcion_operacion.get()

    # Realizar el cálculo según la operación
    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    elif operacion == "Multiplicación":
        resultado = num1 * num2
    elif operacion == "División":
        if num2 == 0:
            messagebox.showwarning("Error", "No se puede dividir por cero.")
            return
        resultado = num1 / num2
    else:
        messagebox.showwarning("Error", "Selecciona una operación válida.")
        return

    # Mostrar el resultado en la etiqueta
    label_resultado.config(text=f"Resultado: {resultado:.2f}")

# Crear la ventana principal
window = tk.Tk()
window.geometry("300x400")
window.title("Calculadora")

# Etiqueta y campo para el primer número
tk.Label(window, text="Primer número:", font=("Arial", 12)).pack(pady=5)
entry_num1 = tk.Entry(window, width=10)
entry_num1.pack(pady=5)

# Etiqueta y campo para el segundo número
tk.Label(window, text="Segundo número:", font=("Arial", 12)).pack(pady=5)
entry_num2 = tk.Entry(window, width=10)
entry_num2.pack(pady=5)

# Etiqueta y menú desplegable para la operación
tk.Label(window, text="Operación:", font=("Arial", 12)).pack(pady=5)
opcion_operacion = tk.StringVar(window)
opcion_operacion.set("Suma")  # Valor por defecto
menu_operaciones = tk.OptionMenu(window, opcion_operacion, "Suma", "Resta", "Multiplicación", "División")
menu_operaciones.pack(pady=5)

# Botón para realizar el cálculo
button_calcular = tk.Button(window, text="Calcular", command=realizar_calculo)
button_calcular.pack(pady=10)

# Botón para salir
button_salir = tk.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(window, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Iniciar el bucle principal
window.mainloop()
