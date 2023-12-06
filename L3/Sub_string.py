#Podemos rebanar (slicer) o fragmentar un string. Es decir, si queremos sacar el string "gusto" del string "Hola, un gusto, soy franco"
#Tenemos que colocar dos puntos a lo que ya sabemos del index. es decir: colocamos el numero de la posicion donde comenzamos a extraer
#y como segundo parametro donde queremos terminar la extraxion, no es inclusivo asique si el str finaliza en la pos. 13, debemos poner 14
texto = "Hola, un gusto, soy franco"
fragmento = texto[9:14] #gusto
print(fragmento)