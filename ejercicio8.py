'''
Un vendedor recibe un sueldo base mas de 10% extra por comision de sus ventas, el vendedor desea 
saber cuanto  dinero obtendra por concepto de comisiones por las tres ventas que realiza en el mes y
el total que recibira en el mes tomando en cuenta su sueldo base y comisiones
'''
v1 = input("Ingresa la venta 1: ")
v1 = int(v1)
v2 = input("ingresa la venta 2: ")
v2 = int(v2)
v3 = input("ingresa la venta 3: ")
v3 = int(v3)
c1 = (v1*0.10)
c2 = (v2*0.10)
c3 = (v3*0.10)
ct = (c1+c2+c3)
vt = (v1+v2+v3)
sueldo = (ct + vt)
print ("El sueldo es de:",sueldo)
