# Realizar un programa que, dada una cantidad de dólares y su cotización permita obtener el equivalente en pesos.  

print("----------------------------------------------")
print("---------- Conversión dolar a pesos ---------- ")
print("----------------------------------------------\n")

dolares = float(input("Ingrese la cantidad de dólares: "))

cotizacion = float(input("Ingrese la cotización del dolar: "))

print("El equivalente en pesos de $", dolares, " es ", dolares * cotizacion)