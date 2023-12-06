#Los str son inmutables, se pueden concatenar, tambien puede contar con mas de una linea, podemos verificar si contiene un caracter especifico
#podemos corroborar el largo de sus caracteres.

#Con esto nos referimos a que es inmutable = 'str' object does not support item assignment
#nombre = "Carina"
#nombre[0] = "K"
#print(nombre)

#Concatenar:
n1 = "Kari"
n2 = "na"
print(n1 + n2) #Karina

#Multiplicacion
no1 = "Fran"
no2 = "co"
print(no1*10)#FranFranFranFranFranFranFranFranFranFran

#multiplicar lineas:
poema = """Mil pequeños peces blancos
como si hirviera 
el color del agua"""
print(poema) #Se imprime de la misma forma que lo escribimos. Siempre utilizando 3 comillas

#Saber si en un str existe una palabra o un caracter:
poema2 = """Mil pequeños peces blancos
como si hirviera 
el color del agua"""
print("agua" in poema2) #true (porque agua ESTÁ en el poema2)
#print("fuego" not in poema2) #true (porque fuego NO ESTA en el poema2)

#Saber el largo del str:
poema3 = """Mil pequeños peces blancos
como si hirviera 
el color del agua"""
print(len(poema3)) #62