'''En esta unidad, estaremos viendo algo super importante, algo con lo que, más adelante, podremos hacer cosas muy geniales, divertidas y asombrosas. Estaremos viendo como manipular archivos existentes en tu ordenador.'''

'''Como primera tarea, debemos tener un archivo txt como el que se encuentra en esta carpeta. Ahora si, a jugar !!!'''

# Primero vamos a crear una variable que contendrá un metodo llamado open y que tendra como parametro la ruta para llegar a ese archivo. La ruta debe estar completa y antes de la misma, debemos colocar una letra r (read)
mi_archivo = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba.txt') 

# Cuando ya abrimos ese archivo simplemente, a la variable que lo contiene, le aplicamos el metodo read() y todo esto lo mandamos a la consola
# print(mi_archivo.read())

# Si quisieramos leer únicamente la primer linea deberiamos usar el metodo readline()
primera_linea = mi_archivo.readline()
#print(primera_linea.upper()) # - Hola, soy la primera linea de codigo !!! y upper seria para que se imprima en mayuscula. 

primera_linea = mi_archivo.readline()
#print(primera_linea) # - Y yo... Bueno, no es tan malo el segundo lugar.

primera_linea = mi_archivo.readline()
#print(primera_linea) # - Vaya, he quedado en tercer lugar.


primera_linea = mi_archivo.readline()
#print(primera_linea) # - Oye, oye, no te quejes número 3... Aquí estoy yo.. 

# Importante, en consola siempre se imprimirá todo con un salto de linea y esto es debido a que el editor lee el archivo txt de forma textual, y habiendo una linea debajo de la otra, toma ese "ENTER" como un salto de linea, para corregir esto, de ser necesario, debemos hacer uso del metodo: rstrip():
# print(primera_linea.rstrip()) => de esa forma, aparecera pegado por debajo (igual que en el archivo txt)


#Por que al colocar el mismo comando, citando la misma variable se imprimen lineas siguientes y no siempre la misma ?? Simplemente cuando citamos al metodo readline, lo que el sistema hace es hacer un puntito en la linea que mostrará y, automaticamente, si repetimos el proceso, para el programa la primera linea será la siguiente (la que no tenga ese puntito)


'''Otro metodo es parecido al anterior pero en plural: readlines() esto devuelve todo pero como UNA LISTA donde cada oración es un elemento'''

mi_archivo2 = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba.txt') 

todas_oraciones = mi_archivo2.readlines() # ['- Hola, soy la primera linea de codigo !!!\n', '- Y yo... Bueno, no es tan malo el segundo lugar.\n', '- Vaya, he quedado en tercer lugar.\n', '- Oye, oye, no te quejes número 3... Aquí estoy yo.. ']

todas_oraciones = todas_oraciones.pop() # - Oye, oye, no te quejes número 3... Aquí estoy yo.. (recordando que el metodo pop excluye a todas dejando el ultimo elemento.)

print(todas_oraciones)#



# Es una muy buena practica que siempre, siempre utilicemos el metodo close() para que no vayamos a ocupar memoria en vano.
mi_archivo.close()
mi_archivo2.close()
