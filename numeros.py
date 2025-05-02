numeros = [1, 2, 3, 4, 5]


# Imprimir la lista completa
print("Lista de números:", numeros)


# Acceder a elementos individuales de la lista (índices comienzan en 0)
primer_numero = numeros[0]
segundo_numero = numeros[1]

print("Primer número:", primer_numero)
print("Segundo número:", segundo_numero)


# Modificar un elemento de la lista
numeros[0] = 10
print("Lista modificada:", numeros)


# Agregar un elemento al final de la lista
numeros.append(6)
print("Lista con elemento agregado:", numeros)


# Encontrar la longitud de la lista (número de elementos)
longitud = len(numeros)
print("Longitud de la lista:", longitud)


# Eliminar un elemento de la lista por valor
numeros.remove(3)
print("Lista con elemento 3 eliminado:", numeros)


# Eliminar un elemento de la lista por índice
elemento_eliminado = numeros.pop(2)
print("Elemento eliminado:", elemento_eliminado)
print("Lista después de eliminar por índice:", numeros)


# Iterar a través de la lista con un bucle for
print("Iterando a través de la lista:")
for numero in numeros:
    print(numero)


# Verificar si un elemento está en la lista
if 5 in numeros:
    print("5 está en la lista")
else:
    print("5 no está en la lista")

