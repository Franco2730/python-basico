# Que pasa si te digo que tenemos el super poder de hablar con la computadora ? Esto es posible gracias a INPUT.
# En el siguiente ejemplo, la terminal - consola nos devolverá lo que nosotros coloquemos dentro de nuestro input. El unico problema es que, una vez que coloquemos nuestro nombre, este dato se perderá ya que no se almaceno en ningun lugar de la memoria. 
input("Hola, me podrías indicar tu nombre: ")

# Para remediar esto, conservar la respuesta que le vayamos a dar y, lo más importante, tener ese dato disponible para luego poder trabajar, podemos almacenar todo el input en una variable para posteriormente, usarla segun nuestra necesidad.

Saludo = input("Hola, me podrías indicar tu nombre: ") #Le respondo: Franco...

print(f"Hola {Saludo}, no tienes ningun mensaje nuevo..") #Hola Franco no tienes ningun mensaje nuevo..

