#Una actualización que tiene python a partir de su modelo 3.10 es el MATCH. 
#Antes, podiamos hacer if, elif y else de la siguiente manera:

serie = "N-03"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Motorola")
elif serie == "N-03":
    print("Nokia")
else:
    print("Vaya a saber que es")

#Imprimirá Motorola.

#Con la actualización de python, podemos encontrar una similitud con Switch en JS.

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Claro perri con MATCH")
    case "N-03":
        print("Nokia")
    case _:
        print("El else en match es: case (espacio + guion bajo)")
        

# Aunque tiene algo mas para ofrecer, y esto es que puede recorrer cosas:

alumno = {'alumno': 'Franco',
          'edad': 30,
          'ocupacion': 'Estudiante'}

pelicula = {'titulo': 'Rapido y furioso',
            'ficha_tecnica': {'actores': 'Vin diesel, Paul Walker',
                              'director': 'Un capo'}}
elementos = [alumno, pelicula, "libro"]

for elemento in elementos:
    match elemento:
        case {'alumno': alumno,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Soy yo!!")
            print(alumno, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'actores': actores,
                                'director': director}}:
            print("Esa es mi movie")
            print(titulo, actores, director)
        case _:
            print("No se que es esto.")