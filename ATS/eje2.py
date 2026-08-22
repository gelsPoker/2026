'''
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
num3 = int(input("Ingrese el primer nuemro:"))
num4 = int(input("Ingrese el segundo numero:"))
num5 = int(input("Ingrese el tercer numero:"))

if(num3>num4) and (num3>num5):
    print(f"El numero 1: {num3} es el mayor de todos ")
elif(num4>num3) and (num4>num5):
    print(f"El numero 2: {num4} es el mayor de todos")
elif(num5>num3) and (num5>num4):
    print(f"El numero 3: {num5} es el mayor a todos")
else:
    print("Todos los numeros son igualees")

#eje3 
# Hacer un programa que pida un caracter e indique si es una vocal o no 
letra = input("Ingrese un caracter:")
if(letra=="a") or (letra=="e") or (letra=="i") or (letra=="o") or (letra=="u"):
    print("La letra pertenece una vocal")
elif(letra=="A") or (letra=="E") or (letra=="I") or (letra=="O") or (letra=="U"):
    print("La letra pertenece a una vocal mayuscula")
else:
    print("LA letra No pertenece a ninguna vocal")

# Si ingresamos en letra = input("Ingrese un caracter:").lower()
# .lower() --> transformar todo a minuscula
# .upper() --> transformar todo a mayuscula


#eje 4
# Contruir un programa que simule el funcionamiento de una calculadora que puede realizar las 4 operaciones
# el ususuario debe especificar la operacion con el primer caracter del nombre de la operacion
print("Bienvenido a la calculadora")
print("Ingrese S,s --> Suma")
print("Ingrese R,r --> Resta")
print("Ingrese M,n --> Multiplicacion")
print("Ingrese D,d --> Division")
caracter = input("Ingrese la operacion que desea:")
num1 = float(input("Ingrese el primer numero:"))
num2 = float(input("Ingrese el segundo numero:"))
if(caracter=="S") or (caracter=="s"):
    resul = num1 + num2
    print(f"El resultado de la Suma de ambos numeros es: {resul}")
elif(caracter=="R") or (caracter=="r"):
    resul = num1 - num2
    print(f"El resultado de la Suma de ambos numeros es: {resul}")
elif(caracter=="M") or (caracter=="m"):
    resul = num1 * num2
    print(f"El resultado de la Suma de ambos numeros es: {resul}")
elif(caracter=="D") or (caracter=="d"):
    resul = num1 / num2
    print(f"El resultado de la Suma de ambos numeros es: {resul}")
else:
    print("No ingreso ningun caracter recomendado")
    
'''
#eje 5
# Hacer un programa que simule un cajero con uun saldo inicial de $1000 y tendra
# 1. Ingresar dinero a la cuenta. 2. Retirar dinero de la cuenta 
# 3. Mostrar dinero disponible. 4. Salir
saldo_inicial = 1000
print(f"Bienvnidos a su cajero automatico, su saldo inicial es de: {saldo_inicial}")
print("Ingrese 1 para ingresar dinero a la cuenta")
print("Ingrese 2 para retirar dinero de la cuenta")
print("Ingrese 3 para mostrar dinero disponible")
print("Ingrese 4 para salir")
print("")
while(saldo_inicial>=0):
    opcion = int(input("Ingrese la opcion que desea:"))
    if(opcion==1):
        ingreso = float(input("Ingrese la cantidad de dinero que desea ingresar:"))
        saldo_inicial = saldo_inicial + ingreso
        print(f"Su nuevo saldo es de: ${saldo_inicial}")
    elif(opcion==2):
        retiro = float(input("Ingrese la cantidad de dinero que desea retirar:"))
        if(retiro>=saldo_inicial):
            print("Usted no posee esa cantidad de dinero, intente de nuevo")
        else:
            saldo_inicial = saldo_inicial - retiro
            print(f"Su nuevo saldo es de: ${saldo_inicial}")
    elif(opcion==3):
        print(f"El saldo que posee es de: ${saldo_inicial}")
    elif(opcion==4):
        print(f"Gracias por su paciencia")
        exit();