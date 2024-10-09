"""La universidad necesita un sistema para cargar las notas finales de los alumnos. 
Los datos para ingresar son: Legajo (número positivo), mes (solamente se aceptan los números 3, 6 y 12) 
y nota (número entre 1 y 10). La carga de datos termina al ingresar -1 como legajo. 
Validar los datos pedidos. Al finalizar, informar:  
Cantidad de alumnos que promocionaron la materia (nota 7 o más). 

Cantidad de alumnos que aprobaron (nota 4 o más). 

Porcentaje de alumnos reprobados. 

Promedio de notas obtenidas en el mes 6."""

promocionados = 0
aprobados = 0
reprobados = 0
mes_6_notas = 0
mes_6_total = 0
total_alumnos = 0

legajo = int(input("Ingrese el legajo del alumno (ingrese -1 para terminar): "))

while legajo != -1:
    if legajo > 0:
        mes = int(input("Ingrese el mes (3,6 o 12) correspondiente a la nota: "))
        if mes == 3 or mes == 6 or mes == 12:
            nota = float(input("Ingrese la nota del alumno (entre 1 y 10): "))
            if nota >= 1 and nota <= 10:
                total_alumnos += 1

                if nota >= 7:
                    promocionados += 1
                elif nota >= 4:
                    aprobados += 1
                else:
                    reprobados += 1

                if mes == 6:
                    mes_6_notas += nota
                    mes_6_total += 1
            else: 
                print("La nota debe encontrarse entre 1 y 10.")
        else:
            print("El mes ingresado debe ser 3, 6 o 12.")
    else:
        print("El legajo debe ser mayor a 0.")

    legajo = int(input("Ingrese el legajo del alumno (ingrese -1 para terminar): "))
    
if total_alumnos > 0:
    print("Cantidad de alumnos que promocionaron el final: ", promocionados)

    print("Cantidad de alumnos que aprobaron el final: ", aprobados)

    porcentaje_reprobados = (reprobados / total_alumnos) * 100
    print("Porcentaje de alumnos reprobados: ", porcentaje_reprobados, "%")

    if mes_6_total > 0:
        promedio_mes_6 = mes_6_notas / mes_6_total
        print("Promedio de notas obtenidas en el mes 6: ", promedio_mes_6)
else:
    print("No se ingresaron alumnos.")


