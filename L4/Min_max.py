#Esto sirve para detectar el elemento mas alto y el mas bajo. Funciona tanto con elemento numericos y alfanumericos. Ejemplo:

lista = [58, 96, 72, 64, 35]

menor = min(58, 96, 72, 64, 35) #Podriamos usar cualquier elemento iterable
print(menor) #35

mayor = max(58, 96, 72, 64, 35) 
print(mayor) #96

print(f"El menor es: {min(lista)} y el mayor es: {max(lista)}") #El menor es: 35 y el mayor es: 96