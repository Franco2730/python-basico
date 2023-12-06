# popitem: sirve para extraer el ultimo elemento, en este caso, de un diccionario
dicc = {'clave1': 100, 'clave2': 200, 'clave3': 300, 'clave4': 400}
print(dicc) # {'clave1': 100, 'clave2': 200, 'clave3': 300, 'clave4': 400}

elementoEliminado = dicc.popitem()

print(elementoEliminado) # El elemento eliminado (almacenado en elementoEliminado) es: ('clave4', 400)

print(dicc) #El dicc quedaria: {'clave1': 100, 'clave2': 200, 'clave3': 300}

print("---")

# lista = [1, 2, 3, 4, 5]
# lista.pop() # La funcion es la misma que popitem pero para nuestra lista. Elimina el ultimo elemento de la misma.
