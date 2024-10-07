'''
2. Programa que calcule el área y el perímetro de un rectangulo a partir de su base y su altura
Entradas:
   base: integrer
   altura: integrer
Salidas:
   perimetro: integrer
   area: integrer
Analisis:
   se requiere calcular con las formulas para area y perimetro
'''
base = input ("escribe la base del rectangulo: ")
base = int(base)
altura = input ("escribe la altura del rectangulo: ")
altura = int(altura)
area = base * altura
perimetro = base + base + altura + altura
perimetro = (base + altura) * 2
print("el area del rectangulo es " + str(area))
print("el perimetro del rectangulo es " + str(perimetro))