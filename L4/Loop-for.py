# En programación, un "loop" (bucle) es una estructura que permite ejecutar un bloque de código repetidamente. Los loops son fundamentales para la automatización de tareas repetitivas. En Python, hay varios tipos de loops, pero los dos más comunes son for y while.

#      forbucle:
#     El bucle  forse utiliza para iterar sobre una secuencia (como una lista, tupla, cadena de caracteres o rango) y ejecutar un bloque de código para cada elemento de esa secuencia.

#     Ejemplos:

# Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Este bucle imprimirá cada elemento de la lista frutas.

#  whilebucle:
# El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera.

# Ejemplo:
print("----------")
# Bucle while para contar hasta 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Están los loops que se ejecutaran una cantidad definida de veces y otros loops que lo harán una cantidad indefinica.

# Objetos iterables:
# Un objeto iterable en Python es cualquier objeto que se puede recorrer elemento por elemento. Los objetos iterables pueden ser utilizados en bucles for. Algunos ejemplos comunes de objetos iterables son listas, tuplas, cadenas de caracteres, diccionarios y rangos.

# Por ejemplo, en el bucle for anterior, la variable frutas es un objeto iterable (una lista), y cada iteración del bucle toma un elemento de esa lista y ejecuta el bloque de código.
print("----------")
# Para qué qué sirve un bucle?
# Los loops son esenciales en la programación porque permiten automatizar tareas repetitivas y realizar operaciones en conjuntos de datos. Al usar bucles, puedes evitar escribir el mismo código una y otra vez, lo que hace que tu programa sea más eficiente y fácil de mantener.

# En resumen, los loops son una herramienta poderosa que te permite ejecutar código de manera repetitiva, ya sea para procesar datos, realizar cálculos o realizar cualquier tarea que deba repetirse varias veces.

# Como habiamos dicho, los dos loops mas conocidos son el FOR y el WHILE. Uno se repite una cantidad DEFINIDA de veces y el otro no.

# Bucle "FOR LOOP" que se repite una cantidad DEFINIDA de veces.

nombres = ['Franco', 'Carina', 'Carlos', 'Teresa', 'Claudia']

for elemento in nombres: #por cada elemento en nombres
    print("Hola!!" + elemento)     #imprimir("Hola!!")

# Hola!!Franco
# Hola!!Carina
# Hola!!Carlos
# Hola!!Teresa
# Hola!!Claudia

print("----------")

lista = ['a', 'b', 'c', 'd']

for letra in lista: # Se utiliza un bucle for para iterar sobre cada elemento (letra) en la lista lista.
    numeroLetra = lista.index(letra) + 1 
    print(f"Letra {numeroLetra}: {letra}")


# for letra in lista: 
#   Se utiliza un bucle for para iterar sobre cada elemento (letra) en la lista lista

# numeroLetra = lista.index(letra) + 1 
#   Dentro del bucle, se utiliza el método index() para obtener el índice de la letra actual en la lista y luego se suma 1. Esto se hace para obtener el número de la letra, ya que los índices en Python comienzan desde 0, pero en este caso, parece que se quiere comenzar a contar desde 1.

# print(f"Letra {numeroLetra}: {letra}")
#   Se imprime un mensaje formateado que muestra el número de la letra y la letra misma. La f-string (cadena formateada) permite incluir variables directamente en la cadena.

#   En resumen, este código recorre la lista de letras e imprime un mensaje para cada letra que indica su posición en la lista (empezando desde 1) y la letra misma. Es un ejemplo simple de cómo usar un bucle for para procesar elementos en una lista. La salida esperada sería algo como:

print("----------")

listaNombres = ["Franco", "Axl", "Slash", "Matt", "Duff", "Izzy"]

for rockero in listaNombres:
    if rockero.lower().startswith("f") or rockero.endswith("f"):
        print(rockero)

#Franco
#Duff

#  En el ejemplo anterior tenemos una lista (listaNombres) la cual contiene una serie de nombres (elementos iterables que luego, denominamos rockero)
#  debajo, aplicamos un bucle for para iterar sobre cada rockero diciendo: POR CADA rockero DE LA lista (listaNombres)...
#  Debajo del bocle for, vamos a desarrollar un condicional, es decir, POR CADA iteracion el bucle realizará una pregunta, una condicion. Entonces: POR CADA.... vamos a preguntar:
#  SI rockero.lower.startwith (si el elemento, en ese momento iterando, teniendo en cuenta todos sus caracteres en MINUSCULA, COMIENZA CON la letra f) O ese mismo elemento que se está iterando termina con f.
#  Por ultimo, lo imprimimos. 

print("----------")

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

# 1
# 2
# 3
# 4
# 5
# 6

# En el ejemplo anterior, vemos que no hace falta crear una variable que contenga el objeto iterable, ya que con ponerlo de esa forma está bien para iterar. Ahi vemos como decimos que POR CADA a, b (como diciendo, por cada par de elementos) DE LA LISTA, vamos a imprimir el primero y el segundo.

print("----------")

dicc = {"clave1": "10", "clave2": "100", "clave3": "1000"}

for item in dicc.keys(): #Depende el metodo que elijamos vamos a tener la clave o el valor. (keys / values o si queremos todo, colocar intems)
    print(item)

dicc = {"clave1": "10", "clave2": "100", "clave3": "1000"}

# for a, b in dicc.items(): 
#     print(a, b) 

lista_numeros = [10, 100, 90]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)

print("---------------------")

lista_numeros = [1, 2, 3, 4, 7, 6, 9] #impares=20  pares=12
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero

print(suma_pares)
print(suma_impares)