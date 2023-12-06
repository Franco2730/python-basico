# En esta oportunidad vamos a ver un metodo llamado randint() que significa citar a un numero INT de forma RANDON
# Lo negativo es que dicho metodo no es propio de Python, si no, que corresponde a una libreria llamada RANDOM. Para llamar a un metodo de una libreria (paso a paso manual para importar un metodo) debemos decir: Desde tal libreria importa tal metodo. En este caso, deberiamos decir: "from random import randint" Aunque si vamos a usar muchos metodos de una libreria, lo conveniente es importarlos a todos como lo vemos a continuacion

from random import *  

aleatorio = randint(1, 100) #Devuelve un numero entero random entre los dos parametros que le brindamos. 67

aleatorio2 = uniform(1, 10) #Devuelve un numero decimal random entre los dos parametros que le brindamos. 2.599207684630059

aleatorio3 = round(uniform(1, 10),2) #Devuelve un numero decimal random entre los dos parametros que le brindamos, pero, a diferencia del anterior, acá aplicamos round para pedirle unicamente dos decimales al numero aleatorio. 4.97

aleatorio4 = random() #Random no pide parametros, simplemente devolverá un numero float del 0 al 1. 0.8221454549654729

colores = ['azul', 'oro', 'celeste', 'blanco']
aleatorio5 = choice(colores) #De la lista seleccionada, lo que hara choice es elegir un elemento por cada vez que se lo llame. azul

numeros = list(range(1, 42)) #Crea una lista del 1 al 41 ya que el 42 es no inclusivo, poner 43 de ultima.
shuffle(numeros) #A la lista que nosotros le asignemos, shuffle va a mezclar los elementos, ideal para juego de cartas.


print(numeros)