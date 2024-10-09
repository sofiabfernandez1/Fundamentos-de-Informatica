"""Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso 
y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. 
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. 
Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar: 
Cantidad de alumnos que aprobaron con nota mayor o igual a 4. 

Cantidad de alumnos que desaprobaron el examen. Nota menor a 4. 

Porcentaje de alumnos que están aplazados (tienen 1 en el examen). 


> mayor que
< menor quie
"""

alumnos = 0
alumnos_aprobados = 0
alumnos_desaprobados = 0
alumnos_aplazados = 0

legajo = int(input("Ingrese el número de legajo (ingrese -1 para finalizar): "))

while legajo != -1:
    if legajo != -1:
        nota = int(input("Ingrese la nota del alumno: "))
        if nota >= 1 and nota <= 10:
            alumnos += 1
            if nota >= 4:
                alumnos_aprobados += 1
            else:
                alumnos_desaprobados += 1
                if nota == 1:
                    alumnos_aplazados += 1
        else:
            print("Se ha ingresado una nota inválida. El valor debe encontrarse entre 1 y 10.")
    else: 
        print("Se ha finalizado con la carga de datos.")

    legajo = int(input("Ingrese el número de legajo (ingrese -1 para finalizar): "))

if alumnos != 0:
    print("-------------------------")
    print("------ Resultados -------")
    print("-------------------------")

    print("Cantidad de alumnos aprobados: ", alumnos_aprobados)
    print("Cantidad de alumnos desaprobados: ", alumnos_desaprobados)
    if alumnos_aplazados > 0:
        porcentaje_aplazados = (alumnos_aplazados / alumnos) * 100
        print("Porcentaje de alumnos aplazados ", porcentaje_aplazados )
    else:
        print("Ningún alumno ha sido aplazado. ")
else:
    print("No se ha ingresado ningún legajo válido.")


