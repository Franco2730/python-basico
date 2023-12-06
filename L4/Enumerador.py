#Miremos el siguiente ejemplo
#Si quisieramos asignarle un numero correspondiente y de forma ascendente a cada elemento, lo hariamos asi:
lista = ['a', 'b', 'c', 'd']
indice = 0

for index in lista:
    print(indice, index)
    indice += 1

# 0 a
# 1 b
# 2 c
# 3 d

#Pero esto no sería lo más conveniente en python ya que podriamos utilizar el metodo enumerator. 

lista2 = ['a', 'b', 'c', 'd']

for index2 in enumerate(lista):
    print(index2)

# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
print("------------")

#Ahora vamos a mezclar enumerate con range:

for prueba in enumerate(range(1, 11)):
    print(prueba)

# (0, 1)
# (1, 2)
# (2, 3)
# (3, 4)
# (4, 5)
# (5, 6)
# (6, 7)
# (7, 8)
# (8, 9)
# (9, 10)