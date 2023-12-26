# A diferencia del *args, con **kwargs ademas de una cantidad indefinida de parametros podemos pasar un nombre a esos argumentos y un valor. Los kwargs trabajan con diccionario. 

def suma(**kwargs):
    print(type(kwargs)) # <class 'dict'>

suma(a = 1, b = 2, c = 3)



def operacion(**kwargs):

    suma = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        suma += valor
    return suma # 6 Ya que simamos los valores como dice la linea anterior

print(operacion(a = 1, b = 2, c = 3))
'''
a = 1
b = 2
c = 3
'''


# Ahora veamos como podemos mezclar valores comunes, args y kwargs como argumentos en una misma funcion. (Protegeme señor con tu espiiiiiiritu)

def suma2(num1, num2, *args, **kwargs):
    
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"Arg = {arg}")
    
    for clave, valor in kwargs.items():
        print(f"Clave valor es igual a: {clave} = {valor}")

#suma2(15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, a = 10, b = 20, c = 30, d = 40, e = 50, f = 60, g = 70)

'''
El primer valor es 15
El segundo valor es 20
Arg = 25
Arg = 30
Arg = 35
Arg = 40
Arg = 45
Arg = 50
Arg = 55
Arg = 60
Arg = 65
Arg = 70
Arg = 75
Arg = 80
Clave valor es igual a: a = 10        
Clave valor es igual a: b = 20        
Clave valor es igual a: c = 30        
Clave valor es igual a: d = 40        
Clave valor es igual a: e = 50        
Clave valor es igual a: f = 60        
Clave valor es igual a: g = 70
'''

# Vamos a proponer otra alternativa al problema anterior:
def suma3(n1, n2, *args, **kwargs):
    
    print(f"The first value is {n1}")
    print(f"The second value is {n2}")

    for arg in args:
        print(f"Arg = {arg}")
    
    for clave, valor in kwargs.items():
        print(f"Clave valor es igual a: {clave} = {valor}")

args = [25, 30, 35, 40, 45, 50]
kwargs = {'a': 10, 'b': 20, 'c': 30}

suma3(15, 20,*args, **kwargs) #Este es un truquito para llamarlo directamente de aca. Importante, no olvidar colocar los asteriscos. 

'''
The first value is 15
The second value is 20
Arg = 25
Arg = 30
Arg = 35
Arg = 40
Arg = 45
Arg = 50
Clave valor es igual a: a = 10        
Clave valor es igual a: b = 20        
Clave valor es igual a: c = 30 
'''


