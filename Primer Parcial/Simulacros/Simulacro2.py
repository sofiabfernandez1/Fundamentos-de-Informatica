""""Escribir un programa en Python que permita ingresar al usuario las notas de
los alumnos de un curso Serán números enteros entre 1 y 10.
No hace falta validar las mismas. El ingreso de las notas finaliza con -1.
Una vez finalizada la carga se pide Informar:
1.Cuántos alumnos aprobaron el examen. (nota >=4).
2.Cuántos alumnos reprobaron el examen. (nota <4).
3.Cuál fue la mayor nota
4.Cual fue la menor nota
5.Cantidad total de exámenes
6.La posición de la mayor nota
7.La posición de la menor nota"""

aprobados = 0

desaprobados = 0

nota_mayor = 0
posicion_mayor = 0

nota_menor = 1000000
posicion_menor = 0

total_examenes = 0


nota = int(input("Ingrese la nota del alumno (entre 1 y 10) - (Ingrese -1 para finalizar): "))

while nota != -1:
    total_examenes += 1

    if nota >= 4:
        aprobados += 1
    elif nota < 4:
        desaprobados += 1
    
    if nota >= nota_mayor:
        nota_mayor = nota
        posicion_mayor = total_examenes

    if nota <= nota_menor:
        nota_menor = nota
        posicion_menor = total_examenes
    
    nota = int(input("Ingrese la nota del alumno (entre 1 y 10) - (Ingrese -1 para finalizar): "))

if total_examenes != 0:
    print("Cantidad total de examenes: ", total_examenes)

    print("Alumnos aprobados: ", aprobados)

    print("Alumnos desaprobados: ", desaprobados)

    print("Nota menor: ", nota_menor, " en la posicion ", posicion_menor)

    print("Nota mayor: ", nota_mayor, " en la posicion ", posicion_mayor)
else:
    print("No se han ingresado notas de examen.")