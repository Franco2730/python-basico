#Un metodo muy util que tenemos es Range (rango) en vez de crear una variable, con una lista de elementos, en este caso de numeros, para poder iterar y practicar y blabla. Colocamos range y entre que numero y que numero. El segundo parametro no es inclusivo. Si colocamos un tercer parametro, este hara referencia a los pasos que nos vamos a saltear, por ejemplo si ponemos: ...in range(1, 10, 2) el resultado será: 1 / 3 / 5 / 7 / 9 debido a que el primer parametro es DONDE COMENZAMOS, el segundo parametro es HASTA DONDE vamos a llegar pero recordar que NO se tiene en cuenta. y el tercer parametro son los pasos que va a dar el rango para saltearse un numero, en este caso al ser un 2 vamos a tomar el cuenta el primer parametro 1 / el numero siguiente se saltea / 3 / el cuarto numero se saltea / 5 y así....

for numero in range(1, 10, 2):
    print(numero)

# 1
# 3
# 5
# 7
# 9

#Range no solo sirve para los loops, tambien sirve para crear contenido. Es decir, si nosotros tuvieramos que crear una lista con 100 numeros, hasta donde sabemos lo haríamos de la siguiente forma:

lista = [1, 2, 3, 4, 5, 50, 100] # Sería mucho trabajo colocar uno por uno.

#Utilizando range, simplemente le ponemos list adelante del range para avisarle a python que el siguiente contenido es una lista y listo. 

lista = list(range(1, 101))
print(lista)