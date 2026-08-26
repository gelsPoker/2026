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
'''

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

