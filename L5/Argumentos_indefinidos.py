# Hasta ahora sabemos trabajar con funciones con un numero de argumentos definidos, por ejemplo:

def suma(num1, num2):
    return num1 + num2

# Pero como hariamos una funcion que reciba por parametros todos los numeros que el usuario quiera pasar. Le vamos a dar solucion a este problema con dos simples palabras: 
# *args
# **kwargs

# *args significa argumentos, esto nos ayuda a definir argumentos con numeros variables. Podemos definir funciones genericas que se adapten al numero de parametros que nosotros queramos. Lo curioso es que la palabra args es una convención. Podriamos colocar cualquier palabra siempre y cuando comience con un asterisco.

# En el siguiente ejemplo vemos como la funcion suma tiene solamente dos argumentos pero el usuario le brindo 3. El programa le devolverá un error donde especifica que hay dos argumentos pero el le brindo elementos para 3.

def suma(a, b):
    return a + b

print(suma(5, 10, 15)) #TypeError: suma() takes 2 positional arguments but 3 were given



def sumar(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sumar(5, 10, 20, 10, 55, 100, 200)) #TypeError: suma() takes 2 positional arguments but 3 were given
