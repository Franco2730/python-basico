#Los metodos que usamos en los strings los podemos implementar a las listas. algunos de los metodos para listas son:
#Metodo sort(): ordena la lista. Si la lista es numerica, la ordena de menor a mayor, si son letras o nombres, de forma alfabetica.
lista = ['b', 'e', 'a', 'c', 'd']
lista.sort()
print(lista) #['a', 'b', 'c', 'd', 'e']
#Cabe aclarar que sort() NO DEVUELVE NADA, es decir, no podemos hacer lista_ordenada = lista.sort() porque será un no objeto

#Si quisieramos almacenar la lista ordenada podriamos:
desorden = [6, 3, 4, 1, 5, 2]
desorden.sort()
lista_ordenada = desorden
print(lista_ordenada) # [1, 2, 3, 4, 5, 6

#Como tenemos sort() para ordenar, tenemos a reverse para invertir:
lista2 = ['e', 'd', 'c', 'b', 'a']
lista2.reverse()
print(lista2) #['a', 'b', 'c', 'd', 'e']

#Una diferencia entre los metodos que afectan a los str y a las listas, en que los str son inmutables, por el contrario, podemos modificar a una lista
mi_lista = ['a', 'b',' c', 'd']
mi_lista[0] = 'alfa'
mi_lista.append('z') # ['alfa', 'b', ' c', 'd', 'z']: append sirve para agregar al final
mi_lista.pop() #pop sirve para eliminar. Si no le pasamos parametros, elimina el ultimo, para eliminar uno puntual, ponemos la posicion

print(mi_lista) #['alfa', 'b', ' c', 'd']

#Agregar de otra forma (Siempre tienen que tener la misma cantidad de clave que de valores)
mi_list = [1, 10, 100]
a, b, c = mi_list

print(a, b, c) #1 10 100
