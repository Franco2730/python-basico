#Index o indice. Como sabemos, los string son una cadena de caracteres que comienzan por el número 0, los espacios y signos especiales tambien
#ocupan un indice.
#Index nos sirve para saber la posicion de algun caracter.
#Para saber en que posicion se encuentra una determinada letra del string, sería algo así
#Si eligieramos rindex, buscaria de izq a derecha. Index acepta dos 3 parametros, el primero es obligatorio, los otros dos son opcionales
#y es informacion que podriamos colocar, desde donde hasta donde queremos buscar, no es inclisivo, con lo cual, si decimos hasta la pos 10, no se tomara en cuenta
mi_texto = "hola franco, te deseo mucha suerte"
respuesta = mi_texto.index("s") # 18
print(respuesta)

#Por el contrario si queremos brindar una posicion y que nos muestre que letra hay en esta:
mi_texto2 = "hola franco, te deseo mucha suerte"
respuesta2 = mi_texto2[18] #s
print(respuesta2)