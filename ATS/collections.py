# Listas
'''
lista = [1,2,3,4]

print(len(lista))                # len --> saber la cantidad de elementos que tiene tu lista.
lista.append(7)                  # .append() --> agregar elementos a la lista

lista.insert(2,2.5)              # .insert() --> insertar un valor(lugar donde quieres que vaya,valor)
lista.extend([7,8,9])            # .extend([]) --> agregar mas de un elemento a la vez.
print(lista)
print(43 in lista)               # buscar un valor en la lista.
print(lista.index(4))            # .index() --> te mmuestra el indice de donde se encuentra el valor.
print(lista.count(1))            # .count() --> cuenta la cantidad de veces que se enceuntra un valor.
lista.pop(2)                     # .pop() --> eliminar un valor mediante su indice. Si esta vacio elimina el ultimo valor de la lista.
lista.remove(1)                  # .remove() --> eliminar un elemento en especifico.
lista.clear()                    # .clear() ---> limpiar la lista.
print(lista)


# lista.sort() --> ordenar los elementos de la lista ascendentemente.
# lista.sort(reverse=True) --> ordenar los elementos de la lista a la inversa.

# Tuplas
tupla = (1,3.4,"iha")
print(tupla)         
# lista = [2,4,5,"JSI"]            lista.tuple(lista) ---> transformar una lista a tupla.

# Conjuntos 
conjunto = set()                   # Se le pone el set() para que no sea un diccionario.
conjunto = {3}                     # NO puede haber valores duplicados en un conjunto
conjunto.add(2)                    # .add() --> para agregar en un conjunto.
conjunto.discard(2)                # .discard() --> eliminar un elemento.
print(conjunto)

a = set()
b = set()

a = {1,2,3}
b = {3,4,5}                 

# .union() --> unir dos conjuntos. tambien puede ser con el simbolo |
# intersepcion                                  --> &
# diferencia de conjuntos                       --> -
# diferncia simetrica                           --> ^
# ver si un conjunto es subconjunto de otro     --> .issubset()
# ver si un conjunto es superconjunto de otro   --> .issuperset()
# ver si dos conjuntos son disjuntos            --> .isdisjoint()
# hacer un conjunto inmutable                   --> frozenset({1,2,3})

# Diccionarios    ---> {"clave": valor}
diccionario = {"nombre": "Juan", "edad": 30}
diccionario["apellido"] = "Perez"
del(diccionario["edad"])       
print(diccionario)          
'''
# acceder a un valor mediante su llave.         print(diccionario["nombre"])
# agregar un elemento al diccionario.           diccionario["apellido"] = "Perez"
# eliminar un elemento                          del(diccionario[""])

equipos = {10:"leonel mesii",7:"cristiano ronaldo",11:"neymar jr",1:"claudio bravo"}
print(equipos)
print(equipos.get(19,"No existe un jgador con ese nuumero"))
print(equipos.keys())     # Mostrar solo las claves del diccionario.
print(equipos.values())   # Mostrar solos los nombres del diccionario.

# Pilas 
pila = [1,2,3,4]
pila.append(5)          # .append() --> agregar un elemento al final de la pila.
pila.pop()             # .pop() --> eliminar el ultimo elemento de la pila.
print(pila)
# Escriba un programa donde tenga una lista y que, elimine los elementos repetidos y por ultimo mostrar la lista 
lista = [1,2,3,4,5,6,7,8,9,1,2,3,4,"hola","hola","hola"]
lista = list(set(lista))  # Transformar la lista a conjunto y luego a lista para eliminar los elementos repetidos.
print(lista)
# escriba un programa que tenga 2 listas(no debe haber repeticiones)
# 1. Lista de elementos que aparecen en ambas listas.
# 2. Lista de elementos que aparecen en la primera lista pero no en la segunda.
# 3. Lista de elementos que aparecen en la segunda lista pero no en la primera. 
    
