"""Diseñar una función que reciba dos números enteros como parámetros enteros A y B, y permita obtener AB mediante multiplicaciones sucesivas
Desarrollar un programa principal para generar N veces dos valores al azar en un rango desde-hasta ingresado por teclado y calcular AB, mostrar por pantalla los valores creados y el resultado de la operación. """
import random

def multiplicar_numeros(numeroA,numeroB):
    multiplicacion = 1
    for _ in range(numeroB):
        multiplicacion *= numeroA
    return multiplicacion


desde = int(input("Ingrese el inicio del rango numérico: "))
hasta = int(input("Ingrese el final del rango numérico: "))

while desde < hasta:
    print("El inicio del rango no puede ser mayor al final del rango (",hasta,")")
    desde = int(input("Ingrese el inicio del rango numérico: "))

while hasta < desde:
    print("El final del rango no puede ser menor al inicio del rango (",desde,")")
    hasta = int(input("Ingrese el final del rango numérico: "))

cantidad = int(input("Ingrese la cantidad de numeros que desea generar: "))

for i in range(cantidad):
    numeroA = random.randint(desde, hasta)
    numeroB = random.randint(desde, hasta)

    multiplicacion = multiplicar_numeros(numeroA, numeroB)

    print("Valores creados: ", numeroA, " y ", numeroB)
    print("Resultado de la operación: ", multiplicacion)
