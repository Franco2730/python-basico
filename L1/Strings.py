'''Los strings son un conjunto de elementos que conforman un solo elemento, todo lo que se encuentre entre comillas("" / '') será tratado como string. Todo puede ser un string, incluso los numeros, pero estos perderán su magia en cuanto a las matematicas boton'''

# En el siguiente ejemplo, los numeros no serán tratados como tal, lo se podran sumar, estarán siendo concatenados (juntados)
print('100 + 50') # 100 + 50

# Que sucede si queremos colocar comillas ? Se podría dificultar debido a que si colocamos comillas puede que nuestro amigo Python determine que estamos cerrando nuestro string. Hay varias formas de resolver esto:
print(" Mi nombre es 'Franco', y el tuyo ? ") # Agregar comillas simples si abrimos y cerramos con dobles o lo contrario de ser necesario.
print(" Mi nombre es \"Franco\", y el tuyo ? ") # La barra invertida dice: El siguiente caracter, no lo tomes en cuenta como tal, es un caracter textual.
print(" Mi nombre es Franco\n, y el tuyo ? ") # Si colocamos la barra n estamos pidiendo un salto de linea.
print(" Mi nombre es Franco\n, \t y el tuyo ? ") # \t significa tabular.