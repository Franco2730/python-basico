'''
El programa que vamos a realizar es el famoso juego: "El ahorcado". Nuestro programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en la palabra oculta, pierde una vida. En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una en una, cada vez que el jugador elija una letra incorrecta.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra completa antes de perder todas las vidas, el jugador gana. Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas: Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que también vas a crear al comienzo. Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la palabra o no, para verificar si ha ganado o no, etc.
'''

# Importamos desde random un metodo llamado choice, esto nos permite elegir desde una lista un elemento aleatorio (para que el sistema elija una de esas palabras)
from random import choice 

palabras = ['Fisioterapeuta', 'Espasticidad', 'Charger', 'Auto', 'Libertad'] #Palabras para que el sistema elija aleatoriamente
letras_correctas = [] #Esta variable vamos a llevar la cuenta de la cantidad de letras correctas que ha encontrado el usuario
letras_incorrectas = [] #Esta variable vamos a llevar la cuenta de la cantidad de letras incorrectas que ha errado el usuario
intentos = 6 #Necesitamos inicializar la cantidad de intentos que va a tener el usuario. (comienza con 6 vidas)
aciertos = 0 #Esta variable es para llevar la cuenta de los aciertos y saber cuando el usuario ha ganado. 
juego_terminado = False #Esta variable determina si el juego ha finalizado. Comienza con false ya que, todavia no ha comenzado. 


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras) #La variable interna palabra_elegida que va a ser igual de lo que resulte del uso del metodo choise con la lista_palabras
    letras_unicas = len(set(palabra_elegida)) #Esta variable contendra cuantas letras distintas tiene nuestra palabra, sin importar las repeticiones.