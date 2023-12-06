texto = input("Dime una frase a elección:")
letras = []

texto = texto.lower()

letras.append(input("Ingrese la primera letra").lower())
letras.append(input("Ingrese la segunda letra").lower())
letras.append(input("Ingrese la tercera letra").lower())

print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida '{cantidad_letras1}' veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida '{cantidad_letras2}' veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida '{cantidad_letras3}' veces")

print("\n")
print("Cantidad de palabras")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")


print("\n")
print("Letras de inicio y de fin")
letra_inicio = texto[0]
letra_fin = texto[-1]

print(f"La primera letra es: {letra_inicio} y la ultima letra es: {letra_fin}")

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(texto_invertido)

print("\n")
print("Buscando la palabra Python")
buscar_python = 'python' in texto
dicc = { True: "si", False: "no" }
print(f"La palabra 'Python' {dicc[buscar_python]} se encuentra en el texto")