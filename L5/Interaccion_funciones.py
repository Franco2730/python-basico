from random import shuffle
# Como ya sabemos, las funciones son bloques de codigo a los que podemos invocar desde cualquier lugar de nuestro codigo para que cumplan su cometido. 
# En esta clase vamos a ver como relacionar muchas funciones para que se comuniquen entre si. Vamos a realizar un pequeño juego que es el de los palitos en la mano.
# Este juego consiste en que una persona muestra unos cuantos palitos en su puño cerrado (dejando ver una parte de estos) pero uno de ellos es mas corto, pues, a como lo vemos no se nota la diferencia. El que agarre el palito mas corto, pierde. 


# Lista inicial: Acá vamos a crear la lista con todos los palitos.
palitos = ['-', '--', '---', '----']

# Mezclar palitos: Para que no se encuentren en orden.
def mezclar(lista):
    shuffle(lista)
    return lista

print(mezclar(palitos))

# Funcion del juego: Le pediremos al usuario que elija uno de los palitos. 
def probar_suerte():
    intento = ''

    while intento not in['1', '2', '3', '4']:
     intento = input("Elija un palito (número del 1 al 4)")
    
    return int(intento)

intento1 = probar_suerte()
print(intento1)
# Comprobamos si el intento es exitoso o no.
def chequear_intento(lista, intento):
   if lista[intento - 1] == '-':
      print("Lo siento, te ha tocado el mas chiquito")
   else:
      print("Esta vez te has salvado")
   print(f"Te ha tocado {lista[intento - 1]}")



palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)