# precios_cafe = [('capuchino', 1.5), ('Expresso', 1.2), ('Moka', 1.9)]

# for cafe, precio in precios_cafe:
#     print(cafe)

# Supongamos que tenemos una consigna que nos pida extraer de una lista de tuples el elemento mas caro.

precios_cafe = [('capuchino', 3.5), ('Expresso', 1.2), ('Moka', 1.9), ('cubano', 2.8)]

# Aquí se define la función llamada cafe_mas_caro, que toma una lista de tuplas llamada lista_precios como argumento.
def cafe_mas_caro(lista_precios):

# Inicializacion de variables: Se crean dos variables, precio_mayor y cafe_mas_caro, inicializadas en 0 y una cadena vacía, respectivamente. Estas variables se utilizarán para realizar un seguimiento del precio más alto y el café correspondiente.
    precio_mayor = 0
    cafe_mas_caro = ''

# Bucle para recorrer la lista de precios: Se utiliza un bucle for para iterar a través de cada elemento de la lista de precios, donde cada elemento es una tupla que contiene el nombre del café y su precio.
    for cafe, precio in lista_precios:
        # Compara precios: Se compara el precio actual con el precio almacenado en precio_mayor. Si el precio actual es mayor, se actualizan las variables precio_mayor y cafe_mas_caro con el precio y el nombre del café actual. En la primer iteracion se almacenarà ese valor ya que de seguro es mayor a cero (como se inicializò la variable)
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    # Retorno de resultados, la funcion devuelve la tupla con el nombre del cafe mas caro y su precio
    return(cafe_mas_caro, precio_mayor) 
# Llamada a la funcion: La función se llama con la lista de precios precios_cafe y los resultados se almacenan en las variables cafe y precio.
cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El café mas caro es {cafe} con un valor de {precio}")

