'''pathlib es una librería de Python que te proporciona una forma amigable y consistente para trabajar con rutas de archivo en tu computador.'''
'''PureWindowsPath significa algo así como: Ruta de wuindows pura y sirve para transformar cualquier ruta que tengamos en ua ruta de wuindows'''
from pathlib import Path, PureWindowsPath

# En vez de abrir el archivo con el metodo open y leerlo con readlines, utilizamos, gracias a la libreria pathlib Path (por open) y read_text (por readlines) darnos cuenta que no utilizamos ni open ni close para seguridad de memoria por los archivos.

archivo = Path(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba.txt') 

archivo2 = Path(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba.txt') 

archivo3 = Path(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba.txt') 

archivo4 = Path(r'C:\Users\54261\OneDrive\Escritorio\Carpetas-proyectos-semana\python-basico\L6\prueba.txt') 

#print(archivo4.stem) # prueba --> Nos devuelve el nombre (sin la terminación) del archivo.
#print(archivo3.suffix) # txt --> Nos devuelve el sufijo (terminación) del archivo.
#print(archivo2.name) # prueba.txt --> Nos devuelve el nombre (con la terminación) del archivo. 
#print(archivo.read_text()) # Creo que he borrado todo --> Nos devuelve el contenido del archivo. 

'''Vamos a hacer un if preguntando si el archivo NO existe con un metodo que, justamente, sirve para eso. Este metodo es exists()'''

# if not archivo.exists():                  # IF NOT ARCHIVO EXISTE:
#     print("Este archivo no existe")       # PRINT ....
# else:                                     # ELSE si existe...
#     print("Uh, genial !! Lo voy a leer.") # PRINT ....

# ----
    
'''Vamos a utilizar el metodo PureWindowsPath que, como ya dijimos, serviria por ejemplo para transformar una ruta de MAC en una ruta para wuindows'''

rute_wuindows = PureWindowsPath(archivo)
print(rute_wuindows)