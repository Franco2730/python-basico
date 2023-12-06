#Son inmutables y se escriben como las listas pero en vez de corchete, llevan parentesis .Los tupples se procesan mas rapido que
# las listas, ocupan menos memoria y son a prueba de errores debido a su inmutabilidad.

mi_tuple = (1, 2, 3, 4)
mi_tuple2 = (1, 2.5, "3", {'tuple': 'con-objeto'})

print(type(mi_tuple))#<class 'tuple'>
print(mi_tuple2) #(1, 2.5, '3', {'tuple': 'con-objeto'})
print(mi_tuple[0]) #1
print(mi_tuple[-2]) #3 : Recordando que si elegimos un numero negativo se contara de derecha a izquierda

#consultamos y cambiamos de tuple a lista
mi_tuple3 = (1, 2, (100, 200, 300), 4)
mi_tuple_lista = list(mi_tuple3)
print(type(mi_tuple_lista)) #<class 'list'>
print(mi_tuple3[2][1]) #200

#Como asignar valores a claves. Lo mismo se puede lograr en diccionarios y listas. Siempre tener la misma cantidad de claves que de valores
mi_tuple4 = (1, 10, 100)
a, b, c = mi_tuple4
print(a, b, c) #1 10 100

#Count nos permite saber la cantidad de veces que se repite un valor:
mituple = (1, 2, 3, 3, 2, 1, 1, 6, 8)
print(mituple.count(1)) #Nos informa que el numero 1 aparece 3 veces
print(mituple.index(3)) #Nos informa que en la posicion 3 se encuentra el numero 2
