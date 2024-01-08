'''
Antes de comenzar, es necesario que crees en tu ordenador un directorio en la carpeta
base de tu ordenador, con una carpeta llamada Recetas, que contiene cuatro carpetas y cada
una de ellas contiene dos archivos de texto. Dentro de los archivos puedes escribir lo que
quieras, puede ser la receta en sí misma o no, pero eso no es importante para este ejercicio. Lo
importante es que escribas algo para poder leerlas cuando haga falta o, si prefieres, también
puedes directamente descargar y descomprimir el archivo adjunto a esta elección y ubicarlo en
tu directorio raíz si no tienes ganas de crearlo tú mismo.
Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
estas opciones que tenemos aquí:
1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.
3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.
4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar
5. La opción 5, le va a preguntar qué categoría quiere eliminar
6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.
Este programa tiene algunas cuestiones importantes a considerar:
- Cada vez que el usuario realice exitosamente cualquiera de sus opciones, el programa le
va a pedir que presione alguna letra para poder volver al inicio, por lo que el código se
va a repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo
el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se
cumpla la condición de que la elección del usuario sea 6
- Sería genial que cada vez que el usuario vuelva al menú inicial, la consola limpie la
pantalla para que no se acumulen las ejecuciones anteriores. Recuerda que cuentas con
system para poder reiniciar la pantalla y comenzar a mostrar todo desde cero.
- Si bien te he enseñado muchos métodos para administrar archivos, para este ejercicio
vas a necesitar algunos que aún no has visto, pero que están incluidos en los objetos con
los que hemos estado trabajando, por lo que en ocasiones deberás buscar entre los
métodos que trae Path, por ejemplo, leer la documentación y aprender a implementarlo.
Yo sé que sería mucho más fácil que yo te enseñe todo acerca de cada uno de los
métodos, pero recuerda que también es importante que a medida que avanzamos vayas
aprendiendo a gestionar tu propio aprendizaje. Es parte de la vida real y cotidiana del
programador en el mundo en que vivimos.
- Utiliza muchas funciones, todas las que creas necesario. Las funciones ayudan a
compartir, mentalizar el código y hacerlo mucho más dinámico, ordenado, repetible y
más fácil de mantener.
- Recuerda comenzar con un diagrama de flujos o un gráfico hecho a mano que te permita
visualizar con más facilidad el árbol de decisiones que necesitas ejecutar en tu código.
Sin eso te vas a enredar más rápido de lo que crees y se te va a complicar bastante.
- Y, por último, no te frustres si no logras hacerlo o completarlo. Si logras hacer una parte,
un par de funciones, algunas cosas sí y otras no, está muy bien. Siempre estamos
aprendiendo y parte de aprender es no saber. 

Mi recomendación es que, ya que empezamos a ampliar nuestro espectro de conocimiento y los proyectos se volverán cada vez más ambiciosos, implementar técnicas que te ayudarán en el proceso de elaboración. Ten en cuenta que, a partir de ahora, los proyectos que te presentaré y los que tendrás en tu día a día, conllevaran una estructura de datos mas compleja y elaborada con lo cual:
 Te animo a que diagrames los procesos en un papel, el paso a paso de lo que debe realizar tu código. “Yo debo limpiar mi casa si mis amigos hacen mucho desorden”

1. Estado Inicial: "La casa de Franco está limpia"
   |
2. Condición: ¿Mis amigos hacen mucho desorden?
   |
3. Opción 1: Sí, mis amigos hacen mucho desorden
   |
4. Acción: Debo limpiar mi casa
   |
5. Resultado Final: "Mi casa está limpia de nuevo"

O también puedes utilizar alguna de estas paginas / programas: (cortesía de ChatGPT)

1.	Draw.io: Es una herramienta en línea gratuita que te permite crear diagramas de manera fácil. Puedes elegir la categoría "Flowchart" para representar tus estructuras de datos o árboles de decisión.
2.	Lucidchart: Similar a Draw.io, Lucidchart es otra herramienta en línea que te permite crear diagramas de flujo y otros tipos de diagramas de manera colaborativa.
3.	Microsoft Visio: Si tienes acceso a Microsoft Office, Visio es una opción robusta para crear diagramas profesionales, incluyendo diagramas de estructuras de datos.
4.	yEd Graph Editor: Es una aplicación de escritorio gratuita que te permite crear fácilmente diagramas, incluyendo diagramas de árboles y estructuras de datos.
5.	MindMeister: Aunque está diseñado para mapas mentales, también puedes utilizarlo para representar estructuras de datos y relaciones.
'''

