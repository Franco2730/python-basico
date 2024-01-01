'''En la clase pasada vimos como modificar el archivo pero unicamente en las variables de nuestra computadora, ahora es momento de modificar el archivo original, modificar nuestro querido archivo prueba.txt'''

'''En la clase de EntradaSalida utilizamos el metodo open para abrir dichi archivo y a este no le pusimos ningun tipo de parametro mas que el path de nuesto txt, En realidad open recibe 2 parametros ('Elnombredelarchivo.txt', modo_apertura) ¿Qué es el modo de apertura? se refiere a que queremos hacer con el archivo. 
 Los tres modos de apertura son:

    mi_archivo = open('archivo.txt','r') - Modo de solo lectura. Si usamos el metodo open con la 'r' como segundo parametro, no podremos hacer modificaciones sobre dicho documento, solo lee su contenido.

    mi_archivo = open('archivo.txt','w') - Modo de solo escritura. Si usamos la 'w' y el archivo.txt ya existe es vaciado (se resetea desde 0) y si no existe se lo crea.

    mi_archivo = open('archivo.txt','a') - Modo de solo escritura al final del archivo. Cuando utilizamos la 'a' como segundo parametro, se crea el archivo.txt (en caso de que no exista) y si ya existe, el cursor se posiciona al final del archivo para salvar los cambios que en el se alojen. No se borrará el contenido existente. 
    '''