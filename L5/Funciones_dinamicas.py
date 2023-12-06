# Ahora vamos a complejizar las funciones implementando cosas dentro de ellas como pueden ser condicionales o bucles. La sintaxis no cambia mucho:

def sumar_todo( lista ):
    lista
    # loop for
    # return resultado_del_loop

sumar_todo([10, 100, 90, 800])

# Ahora vamos a elaborar una funcion que determine si el numero que le pasamos es de 3 sifras (por ejemplo) ESTO PUEDE SERVIR PARA EL DESAFIO DEL AHORCADO.

def chequear_3_cifras(numero):
    return numero in range(100, 1000) # Acá decimos que retornemos el resultado booleano de que si NUMERO (q pasamos por parametro) se encuentra IN el RANGE(de 100 a 1000) recordar que el range no es inclusivo asique solamente es del 100 al 999

# Si quisieramos agregarle un poco de complejidad, podriamos colocar una variable llamada suma = 586 + 402 y despues hacerle un print a esa variable y nos devolvera la respuesta booleana si el resultado de esa suma es de 999 o lo sobrepasa.

resultado = chequear_3_cifras(1000)
#print(resultado)

# Al tener que hacer el juego del ahorcado, debemos corroborar los elementos de una lista (aunque las letras sean invisibles antes de adivinarlas) una forma apropiada sería:

def chequear_lista(lista):

    for num in lista:
        if num in range(100,1000):
            return True
        else:
            pass

    return False

    # El flow del loop for fue: Primeramente, la funcion chequear_lista recibe por parametro una lista, lista a la cual, el bucle for estará iterando a continuacion
    # Al iterar sus elementos, el loop dice: POR cada num que este IN lista:
    # Por cada n de la lista, vamos a preguntar IF ese numero iterado está en el RANGE(de 100 a 1000).
    # Si esto es así, retornar True, caso contrario pasar. Al momento de pasar, pasa a iterar el siguiente elemento de la lista.
    # Cuando haya finalizado de iterar TODOS los elementos de la lista, retornara False.

resultado2 = chequear_lista([500, 632, 732, 942]) # True
resultado3 = chequear_lista([21, 32, 63, 42]) # False
resultado4 = chequear_lista([21, 32, 63, 9421]) # False

#print(resultado2)

# Ahora supongamos que queremos hacer lo mismo pero en vez de retornar si es True o False, necesitamos almacenar en un lugar los numeros que cumplan la condicion (estar en un rango)

def comprobar_lista(lista):

    almacen = []

    for n in lista:
        if n in range(100, 1000):
            almacen.append(n)
        else:
            pass

    return almacen
    
    
result = comprobar_lista([10, 100, 200, 5, 81, 196, 600, 1000]) 
print(result) # [100, 200, 196, 600]