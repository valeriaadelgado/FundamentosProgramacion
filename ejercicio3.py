'''
Ejercicio 3:
   Programa que calculle la hipotenusa a apartir de los dos catetos
Entradas
   catetoA: int -a
   catetoB: int -b
   Salidas:
Salidas:
   hipotenusa -c
'''
a = input("Escrib el valor de cateto A: ")
a = int(a)
b = input("Escribe el valor de cateto B: ")
b = int(b)
c = (a * a + b * b) ** (1/2)
c = math.sqrt (a*a+b*b)
print("El valor de la hipotenusa es: ", c)