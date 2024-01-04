'''A veces vamos a querer que, despues de que el usuario otorgue información, la consola se limpie automaticamente y dejar de ver los input con la respuesta y abajo el mensaje predeterminado para solo ver dicho mensaje. Para ello: '''

from os import system #Vamos a importar system ya que tiene el metodo para llevar a cabo esta tardea.

nombre = input('Por favor, dinos tu nombre: ')
edad = input('Ahora, dinos... ¿Cuantos años tienes?: ')

system('cls') #Esta linea de codigo, la vamos a utilizar donde nosotros queramos limpiar la consola.

print(f"Tu nombre es: {nombre} y tienes {edad}")

'''
Ejercicio 1:
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).

RTA:
def abrir_leer(parametro):
    archivo = open(parametro)
    return archivo.read()

    
Ejercicio 2:
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

RTA:
def sobrescribir(parametro):
    archivo = open(parametro, 'w')
    archivo.write("contenido eliminado")


Ejercicio 3:
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.

RTA:
def registro_error(parametro):
    archivo = open(parametro, 'a')
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()
    
'''