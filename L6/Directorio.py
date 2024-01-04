# Importa la clase Path de la biblioteca pathlib
from pathlib import Path
import os

#getcwd traducido sería: obtener directorio de trabajo actual. Y hace justamente eso.
ruta = os.getcwd() #c:/Users/54261/OneDrive/Escritorio/Carpetas-proyectos-semana/python-basico/L6/Directorio.py

#chdir significa Change directori - Cambiar directorio.
ruta2 = os.chdir(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6 - otro-directorio')

archivo = open('Otro_archivo.txt')

#print(archivo.read())

# Ahora vamos a utilizar el metodo makedirs que, como su nombre lo indica, crea un directorio: con la siguiente linea se creara una nueva carpeta llamada MakeDirs
# ruta3 = os.makedirs(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\MakeDirs') 

# A continuación vamos a eliminar un directorio con el metodo rmdir que significa: remove directori.
# os.rmdir(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\MakeDirs')

#Ahora vamos a leer un archivo que se encuentre en otro directorio.
# otro_archivo = open(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6 - otro-directorio\Otro_archivo.txt')
# print(otro_archivo.read())

# Ahora nos vamos a ayudar de la libreria pathlib 
# Define una ruta de directorio utilizando la clase Path
carpeta = Path(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6 - otro-directorio')
# Combina la ruta del directorio con el nombre del archivo 'Otro_archivo.txt' para obtener la ruta completa del archivo
archivo = carpeta / 'Otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

# Finalmente, se debe cerrar el archivo después de usarlo para liberar los recursos
mi_archivo.close()

'''Una explicacion detallada de este último ejercicio:

    from pathlib import Path: Importa la clase  Pathde la biblioteca pathlib, que proporciona una interfaz orientada a objetos para manipular rutas de archivos y directorios de manera más eficiente.

    carpeta = Path(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6 - otro-directorio'): Crea un objeto Path llamado carpeta que representa la ruta del directorio especificado.

    archivo = carpeta / 'Otro_archivo.txt': Combina la ruta del directorio (carpeta) con el nombre del archivo 'Otro_archivo.txt' utilizando el operador / proporcionado por pathlib. Esto crea un objeto Path que representa la ruta completa del archivo.

    mi_archivo = open(archivo): Abre el archivo especificado en modo lectura ('r') y asigna el objeto de archivo resultante a la variable mi_archivo.

    print(mi_archivo.read()): Imprime el contenido del archivo leído utilizando el método read() del objeto de archivo.

    mi_archivo.close(): Es importante cerrar el archivo después de utilizarlo para liberar los recursos del sistema. En este caso, no está explícitamente cerrado en el código proporcionado, pero es una buena práctica cerrar el archivo manualmente después de su uso, o se puede utilizar un bloque with para asegurar que se cierre automáticamente cuando ya no sea necesario.'''



'''
                                Dada la siguiente ruta, ¿qué devolverá os.path.basename(ruta)?

                                ruta = 'C:\\Users\\Desktop\\documento.txt'

                                Devolverá documento.txt ya que es la base
'''