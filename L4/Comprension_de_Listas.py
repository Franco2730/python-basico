palabra = "Python"
lista = []

for letra in palabra:
    lista.append(letra) #Acá pedimos que por cada letra que se encuentre en palabra, se agrege a lista. Devolviendo: 
print(lista) # ['P', 'y', 't', 'h', 'o', 'n']

# Con comprension de listas, la misma tarea que hicimos arriba podria ser algo como:

palabra2 = "Harley Davidson"
lista2 = [letra for letra in palabra2] #Lista va a contener, cada letra de las letras que compongan a palabra2

print(lista2) # ['H', 'a', 'r', 'l', 'e', 'y', ' ', 'D', 'a', 'v', 'i', 'd', 's', 'o', 'n']

pies = [10, 20, 30, 40, 50]
metros = [n / 3.281 for n in pies]

print(metros)