# Importamos los modulos que vamos a necesitar:
import os  # Modulo para navegar entre nuestras carpetas
from pathlib import Path  # El objeto path es esencial para construir rutas
from os import system  # System nos permite limpiar la pantalla. Es un detalle visual

# Ahora debemos crear en el menu de inicio, este debe hacer:
# Dar la bienvenida.
# Informar donde se encuentran los archivos.
# Luego informar cuantas recetas tenemos.
# Mostrar el menu.

mi_ruta = Path(Path.home(), "Recetas")  # Esta variable contendrá la ruta a nuestra carpeta madre y como segundo parametro, el elemento que queremos detallar. Aquí tendremos la ruta directa a nuestra carpeta Recetas y su contenido.


def contar_recetas(ruta):  # Esta función se encargará de contar las recetas. Necesita un parámetro que será la ruta
    contador = 0  # La variable contador se inicializará en 0 y nos ayudará a llevar la cuenta de las recetas.
    for txt in Path(ruta).glob("**/*.txt"):  # POR cada TXT que haya EN la RUTA y .CUMPLA con ("TODOS LOS QUE TENGAN.txt") vamos a:
        contador += 1  # pedirle a la variable CONTADOR que, al valor que ya tenga, le sume 1.

    return contador  # Luego, simplemente retornamos dicha variable.


# Menu de inicio, en la siguiente función le daremos la bienvenida al usuario entre otras cosas que detallaremos a continuación.
def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    # En el siguiente loop while decimos: MIENTRAS QUE NO sea un numero (isnumeric) eleccion_menu (lo que haya en esa variable) ( ) OR eleccion_menu (lo que haya en esa varuable) NO ESTE EN EL RANGO DEL (1 al 7) teniendo en cuenta que el segundo parametro no es inclucivo y será en este caso hasta el 6 entonces:...

    '''En el siguiente punto, debemos mostrarle al usuario todas las opciones y él tendrá que elegir una. Pero como dicho menú debe mostrarse una y otra vez mientras que el usuario no brinde una opción correcta vamos a hacerlo dentro de un loop WHILE'''
    
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()

    return int(eleccion_menu)

# inicio()  # Puedes llamar a la función inicio() si deseas ejecutarla al final del script.


# Ahora vamos a crear una funcion (una de las primeras) que sirva para mostrar las categorias:
def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

# Creando la funcion para mostrar las categorias:
def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria: ")

    return lista[int(eleccion_correcta) - 1]

# Creando la fn para mostrar las recetas:
def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas

# Elegir una receta:
def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta: ")

    return lista[int(eleccion_receta) - 1]

# Leer una receta:
def leer_receta(receta):
    print(Path.read_text(receta))

# Crear receta
def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

#Crear categoria
def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento Argento... esa categoria ya existe")

# Eliminar receta:
def eliminar_receta(receta):
    Path(receta).unlink()   #unlink se utiliza para eliminar algo.
    print(f"La receta {receta.name} ha sido eliminada con éxito")

# Eliminar categoria
def eliminar_categoria(categoria):
    Path(categoria).rmdir() #rmdir se utiliza para eliminar un directorio.
    print(f"La categoria {categoria.name} ha sido eliminada con éxito")

# Fn para volver al inicio
def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")


finalizar_programa = False

while not finalizar_programa:
    menu = inicio() # Acá se guardara la decision del cliente.

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)

    elif menu == 6:
        finalizar_programa = True
    