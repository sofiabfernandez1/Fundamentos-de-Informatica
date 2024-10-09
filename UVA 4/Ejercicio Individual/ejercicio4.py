"""Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no está entre 0 y 10, debe informar un error.  

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7. 

Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4. 

Se debe recuperar cuando al menos una de las dos notas es menor a 4. """

nota_1 = float(input("Ingrese la nota del primer parcial: "))

nota_2 = float(input("Ingrese la nota del segundo parcial: "))

if nota_1 == 0 or nota_2 == 0:
    if nota_1 == 0:
        print("Las nota del primer parcial deben ser mayor a 0.")
    else:
        print("La nota del segundo parcial debe ser mayor a 0.")
else:
    if(nota_1 >= 7 and nota_2 >= 7):
        print("El alumno promocionó la materia.")
    elif nota_1 >= 4 and nota_2 >= 4:
        print("El alumno aprobó la materia.")
    elif nota_1 < 4 or nota_2 < 4:
        print("El alumno debe recuperar la materia.")