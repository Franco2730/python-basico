# IF, ELIF, ELIF, ELIF, ELSE:

#if una_condicion:
#    print(codigo_a)
#elif otra_condicion:
#    print(codigo_b)
#elif otra_condicion_nueva:
#    print(codigo_c)
#else:
#    print(codigo_z)

if 10 > 11: #SUPER IMPORTANTE, SIEMPRE respetar las TABULACIONES.
    print("Es correcto")
else:
    print("No es correcto")
#---
mascota = "perro"

if mascota == "gato":
    print("Tienes un gatito")
elif mascota == "pez":
    print("Tienes un pescadito")
elif mascota == "tucan":
    print("Tienes un pajarito")
elif mascota == "perro":
    print("Tienes un hermoso perrito") #Va a tomar esta opcion.
else:
    print("No se que animal tienes")
#---
edad = 2
calificacion = 3

if edad > 18:
    print("Eres mayor de edad")
    if calificacion >= 7:
        print("Estás aprobado")
    else:
        print("Estás desaprobado")
else:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Estás aprobado")
    else:
        print("Estás desaprobado")

#En el siguiente ejemplo trabajaremos con inputs, como ya sabemos, los
num1 = int(input("ingrese el primer numero: ")) #300
num2 = int(input("ingrese un numero: ")) #33

if num1 > num2:
    print(str(num1) + " es mayor que: " + str(num2))
elif num2 > num1:
    print(str(num2) + " es mayor que: " + str(num1))
else:
    print(f"El numero: {num1} es igual a: {num2}")

#---
python = input("Por si o por no. Maneja el lenguaje de Pthon").lower()
ingles = input("Por si o por no. Tiene conocimientos en ingles").lower()

if python == "si":
    print("El saber python es uno de los requisitos, genial !!")
    if ingles == "si":
        print("Estas capacitado para el puesto !! Felicitaciones.")
    else:
        print("Saber ingles es un requisito no excluyente")
elif python == "no":
    print("Deberías saber python")
    if ingles == "no":
        print("Todavía no estás preparado para el puesto.")
