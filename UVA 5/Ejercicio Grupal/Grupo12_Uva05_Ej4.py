#Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y la cantidad de edades ingresadas. Descartar valores que no representan una edad válida (se considera válido una edad entre 0 y 100). Utilizar el depurador de Thonny para visualizar las variables y detectar posibles errores en tiempo de ejecución.

cantidad = 0
menor_18 = 0
mayor_18 = 0

edad = int(input("Ingrese una edad: "))
while edad != 999:
    if edad >= 0 and edad <= 100:
        cantidad += 1
        if edad < 18:
            menor_18 += 1
        else:
            mayor_18 += 1
    else:
        print("La edad ingresada debe encontrarse entre 0 y 100.")
    edad = int(input("Ingrese una edad: "))    

print("Total menores de 18 años: ", menor_18)

print("Total mayores de 18 años: ", mayor_18)

print("Cantidad de edades ingresadas: ", cantidad)