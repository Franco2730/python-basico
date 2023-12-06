#Tal ves nosotros queramos cambiarle el tipo de dato a una variable, tal vez queramos tratar como INT al STR que un usuario envia
# por el input. Esto se llama Convercion y hay dos tipos de Convercion.
#La Convercion implícita: Python convierte el tipo de datos en otro tipo de datos AUTOMATICAMENTE. En este proceso, el usuario no debe hacer NADA.
#La convercion explicita: Python necesita que el usuario haga algo para convertir un tipo de dato en otro. Lo tenemos que expresar nosotros. Por Eje:

#El siguiente ejemplo es una conversion implicita ya que Python transforma el tipo de dato de la variable num1 al sumarlo con num2 deja de valer 20
#para valer 50.5 cambio el tipo de dato por si solo.
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

#En el siguiente ejemplo lo vamos a pedir explicitamente que, pese a que sabemos que el valor de la variable num3 es Float, abajo le estamos otorgando
#como valor, a la variable num4, que sea INTEGER de num3. Es decir, se va a imprimir 5 ya que al transformar el tipo de dato NO redondeo, si no, que
#elimino todos los decimales

num3 = 5.8
print(num3)
print(type(num3))
#5.8
#<class 'float'>

num4 = int(num3)
print(num4)
print(type(num4))
#5.8
#<class 'float'>


#Ahora, solucionemos el problema del input, la edad, el usuario y la virgen Maria.
edad = input("Dime tu edad: ")
print(type(edad))
#Dime tu edad: 30
#<class 'str'>
#Si queremos hacer una frase que diga: Tu edad es 30 se puede hacer perfectamente ya que ambas partes de la concatenacion son STRING, ya que todo lo
#que ingresa un usuario por un input se trata como str
saludo = "Hola, tu edad es: " + edad
print(saludo)
#Entonces, si todo se trata como str como podriamos decir algo como: el año que viene cumplirias.... En dicha oportunidad tendriamos que hacer una
#operacion matematica, y al ser todo str no podriamos. vamos a:
nueva_edad = int(edad)
print(type(nueva_edad))
#Hola, tu edad es: 30
#<class 'int'>

