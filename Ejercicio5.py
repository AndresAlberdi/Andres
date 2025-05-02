import tkinter as tk
from tkinter import messagebox
import math

def realizar_calculo():
    # Obtener el valor del primer número
    try:
        num1 = float(entry_num1.get().strip())
    except ValueError:
        messagebox.showwarning("Error", "Ingresa un número válido en el primer campo.")
        return

    # Obtener el segundo número (si es necesario)
    num2 = None
    if opcion_operacion.get() in ["Suma", "Resta", "Multiplicación", "División", "Potencia", "Módulo"]:
        try:
            num2 = float(entry_num2.get().strip())
        except ValueError:
            messagebox.showwarning("Error", "Ingresa un número válido en el segundo campo.")
            return

    # Obtener la operación seleccionada
    operacion = opcion_operacion.get()
    resultado = None

    # Realizar el cálculo según la operación
    try:
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
        elif operacion == "Potencia":
            resultado = num1 ** num2
        elif operacion == "Módulo":
            if num2 == 0:
                messagebox.showwarning("Error", "No se puede calcular el módulo con cero.")
                return
            resultado = num1 % num2
        elif operacion == "Seno":
            resultado = math.sin(math.radians(num1))  # Convertir a radianes
        elif operacion == "Coseno":
            resultado = math.cos(math.radians(num1))
        elif operacion == "Tangente":
            if math.cos(math.radians(num1)) == 0:
                messagebox.showwarning("Error", "La tangente no está definida para este ángulo.")
                return
            resultado = math.tan(math.radians(num1))
        elif operacion == "Logaritmo base 10":
            if num1 <= 0:
                messagebox.showwarning("Error", "El logaritmo base 10 no está definido para números no positivos.")
                return
            resultado = math.log10(num1)
        elif operacion == "Logaritmo natural":
            if num1 <= 0:
                messagebox.showwarning("Error", "El logaritmo natural no está definido para números no positivos.")
                return
            resultado = math.log(num1)

        # Mostrar el resultado
        label_resultado.config(text=f"Resultado: {resultado:.4f}")
        
        # Agregar al historial en el Listbox
        if num2 is not None:
            listbox_historial.insert(tk.END, f"{operacion}: {num1} y {num2} = {resultado:.4f}")
        else:
            listbox_historial.insert(tk.END, f"{operacion}: {num1} = {resultado:.4f}")

        # Limpiar campos
        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)

    except Exception as e:
        messagebox.showwarning("Error", f"Error en el cálculo: {str(e)}")

# Crear la ventana principal
window = tk.Tk()
window.geometry("400x500")
window.title("Calculadora Científica")

# Etiqueta y campo para el primer número
tk.Label(window, text="Primer número:", font=("Arial", 12)).pack(pady=5)
entry_num1 = tk.Entry(window, width=15)
entry_num1.pack(pady=5)

# Etiqueta y campo para el segundo número
tk.Label(window, text="Segundo número (si aplica):", font=("Arial", 12)).pack(pady=5)
entry_num2 = tk.Entry(window, width=15)
entry_num2.pack(pady=5)

# Etiqueta y menú desplegable para la operación
tk.Label(window, text="Operación:", font=("Arial", 12)).pack(pady=5)
opcion_operacion = tk.StringVar(window)
opcion_operacion.set("Suma")  # Valor por defecto
operaciones = [
    "Suma", "Resta", "Multiplicación", "División", "Potencia", "Módulo",
    "Seno", "Coseno", "Tangente", "Logaritmo base 10", "Logaritmo natural"
]
menu_operaciones = tk.OptionMenu(window, opcion_operacion, *operaciones)
menu_operaciones.pack(pady=5)

# Botón para realizar el cálculo
button_calcular = tk.Button(window, text="Calcular", command=realizar_calculo)
button_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(window, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Listbox para el historial de cálculos
tk.Label(window, text="Historial de cálculos:", font=("Arial", 12)).pack(pady=5)
listbox_historial = tk.Listbox(window, width=40, height=8)
listbox_historial.pack(pady=5)

# Botón para salir
button_salir = tk.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Iniciar el bucle principal
window.mainloop()
