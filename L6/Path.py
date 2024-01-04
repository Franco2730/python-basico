'''
Path es una clase que proporciona una forma más intuitiva y fácil de trabajar con rutas de archivos y directorios en diferentes sistemas operativos. Es una forma más moderna y segura de trabajar con archivos y directorios en Python.
Path es una herramienta útil para trabajar con rutas de archivos y directorios de forma segura y confiable. Con Path puedes crear y abrir archivos, crear y eliminar directorios, y en general, manipular rutas de una manera mucho más intuitiva y fácil de leer que utilizando otras herramientas.
'''
from pathlib import Path
'''
Algo curioso que puede hacer Path es construir un objeto con el formato de ruta de acceso con nombres aleatorios que nosotros le otorgemos:

'''

base = Path.home()
# C:\Users\54261\America\Argentina\Mendoza\Lujan\Chacras.txt :
guia = Path(base, "America", "Argentina", Path("Mendoza", "Lujan", "Chacras.txt")) 

# C:\Users\54261\America\Argentina\Mendoza\Lujan\Cacheuta.txt : (Con el metodo with_name, cambiamos el ultimo elemento, el nombre)
guia2 = guia.with_name("Cacheuta.txt")
# print(guia)
# print(guia2) 

# ----
'''Con el metodo parent vemos que omite el nombre de lo que sería nuestro archivo, su nombre... .parent es una instancia de Path que devuelve el antecesor mas inmediato de una ruta de archivo determinada, en este caso devuelve el directorio que tiene a Sanford y este es Orlando'''
unaGuia = Path(base, "America", "Estados_Unidos", Path("Orlando", "Sanford.txt"))
# print(unaGuia.parent) #C:\Users\54261\America\Estados_Unidos\Orlando
# print(unaGuia.parent.parent) #C:\Users\54261\America\Estados_Unidos
# print(unaGuia.parent.parent.parent) # C:\Users\54261\America

# ----

# En el siguiente ejercicio, tomamos una carpeta llamada Europa y la colocamos en el home de la ruta (C:\Users\54261) dicha carpeta contiene algunos archivos y carpetas que a su vez contienen mas archivos. Lo que estamos haciendo en el ejercicio es crear una variable que contenta la ruta y luego iteramos esa ruta buscando TODOS (**/*) los archivos que terminen en .txt Cuando ya hicimos eso simplemente imprimimos esos archivos que iteramos.

# ejer = Path(Path.home(), "Europa")

# for txt in Path(ejer).glob("**/*.txt"):
#     print(txt)

# ----
    
'''Ahora vamos a ver el metodo relative devuelve un nuevo objeto Path relacionado con el argumento determinado. En conclución, el objeto Path es un componente muy importante de la biblioteca estandar de Python que nos permite manipular rutas de sistema de archivo de forma rapida y en cualquier sistema operativo. '''

otraGuia = Path("America", "Argentina", "Mendoza", "Lujan", "Chacras.txt")

# La variable enChacras lo que va a contener es: al Path otraGuia aplicando el metodo relative_to, y dentro del relative_to colocamos un Path QUE ARRANQUE DESDE: America
enChacras = otraGuia.relative_to(Path("America")) # Argentina\Mendoza\Lujan\Chacras.txt
# print(enChacras)

# Si creamos otra variable que sea relativ Pat desde Mendoza, se mostrara lo que arranque DESPUES de mendoza: Lujan\Chacras.txt
enMendoza = otraGuia.relative_to(Path("America", "Argentina", "Mendoza"))
print(enMendoza) 


'''
Ejercicio 1:

Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
Recuerda importar Path del módulo pathlib, y utilizar el método home()

RTA:

from pathlib import Path

ruta_base = Path.home()

----

Ejercicio 2:

Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

--Curso Python
|
|_____Día 6
|
|_____________practicas_path.py

Almacena el directorio obtenido en la variable ruta. No olvides importar Path.

RTA:

from pathlib import Path
ruta = Path("Curso Python", "Día 6", "practicas_path.py")


Ejercicio 3:

Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

 ___home(directorio base)
|
|____Curso Python
|
|_______Día 6
|
|_____________practicas_path.py


Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.

from pathlib import Path
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")
'''
