# # Mientras que el loop for se repite una cantidad de veces especifica, el bucle WHILE se va a repetir N cantidad de veces, es decir, se repetirá de forma indefinica SIEMPRE Y CUANDO una condicion se cumpla (puede que una condicion se cumpla por siempre, con lo cual, el bucle while caera en un bucle infinito)
    
# # La frase es: Se repiten MIENTRAS que se cumpla: (en ingles MIENTRAS se dice WHILE)

# # La sintaxis es:

# # vidas = 10

# # while vidas > 0:                                              === MIENTRAS una_condicion:
# #     print("el jugador todavia tiene vidas por jugar")         === Se ejecutará este codigo.

# monedas = 5

# while monedas > 0:
#     print(f"Tengo {monedas} monedas")
#     monedas -= 1
# else : print("No tengo mas dinero.")


# # En el siguiente ejemplo, vamos a ver la caracteristica principal del loop while ya que dicho loop tendrá lugar pura y exclusivamente dependiendo del usuario, si el usuario coloca S por toda la eternidad, será un loop infinito.

# respuesta = "s"

# while respuesta == "s" or respuesta == "S":
#     respuesta = input("Quieres continuar ?? (s/n): ")
# else:
#     print("Muchas gracias.")

# #En el siguiente ejemplo vamos a ver el metodo PASS. Simplemente no hace nada XD. En vez de colocar: print("acá va a ir algo"). Colocamos pass.

# # dia = "soleado"

# # while dia == "soleado":
# #     pass

# #Ahora vamos a ver BREAK, esto sirve para romper la iteracion. Por ejemplo en un input, podemos hacer que el programa se interrumpa una vez que demos match con alguna coincidencia. Por ejemplo:

# nombre = input("Por favor dinos tu nombre: ")

# for letra in nombre:
#     if letra == "n" or letra == "N": #Sin importar si se coloca n o N, a partir de esa letra no se mostrará. En este caso al poner Franco. La terminal mostrará Fra
#         break
#     print(letra)

# #Ahora vamos a ver CONTINUE, esto sirve para saltearnos una iteracion.

# apellido = input("Por favor dinos tu apellido: ")

# for letra in apellido:
#     if letra == "s" or letra == "S": #Sin importar si se coloca n o N, a partir de esa letra no se mostrará. En este caso al poner Franco. La terminal mostrará Fra
#         continue
#     print(letra)

# #En el ejemplo anterior, la terminar devolvería Roale, porque continuo omitiendo lo que le ordenamos.


numero = 50

while numero >= 0:
    print(numero)
    numero -= 1
    if numero % 5 == 0:
        print(f"El numero {numero} es divisible por 5")
    else:
        continue

 

