""""Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999.
 Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. 
 Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100).  """

suma_menores = 0
menores_18 = 0
suma_mayores = 0
mayores_18 = 0
promedio_menores = 0
promedio_mayores = 0
edades_validas = 0

edad = int(input("Ingrese una edad entre 0 y 100 (Ingrese 999 para finalizar): "))

while edad != 999:
    if edad >= 0 and edad <= 100:
        edades_validas += 1
        if edad < 18:
            suma_menores += edad
            menores_18 += 1
        else:
            suma_mayores += edad
            mayores_18 += 1
    else:
        print("Se ha ingresado una edad inválida.")

    edad = int(input("Ingrese una edad entre 0 y 100 (Ingrese 999 para finalizar): "))

if edades_validas > 0:
    if menores_18 >= 0:
        promedio_menores = suma_menores / menores_18
        print("Cantidad de menores ingresados: ", menores_18)
        print("Edad promedio de menores: ", promedio_menores)
    else:
        print("No se han ingresado menores de edad.")

    if mayores_18 > 0:
        promedio_mayores = suma_mayores / mayores_18
        print("Cantidad de mayores ingresados: ", mayores_18)
        print("Edad promedio de mayores: ", promedio_mayores)
    else:
        print("No se han ingresado mayores de edad.")
else:
    print("No se ha ingresado una edad válida.")