'''
El programa que vamos a realizar es el famoso juego: "El ahorcado". Nuestro programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en la palabra oculta, pierde una vida. En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una en una, cada vez que el jugador elija una letra incorrecta.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra completa antes de perder todas las vidas, el jugador gana. Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas: Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que también vas a crear al comienzo. Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la palabra o no, para verificar si ha ganado o no, etc.
'''

# Importamos desde random un metodo llamado choice, esto nos permite elegir desde una lista un elemento aleatorio (para que el sistema elija una de esas palabras)
from random import choice 

palabras = ['coco', 'Libertad'] #Palabras para que el sistema elija aleatoriamente
letras_correctas = [] #Esta variable vamos a llevar la cuenta de la cantidad de letras correctas que ha encontrado el usuario
letras_incorrectas = [] #Esta variable vamos a llevar la cuenta de la cantidad de letras incorrectas que ha errado el usuario
intentos = 6 #Necesitamos inicializar la cantidad de intentos que va a tener el usuario. (comienza con 6 vidas)
aciertos = 0 #Esta variable es para llevar la cuenta de los aciertos y saber cuando el usuario ha ganado. 
juego_terminado = False #Esta variable determina si el juego ha finalizado. Comienza con false ya que, todavia no ha comenzado. 


# La sig fn va a elegir una palabra del array ya armado
def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras) #La variable interna palabra_elegida que va a ser igual de lo que resulte del uso del metodo choise con la lista_palabras
    letras_unicas = len(set(palabra_elegida)) #Esta variable contendra cuantas letras distintas tiene nuestra palabra, sin importar las repeticiones. Basicamente estamos diciendo. Queremos saber la CANTIDAD(len) de ELEMENTOS UNICOS(set) que tienga la variable: palabra elegida 

    # Vamos a retornar ambas variables para obtener esa info y salir de la funcion
    return palabra_elegida, letras_unicas

# Ahora tenemos que crear una funcion que le pida al usuario elegir una letra, dicha funcion se tendrá que repetir tantas veces sea necesaria hasta que el usuario gane o pierda. 

def pedir_letra():
    letra_elegida = '' # En esta variable vacía se irán agregando las letras elegidas por el usuario.
    letra_valida = False # Ahora tenemos que validar si el ingreso del usuario es algo aceptable y no es una palabra o n. Al principio  sera False hasta que ingrese algo que cambie dicho valor booleano. 
    ayuda_abecedario = 'abcdefghijklmnñopqrstuvwxyz' # Esto lo usaremos para decir: Si la letra elegida por el usuario esta acá. Es GOD

    # Vamos a crear un loop que le pida al usuario una letra y se lo pregunte tantas veces la letra no sea valida 
    while not letra_valida: # MIENTRAS QUE NO letra_valida (mientras que sea falso)
        
        letra_elegida = input('Por favor, elige una letra: ').lower() # la variable letra_elegida contendrá el ingreso del usuario a traves del input y ademas, transformamos el ingreso a minuscula con .lower() sin importar si el usuario ingresó min o mayu. Por las dudas lo transformamos.

        
        if letra_elegida in ayuda_abecedario and len(letra_elegida) == 1: # Para corroborar que el usuario no ingreso una palabra o un número vamos a decir: IF letra_elegida está IN ayuda_abecedario AND el LEN de letra_elegida es 1: letra_valida pasará a tener el valor de True
            letra_valida = True
        else: # Si no se cumple lo anterior...
            print('No has elegido una letra correcta') # aparecerá esto como respuesta y volveremos a entrar en el loop.
        
    return letra_elegida # devolvemos la letra elegida. 

# La proxima función se encargara de mostrar en pantalla los guiones que representan la letra que el usuario debe adivinar. (AUTO = _ _ _ _)

def mostrar_nuevo_tablero(palabra_elegida): #

    lista_oculta = []

    for letra in palabra_elegida: # FOR cada letra IN palabra_elegida nos vamos a preguntar:
        if letra in letras_correctas: # IF letra se encuentra IN letras_correctas
            lista_oculta.append(letra) # Si la letra se encuentra en letras_correctas. A la variable inicializada [] llamada lista_oculta le agregaremos esa letra.
        else: # Caso contrario:
            lista_oculta.append('_') # Le agregaremos simplemente un guión bajo. 
    
    print(' '.join(lista_oculta)) # Vamos a unir todos los elementos de lista_oculta separados por un espacio vacio(' ')

# La siguiente funcion es para chequear si la letra que ha elegido el usuario se encuentra o no y cada vez que chequee esto, va a alimentar las listas de letras correctas o incorrectas. Se encargará de quitar una vida al usuario, se encargará de determinar si el usuario a ganado o perdido. 
    
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print('Te has quedado sin vidas')
    print(f"La palabra oculta era: {palabra}")

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('Felicitaciones. Has encontrado la palabra oculta !!!')

    return True


# -------

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabras)
    print('\n')
    print('letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')

    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado

