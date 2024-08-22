# Diseñar el algoritmo para resolver los siguientes problemas y escriba el programa correspondiente en lenguaje Python. 

# 1A - Mostrar el mensaje “Hola Mundo”. 

print("Hola Mundo")

#1B - Ingresar el nombre del usuario del programa y saludarlo. Ejemplo: si el usuario se llama Juan, se debe mostrar el mensaje “Hola Juan”. 

nombre = input("Ingresa tu Nombre de Usuario: ")

print("Hola", nombre)

#1C - Ingresar dos números y mostrar la suma y la diferencia.

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

suma = numero1 + numero2
diferencia = numero1 - numero2

print("La suma de ", numero1, " y ", numero2, " es:", suma)
print("La diferencia de ", numero1, " y ", numero2, " es:", diferencia)

#1D - Ingresar tres números y mostrar la suma y el promedio. 
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

suma = numero1 + numero2 + numero3

promedio = suma / 3

print("La suma de ", numero1, ", ", numero2, " y ", numero3, " es:", suma)

print("El promedio de ", numero1, ", ", numero2, " y ", numero3, " es:", promedio)

#1E - Ingresar el monto de una factura y calcular el IVA (21%). 

monto = float(input("Ingrese el monto de la factura: ")) 

iva = monto * 0.21

print("El IVA (%21) de $", monto, " es ", iva)