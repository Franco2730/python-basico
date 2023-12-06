#Los diccionarios en python son similares a las listas pero con algunas diferencias:
#Los diccionarios tienen la siguiente sintaxis:
mi_dicc = { 'c1':'Valor 1' , 'c2':'Valo 2' , 'c3':'Valor 3' } #Los elementos cuentan con una clave (c1, 2, 3) y un valor (Valor1, 2, 3) estos son
#separados por una coma y todo va dentro de llaves. Dichos elementos no respetan un orden, es decir, metodos como sort() o reverse() no funcionarian
#por el contrario, podriamos acceder a sus valores de la siguiente forma:
paciente = { 'nombre':'Franco',
            'apellido': 'Rosales',
            'peso': 90,
            'altura': 1.85 }

print(paciente['nombre']) #Franco
print(paciente['altura']) #1.85
print(paciente['peso']) #90

#Veamos otros ejemplos:

diccionario = { 'clave1' : 'valor 1', 'clave2' : 'valor 2' } #las claves no se pueden repetir, los valores si.
print(type(diccionario)) #<class 'dict'>

resultado = diccionario['clave1']
print(resultado) #valor 1

#----

cliente = {'nombre': 'Carina',
           'apellido': 'Rosales',
           'edad': 60,
           'parentezco': 'madre',
           'altura': 1.70}

consulta = cliente['edad']
print(consulta) #60

#----

dicc = {'cl1': 55, 'cl2': [30, 40, 50], 'cl3': {'sub1': 'Valor del dicc dentro de otro dicc', 'sub2': 'so confused'}}
print(dicc['cl2']) #[30, 40, 50]
print(dicc['cl2'][1]) #40
print(dicc['cl3']['sub1']) #Valor del dicc dentro de otro dicc
#----

test1 = { 'cla1' : ['a', 'b', 'c'], 'cla2': ['d', 'e', 'f'] }
print(test1['cla2'][1].upper()) # E : Se imprimió en mayuscula
#----
#Agregar un elemento a un diccionario ya creado. Con la siguiente sintaxis vamos a decir: Si en el dicionario existe el elemento tal dic[3], le
#vamos a modificar el valor a 'c'. En el caso de que no exista, crearlo.
dic = {1: 'a', 2: 'b'}
print(dic) #{1: 'a', 2: 'b'}

dic[3] = 'c'
print(dic) #{1: 'a', 2: 'b', 3: 'c'}

dic[2] = '$'
print(dic) #{1: 'a', 2: '$', 3: 'c'}

#conocer todas las claves de un diccionario.
print(dic.keys()) #dict_keys([1, 2, 3]) : Solicitamos ver únicamente las llaves (las claves)
print(dic.values()) #dict_values(['a', '$', 'c']) : Únicamente los valores (values)
print(dic.items()) #dict_items([(1, 'a'), (2, '$'), (3, 'c')]) : Solicitamos ver el dicc completo con llave y valor.
#----

#Práctica 1
#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición.
#Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}

print(mi_dict["puntos"]["points2"][1])


#Práctica Diccionarios 3
#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (
# sin tilde). Los nuevos datos son:
#nombre: Karen
#apellido: Jurgens
#edad: 36
#ocupacion: Editora
#pais: Colombia
#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

#Otra forma en la que se puede asignar valores a claves. Siempre tenemos que tener la misma cantidad de claves que de valores
#Lo mismo se puede lograr en listas y tuples:
mi_dicci = {1, 10, 100}
a, b, c = mi_dicci
print(a, b, c) #1 10 100