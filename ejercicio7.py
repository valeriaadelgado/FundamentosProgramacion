'''
Programa que recibe una cantidad de minutos y muestra por pantalla a cuantas horas y minutos corresponde
'''
def convertir_minutos_a_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

# Solicitar al usuario que ingrese la cantidad de minutos
try:
    minutos_input = int(input("Ingrese la cantidad de minutos: "))
    if minutos_input < 0:
        print("Por favor, ingrese un número positivo.")
    else:
        horas, minutos = convertir_minutos_a_horas(minutos_input)
        print(f"{minutos_input} minutos son {horas} horas y {minutos} minutos.")
except ValueError:
    print("Por favor, ingrese un número válido.")
