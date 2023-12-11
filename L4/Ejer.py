# Ejercicio 1:

'''Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio'''


def devolver_distintos(num1, num2, num3):
    
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]

    if suma > 15: # Si el resultado de la suma de los parametros es mayor a 15:
        return max(lista) # Vamos a returnar de la lista, el mayor elemento con la ayuda del metodo max.
    elif suma < 10: # Si el resultado de la suma de los parametros es menor a 10:
        return min(lista) # Vamos a returnar de la lista, el menor elemento con la ayuda del metodo min.
    else:
        lista.sort() # Ya que el usuario puede haber brindado los elementos desordenados, con sort los ordenaremos de menor a mayor
        return lista[1] # Como nuestra lista ya está ordenada, retornaremos el elemento del medio.
    
#print(devolver_distintos(20, 5, 7)) # max - 20
#print(devolver_distintos(3, 2, 4)) # min - 2
#print(devolver_distintos(7, 2, 4)) # el valor intermedio es 4. 

print("---------------------------------------------------------------------------")

# Ejercicio 2:

'''Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']'''

def letras_unicas(palabra):

    mi_set = set() # Usando el metodo set, nos aseguramos que las letras sean unicas, pues dicho metodo no acepta elementos repetidos.

    for letra in palabra: # Acá pedimos que por cada letra que haya en palabra:
        mi_set.add(letra) # la agreguemos a mi_set(la letra iterada)

    mi_lista = list(mi_set) # creamos una nueva variable con el contenido en forma de lista, dicho contenido son las letras que previamente guardamos
    mi_lista.sort() # Volvemos a utilizar nuestro metodo sort que sirve para ORDENAR de MENOR a MAYOR y ALFAÉTICAMENTE 

    return mi_lista

#print(letras_unicas("aadoonddde")) # ['a', 'd', 'e', 'n', 'o'] 

print("---------------------------------------------------------------------------")

# Ejercicio 3:

'''Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False'''


def funcion_muchos_argumentos(*args): #De esta manera aceptamos multiples argumentos (*args)

    contador = 0 # Gracias a esta variable podemos organizar nuestra tarea, debido a que nos sirve como guia para completar la totalidad de los argumentos.

    for numero in args: # FOR cada NUMERO IN ARGS vamos a preguntarnos...

        if args[contador] == 0 and args[contador + 1] == 0: # IF ARGS en la posicion cero (ya que asi lo definimos anteriormente) es igual a 0, AND ARGS es igual a 0 MAS 1 (es decir uno) es igual a cero. Acá estamos comparando los elementos en la posicion 0 y 1. De cumplirse esta condicion...
            return True # ... devolvemos True
        else: # Caso contrario
            contador += 1 # sumamos 1 a lo ya existente en nuestra variable contador. Esto es clave para que en la proxima iteración dejemos de analizar la posicion 0 y 1 y analicemos 1 y 2, si eso tampoco se cumple, nuevamente se le sumará 1 valor a la variable contador y al comenzar nuevamente el condicional, se estará evaluando las posiciones 2 y 3. Hasta terminar con todos los elementos en el argumento.
    
    return False

print(funcion_muchos_argumentos(1, 2, 3, 4, 5, 6, 7, 8, 9)) # False
print(funcion_muchos_argumentos(1, 2, 3, 4, 0, 7, 0, 9)) # False Existen 2 elementos 0. Pero no estan juntos y la condicion AND pide que ambas condiciones se cumplan.
print(funcion_muchos_argumentos(0, 2, 3, 0, 0, 7, 8, 9, 0)) # True

print("---------------------------------------------------------------------------")

# Ejercicio 4:

'''Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos'''

def contar_primos(num):
    numeros_primos = []

    