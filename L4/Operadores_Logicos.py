#A continuacion, vamos a ver como comparar mas de un elemento como aprendimos con los operadores de comparacion.
#Los operadores logicos son: AND, OR

#AND, que significa Y. Este operador obliga a que todas las condiciones se cumplan.
mi_bool = 4 < 5 and 5 == 2 + 3
print(mi_bool) #True

mi_bool2 = 4 < 5 and "Mi perro" == "Mi perro"
print(mi_bool2) #True

#OR, que significa O. Este operador obliga a que aunquesea una condicion se cumpla.
mi_bool = 5 == 5 or 3 == 1 #Aunque la segunda condicion es falsa, dará True porque con que una condicion se cumpla, ya es verdadero
print(mi_bool) #True

#---
texto = "Este texto es muy breve"
find = (('breve' in texto) and ('Este' in texto)) #True


#NOT, que significa NO. Este operador obliga a cambiar la logica comun de un operador. Es decir, NOT nos dice lo contrario a lo que sería.
#NOT niega la comparacion original.
bool = not "a" == "a"
print(bool) #False