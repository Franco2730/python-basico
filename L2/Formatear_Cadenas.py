#Vamos a tener un inconveniente si queremos cambiarle el tipo de dato a una variable y despues volverlo a cambiar. Por ejemplo:
#queremos cambiar el str de un ingreso de input a int, pero luego, queremos mostrar un mensaje concatenando un mensaje (str) y el valor
#pues, como sabemos, no podremos lograr concatenar un str con un int, osea que, tendriamos que volver a cambiar el int nuevamente a str.
#Para este inconveniente se crearon las cadenas literales. Hay dos formas de hacerlo:

#1- Funcion format: Esta fue la primer solucion que le dieron para el problema anteriormente mencionado, pero no es muy legible, ya que tenemos que
#ir y volver con la mirada:

#print("Mi auto es{} y tiene la matricula número{}".format(color_auto, matricula)

#2- Cadena literal: Acá simplemente, antes del str colocamos la f minuscula y entre los corchetes ponemos las variables. Automaticamente todo sera str
#print(f"Mi auto es{color_auto} y tiene la matricula número{matricula}"

nombre_asociado = "Franco Rosales"
numero_asociado = 4

print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")