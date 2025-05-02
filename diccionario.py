persona = {
"nombre": "Juan",
"edad": 30,
"ciudad": "Ciudad de México",
"casado": False
}


# Acceder a valores a través de sus claves
nombre = persona["nombre"]
edad = persona["edad"]
print("Nombre:", nombre)
print("Edad:", edad)


# Modificar un valor en el diccionario
persona["edad"] = 31
print("Diccionario con edad modificada:", persona)


# Agregar un nuevo par clave-valor al diccionario
persona["ocupacion"] = "Ingeniero"
print("Diccionario con ocupación añadida:", persona)


# Eliminar un par clave-valor del diccionario
del persona["casado"]
print("Diccionario con 'casado' eliminado:", persona)


# Verificar si una clave está en el diccionario
if "ciudad" in persona:
    print("Ciudad:", persona["ciudad"])
else:
    print("La clave 'ciudad' no está en el diccionario")


# Iterar a través de las claves del diccionario
print("Claves del diccionario:")
for clave in persona:
    print(clave)


# Iterar a través de los valores del diccionario
print("Valores del diccionario:")
for valor in persona.values():
    print(valor)


# Iterar a través de los pares clave-valor del diccionario
print("Pares clave-valor del diccionario:")
for clave, valor in persona.items():
    print(clave, ":", valor)

