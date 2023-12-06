# Las funciones en Python no son distintas a las Fn en otros lenguajes, sirven para economizar codigo, para reiterar bloques sin necesidad de volver a escribir, y la sintaxis es la siguiente:

# Las funciones comienzan con una palabra reservada llamada def, recordar como algo que DEFINIMOS. 
# Luego de la palabra def vamos a colocar el nombre de la fn siempre en minuscula y sin espacios de separacion ya que para esto estan los guiones bajos.
# Por ultimo los parentesis que indican que es una funcion, dentro de ellos podemos pasar un parametro para luego hacer nuestra fn mas compleja
# Por ultimo y pegado al parentesis los dos puntos indicando que, todo lo que este por debajo, siempre y cuando respete la sangria, se tratará del cuerpo de la funcion, lo que se ejecutará cuando la invoquemos.

def mi_funcion(nombre):
    '''Esta funcion se encarga de imprimir un salido en pantalla'''
    print("Hola querido " + nombre)

mi_funcion("Franco") #Hola querido Franco
mi_funcion("Jose")   # Hola querido Jose


