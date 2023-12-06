mi_set = set([1, 2, 3, 4, 5])

print(mi_set) #{1, 2, 3, 4, 5}
print(type(mi_set)) #<class 'set'>

otro_set_sinpalabraset = {10, 100, 1000}
print(otro_set_sinpalabraset)

print(len(mi_set)) #5
print(2 in mi_set) #true

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
set3 = set1.union(set2)
print(set3) #{1, 2, 3, 4, 5, 6} Ya que hay un 3 repetido, python lo omite.

set1.add(10)
print(set1) #{10, 1, 2, 3}

set1.remove((3))
print(set1) #{10, 1, 2}

set1.discard(2)
print(set1) #{10, 1}

set2.pop()
print(set2) #{4, 5, 6} Este metodo elimina de forma aleatoria un elemento

set2.clear()
print(set2) #set() Limpia / elimina lso elementos del set.