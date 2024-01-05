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
import os                   # Modulo para navegar entre nuestras carpetas
from pathlib import Path    # El objeto path es esencial para construir rutas
from os import system       # System nos permite limpiar la pantalla. Es un detalle visual

# Ahora debemos crear en el menu de inicio, este debe hacer:
# Dar la bienvenida.
# Inofmrar donde se encuentran los archivos.
# Luego informar cuantas recetas tenemos.
# Mostrar el menu.

mi_ruta = Path(Path.home(), "Recetas") # Esta variable contendrá la ruta a nuestra carpeta madre y como segundo parametro, el elemento que queremos detallar. Aquí tendremos la ruta directa a nuestra carpeta Recetas y su contenido.

def contar_recetas(ruta): # Esta función se encargará de contar las recetas. Necesita un parametro que será la ruta 
    contador = 0          # La variable contador se inicializará en 0 y nos ayudara a llevar la cuenta de las recetas.
    for txt in Path(ruta).glob("**/*.txt"): # POR cada TXT que haya EN la RUTA y .CUMPLA con ("TODOS LOS QUE TENGAN.txt") vamos a:
        contador += 1 # pedirle a la variable CONTADOR que, al valor que ya tenga, le sume 1.

    return contador #Luego, simplemente retornamos dicha variable.

# Menu de inicio.

menu = 0 # Acá se guardara la decision del cliente.

if menu == 1:
    # Mostrar categorias
    # Elegir categorias
    # Mostrar recetas
    # Elegir recetas
    # Leer recetas
    # Volver a inicio
    pass
elif menu == 2:
    # Mostrar categorias
    # Elegir categorias
    # Crear receta nueva
    # Volver a inicio
    pass
elif menu == 3:
    # Crear categorias
    # Volver a inicio
    pass
elif menu == 4:
    # Mostrar categorias
    # Elegir categorias
    # Mostrar recetas
    # Elegir recetas
    # Eliminar recetas
    # Volver a inicio
    pass
elif menu == 5:
    # Mostrar categorias
    # Elegir categorias
    # Eliminar categorias
    pass
elif menu == 6:
    # Finalizar programa.
    pass