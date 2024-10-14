'''
Dados dos números, mostrar la suma, resta, division y multiplicacion de ambos
'''
# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
# Manejar la división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir por cero"

# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")