#Desarrollar un programa para cargar 5 notas. Validar que se encuentren entre 1 y 10. Al finalizar, mostrar el promedio de las notas.  

notas = 0
cantidad = 0

for i in range(5):
    nota = float(input("Ingrese una nota:"))
    if nota >= 1 and nota <= 10:
        notas += nota
        cantidad += 1
promedio = notas / cantidad

print("El promedio de las notas es: ", promedio)