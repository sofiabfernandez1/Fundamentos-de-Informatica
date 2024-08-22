#Ingresar tres notas de una materia de un alumno y muestre la suma y la promedio. 

nota1 = int(input("Ingresa la primer nota del alumno: "))
nota2 = int(input("Ingresa la segunda nota del alumno: "))
nota3 = int(input("Ingresa la tercera nota del alumno: "))

suma = nota1 + nota2 + nota3

promedio = suma / 3

print("La suma de ", nota1, ", ", nota2, " y ", nota3, " es:", suma)

print("la promedio de ", nota1, ", ", nota2, " y ", nota3, " es:", promedio)
