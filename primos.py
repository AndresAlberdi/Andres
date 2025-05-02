def es_primo(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos(limite):
    """Encuentra todos los números primos entre 1 y limite."""
    primos = [num for num in range(1, limite + 1) if es_primo(num)]
    return primos

def main():
    # Solicitar número al usuario
    try:
        limite = int(input("Ingresa un número entero positivo: "))
        if limite < 1:
            print("El número debe ser positivo.")
            return
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        return

    # Encontrar números primos
    primos = encontrar_primos(limite)

    # Mostrar resultados en consola
    if primos:
        print(f"Números primos entre 1 y {limite}: {primos}")
        print(f"Total de números primos: {len(primos)}")
    else:
        print(f"No hay números primos entre 1 y {limite}.")

    # Guardar resultados en results.txt
    try:
        with open("results.txt", "w") as archivo:
            archivo.write(f"Números primos entre 1 y {limite}:\n")
            if primos:
                archivo.write(", ".join(map(str, primos)) + "\n")
                archivo.write(f"Total de números primos: {len(primos)}\n")
            else:
                archivo.write("No hay números primos.\n")
        print("Resultados guardados en results.txt")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    main()
