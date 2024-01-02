'''En la clase pasada vimos como modificar el archivo pero unicamente en las variables de nuestra computadora, ahora es momento de modificar el archivo original, modificar nuestro querido archivo prueba.txt'''

'''En la clase de EntradaSalida utilizamos el metodo open para abrir dichi archivo y a este no le pusimos ningun tipo de parametro mas que el path de nuesto txt, En realidad open recibe 2 parametros ('Elnombredelarchivo.txt', modo_apertura) ¿Qué es el modo de apertura? se refiere a que queremos hacer con el archivo. 
 Los tres modos de apertura son:

    mi_archivo = open('archivo.txt','r') - Modo de solo lectura. Si usamos el metodo open con la 'r' como segundo parametro, no podremos hacer modificaciones sobre dicho documento, solo lee su contenido.

    mi_archivo = open('archivo.txt','w') - Modo de solo escritura. Si usamos la 'w' y el archivo.txt ya existe es vaciado (se resetea desde 0) y si no existe se lo crea.

    mi_archivo = open('archivo.txt','a') - Modo de solo escritura al final del archivo. Cuando utilizamos la 'a' como segundo parametro, se crea el archivo.txt (en caso de que no exista) y si ya existe, el cursor se posiciona al final del archivo para salvar los cambios que en el se alojen. No se borrará el contenido existente. 
    '''

archivo = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba1.txt', 'w')

archivo.write('Soy el nuevo texto\n') #De esta forma se va a crear un archivo llamado prueba1.txt con el contenido: 'Soy el nuevo texto'

# ----

archivo2 = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba.txt', 'w')

archivo2.write('Creo que he borrado todo') #De esta forma se va a borrar todo lo que había en el archivo para escribir: 'Creo que he borrado todo'

# ----

archivo3 = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba1.txt', 'a')

archivo3.write('''Soy 
el nuevo 
texto''') #De esta forma se va a crear un archivo llamado prueba1.txt con el contenido: 'Soy el nuevo texto' Para lograr un salto de linea se podria colocar \n o 3 comillas al principio y al fin como en el ejemplo.

# ----

#En el siguiente ejemplo, vamos a utilizar el metodo writelines, que vendria siendo como el metodo de la clase pasada: readlines, pero este es para escribir. No se utiliza mucho ya que, nosotros le tenemos que brindar un arreglo con str y dicho metodo concatenará todas las cadenas juntas.

archivo4 = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba4.txt', 'w')
archivo4.writelines(['Hola', 'mundo', 'here', 'i"m']) #Holamundoherei"m

# ----

#Como dijimos, la manera anterior no es muy utilizada, porque si quisieramos escribir un string por cada linea, el metodo writelines no nos ayuda, en su lugar, podriamos idear un codigo que por cada iteracion a cada elemento le agregue un salto de linea: 
archivo5 = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba5.txt', 'w')
lista = ['Hola', 'mundo', 'here', 'i"m'] 

for palabra in lista: # FOR cada palabra IN lista...
    archivo5.writelines(palabra + '\n')  # en el archivo abierto ARCHIVO5 vamos a escribir(cada palabra iterada del punto anterior mas un salto de linea)

'''Hola
mundo
here
i"m
'''

#----

# A continuación, vamos a agregar una linea al archivo anterior, en vez de reescribir con 'w', simplemen te agregamos al final con 'a'

archivo6 = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba5.txt', 'a')
lista = ['Feliz 2024 !!'] 

for palabra in lista: # FOR cada palabra IN lista...
    archivo5.writelines(palabra + '\n')  # en el archivo abierto ARCHIVO5 vamos a escribir(cada palabra iterada del punto anterior mas un salto de linea)

'''
Hola
mundo
here
i"m
Feliz 2024 !! (Se agregó esta linea al final)
'''


archivo.close()
archivo2.close()
archivo3.close()
archivo4.close()
archivo5.close()

