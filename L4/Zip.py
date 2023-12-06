#Zip nos sirve para mezclar dos listas para devolver un tuple con la informacion junta: Una curiosidad, Si llegamos a agregar un nombre o una edad (y difiere por un elemento alguna de las dos listas) No sucederá nada, zip mezcla los elementos por posicion, cuando sobra uno, lo ignora
nombres = ["Franco", "Carina", "Mariano"]
edades = [30, 50, 57]

combinados = list(zip(nombres, edades))

print(combinados)

#[('Franco', 30), ('Carina', 50), ('Mariano', 57)]

print("--------------")

nombres2 = ["Lautaro", "Florencia", "Julia"]
edades = [28, 29, 8]
ciudades = ["Mendoza", "Buenos Aires", "Neuquen"]

otroCombinado = list(zip(nombres2, edades, ciudades))
print(otroCombinado)

#[('Lautaro', 28, 'Mendoza'), ('Florencia', 29, 'Buenos Aires'), ('Julia', 8, 'Neuquen')]

print("--------------")

nombres3 = ["Patricia", "Iris", "Juanmanuel", "Nicolas"]
edades3 = [55, 80, 29, 27]
ciudades3 = ["Orlando", "Mendoza", "Málaga", "Mendoza"]

combina2 = list(zip(nombres3, edades3, ciudades3))

for nombre3, edades3, ciudades3 in combina2:
    print(f"{nombre3} tiene {edades3} años y vive en la ciudad de {ciudades3}")

# Patricia tiene 55 años y vive en la ciudad de Orlando
# Iris tiene 80 años y vive en la ciudad de Mendoza
# Juanmanuel tiene 29 años y vive en la ciudad de Málaga
# Nicolas tiene 27 años y vive en la ciudad de Mendoza