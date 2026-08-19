numero = int(input("ingrese su edad:"))
if(numero >= 18)and(numero<=99):
    print("Es mayor de edad")
elif(numero <= 18)and(numero>0):
    print("Es menor de edad")
else:
    print("No quiera sobrepasar a la maquina")

#eje1 
# Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son
num1 = int(input("Ingrese el primer valor:"))
num2 = int(input("Ingrese el segundo valor:"))
if((num1%2)==0)and((num2%2)==0):
    print("Ambos numero son pares")
elif((num1%2)==0)and((num2%2)==1):
    print("solo el numero 1 es par")
elif((num1%2)==1)and((num2%2)==0):
    print("solo el numero 2 es par")
else:
    print("AMBOS SON IMPARES")

#eje 2
# hacer un programa que pida 3 numeros y determine cual es el mayor


