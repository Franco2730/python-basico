#Ahora vamos a ver 6 metodos muy faciles de aprender:

# upper() - Pasar a mayúsculas
texto = "Este es el texto de Franco"
resultado = texto.upper() #Si quisieramos que solo un caracter fuera en mayuscula: texto[2].upper() = T
print(resultado) #ESTE ES EL TEXTO DE FRANCO

# lower() - Pasar a minúsculas:
texto2 = "Este es el texto de Franco"
resultado2 = texto2.lower()
print(resultado2) # "este es el texto de franco"

# split() - Separarlo en partes (lista). Si queremos que en vez de separar palabras de la lista con un espacio la tenemos que colocar entre()
#resultado3 = texto3.split("t") ['Es', 'e es el ', 'ex', 'o de Franco']
texto3 = "Este es el texto de Franco"
resultado3 = texto3.split()
print(resultado3) #['Este', 'es', 'el', 'texto', 'de', 'Franco']

# join() - Unir items usando separador
a = "aprender"
b = "python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])

print(e) # aprender python es genial. Si en la variable e le colocamos "-" quedaria: aprender-python-es-genial

# find() - Encontrar un sub-string. La unica diferencia con el metodo index, es que si con find buscamos un elemento que no se encuentre en nuestro
#str no nos devolvería un error como lo hacia Index. Devuelve un -1
texto4 = "Este es el texto de Franco"
resultado4 = texto4.find("s")
print(resultado4) # 1 - (la letra "s" se encuentra en la posicion 1 del texto4 )

# replace() - reemplazar un substring. Este metodo solicita dos parametros. El primer parametro, es la palabra que vamos a reemplazar y el 2do
#el str que irá en su lugar
texto5 = "Este es el texto de Franco"
resultado5 = texto5.replace("el texto", "la harley") #reemplazamos el texto, por: la harley
print(resultado5) # Este es la harley de Franco

texto6 = "Hola mundo, estamos aprendiendo metodos con Python"
resultado6 = texto6.replace("o", "$") #reemplazamos las o por el signo $
print(resultado6) #H$la mund$, estam$s aprendiend$ met$d$s c$n Pyth$n