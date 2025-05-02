import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar_funcion():
    # Obtener datos de los campos
    funcion = opcion_funcion.get()
    try:
        inicio = float(entry_inicio.get().strip())
        fin = float(entry_fin.get().strip())
    except ValueError:
        messagebox.showwarning("Error", "Ingresa valores numéricos válidos para el intervalo.")
        return

    # Validar intervalo
    if inicio >= fin:
        messagebox.showwarning("Error", "El valor inicial debe ser menor que el valor final.")
        return

    # Crear ventana para el gráfico
    ventana_grafico = tk.Toplevel()
    ventana_grafico.geometry("600x500")
    ventana_grafico.title(f"Gráfico de {funcion}")

    # Generar datos para el gráfico
    x = np.linspace(inicio, fin, 1000)  # 1000 puntos para suavidad
    x_rad = np.radians(x)  # Convertir grados a radianes

    # Calcular valores de la función
    try:
        if funcion == "Seno":
            y = np.sin(x_rad)
        elif funcion == "Coseno":
            y = np.cos(x_rad)
        elif funcion == "Tangente":
            y = np.tan(x_rad)
            # Limitar valores de tangente para evitar líneas discontinuas extremas
            y = np.clip(y, -10, 10)
    except Exception as e:
        messagebox.showwarning("Error", f"Error al calcular la función: {str(e)}")
        ventana_grafico.destroy()
        return

    # Crear la figura de matplotlib
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x, y, label=funcion)
    ax.set_xlabel("Ángulo (grados)")
    ax.set_ylabel(f"{funcion}(x)")
    ax.set_title(f"Gráfico de {funcion}")
    ax.grid(True)
    ax.legend()

    # Integrar el gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    # Botón para cerrar la ventana del gráfico
    tk.Button(ventana_grafico, text="Cerrar", command=ventana_grafico.destroy).pack(pady=5)

# Crear la ventana principal
window = tk.Tk()
window.geometry("300x300")
window.title("Graficador de Funciones Trigonométricas")

# Etiqueta y menú desplegable para la función
tk.Label(window, text="Función:", font=("Arial", 12)).pack(pady=5)
opcion_funcion = tk.StringVar(window)
opcion_funcion.set("Seno")  # Valor por defecto
menu_funciones = tk.OptionMenu(window, opcion_funcion, "Seno", "Coseno", "Tangente")
menu_funciones.pack(pady=5)

# Etiqueta y campo para el inicio del intervalo
tk.Label(window, text="Inicio del intervalo (grados):", font=("Arial", 12)).pack(pady=5)
entry_inicio = tk.Entry(window, width=10)
entry_inicio.pack(pady=5)

# Etiqueta y campo para el fin del intervalo
tk.Label(window, text="Fin del intervalo (grados):", font=("Arial", 12)).pack(pady=5)
entry_fin = tk.Entry(window, width=10)
entry_fin.pack(pady=5)

# Botón para graficar
button_graficar = tk.Button(window, text="Graficar", command=graficar_funcion)
button_graficar.pack(pady=10)

# Botón para salir
button_salir = tk.Button(window, text="Salir", command=window.destroy)
button_salir.pack(pady=5)

# Iniciar el bucle principal
window.mainloop()
