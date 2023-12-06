from random import randint

intentos = 0
numero_secreto = randint(1, 100)
nombre = input("Dinos tu nombre: ")

print(f"Hola {nombre}, he pensado un número entre 1 y 100 \n Tienes 8 intentos para adivinar. Jugamos?")

# Para este jugo vamos a elegir el loop while ya que este tipo de bucle se repite tantas veces como la dinamica del juego lo necesite, o bien transcurran los 8 intentos o el usuario acierte el numero secreto.

while intentos < 8:
    estimado = int(input("Cuál es el número?: "))
    intentos += 1

    if estimado not in range(1, 100):
        print("Has elegido un numero fuera del rango del juego")
    elif estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi nùmero es mas bajo")
    else:
        print(f"Felicitaciones querido {nombre}!! Has adivinado en {intentos} intentos")
        break
     
if estimado != numero_secreto:
    print(f"Lo siento mucho, se han agotado los intentos, el número secreto era: {numero_secreto}")
            