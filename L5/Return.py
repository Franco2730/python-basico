# Vimos como imprimir en pantalla la devolucion de la resolucion de una funcion, pero no es lo mas habitual, lo mas comun es que la funcion retorne algo. Y cual es la diferencia entre imprimir y retornar ? Es muy sencillo, Cuando imprimimos un valor en la consola, podemos ver ese resultado plasmado en dicho lugar, pero cuando refresquemos la consola, los datos, resultados, procedimientos se perderan porque no fueron guardados en ningun lado. Cuando retornamos, generalmente guardamos ese valor en una variable para retornarla y ahi, estamos guardando una pequeña parte de la memoria para esa información, es decir, nunca desaparecerá a menos que nosotros asi lo queramos.

def multiplicar(num1, num2):
    total = num1 * num2
    return total

resultado = multiplicar(5, 5)
print(resultado)  #25

resultado2 = multiplicar(5, 50)
print(resultado2) # 250

resultado3 = multiplicar(5, 500)
print(resultado3) # 2500



palabra = "Python"
 
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

print(palabra)