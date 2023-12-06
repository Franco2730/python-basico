#Podemos redondear: El metodo round pide dos parametros: el primer parametro es el numero que queremos redondear
print(round(90/7))#13

resultado = 90/7
redondeo = round(resultado)
print(resultado) #12.857142857142858
print(redondeo)#13

#Como ya dijimos, round nos solicita 2 parametros. El primero es el numero que queremos redondear y el segundo, cuantos decimales queres que tenga:
float = 19.6666666666666666666
print(round(float, 2)) #19.67 Acá podemos ver como pedimos imprimir la variable floar pero antes utilizando el metodo round y avisandole que solo
#queremos 2 decimales, en vez de 66 se redondeo el ultimo decimal para arriba ya que esta mas cerca del 9 que del 0.

#Práctica Redondeo 1
#Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
#print(round(10/3, 2))

#Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
#valor = 10.676767
#print(round(valor))

