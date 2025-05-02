def adivinar():
	nombre = input("Ingresa tu nombre: ")
	edad = int(input("Ingresa tu edad: "))

	anio_actual = 2025
	anio_nacimiento = anio_actual - edad


	print(f"Hola, {nombre}! Naciste aproximadamente en el año {anio_nacimiento}.")




adivinar()
