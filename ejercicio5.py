'''
Escriibir un programa que convierta un valor dado en grados Fahrenheit a gradoss Celsius
'''
# Solicitar al usuario que ingrese la temperatura en Fahrenheit
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Convertir a Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Mostrar el resultado
print(f"La temperatura en grados Celsius es: {celsius:.2f}")
