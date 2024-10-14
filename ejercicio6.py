'''
Calcular la media de tres numeros pedidos por teclado
'''
# Solicitar al usuario que ingrese tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular la media
media = (num1 + num2 + num3) / 3

# Mostrar el resultado
print(f"La media de los tres números es: {media:.2f}")
