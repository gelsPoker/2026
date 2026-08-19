# Escribir la sigguientee expresion en forma logaritmica
# a**3 * (b**2 - 2ac) / 2b
a = 3                      # a = int(input("Ingrese el primer valor:"))
b = 2
c = 1
resul = (a**3 * (b**2 - 2*a*c)) / (2*b)
print(f"El resultado del primer ejercicio es: {resul}")

# eje 2
d = float(input("Ingrese el valor de d:"))
e = float(input("Ingrese el valor de e:"))

resultado = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (d>e)
print(f"El resultado del segundo ejercicio es: {resultado}")

#eje 3
# Hacer un programa para intercambiar el valor de 2 variables
f = input("Ingrese el valor de f:")
g = input("Ingrese el valor de g:")
f = g
g = f
print(f"El nuevo valor de f es {f} y el nuevo  valor de g es {g}")

#eje 4
# Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia
import math
radio = float(input("Ingrese el valor del radio:"))
area = math.pi * radio**2
longitud = 2 * math.pi * radio
print(f"El area y la longitud de la circunferencia son {area:.2f} y {longitud:.2f}")

#eje 5
# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera
# pagar finalmente por su compra
total = float(input("Ingrese cual fue el monto de su compra:"))
descuento = (15 * total) / 100
nuevo = total - descuento
nuevo = print(f"la compra con descuento queda en un monto de {nuevo} pesos ")
