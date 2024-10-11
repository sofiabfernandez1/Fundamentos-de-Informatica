"""Escribir una función para crear una lista con N números al azar en un rango de valores que se recibe por parámetro. 
La función devuelve la lista cargada (o vacía si el rango indicado no es válido)"""

import random

def cargar_numeros(a,b,n):
    lista = []
    if a >= b:
        print("El rango ingresado es inválido.")
    else:
        for i in range (n):
            numero = random.randint(a, b)
            lista.append(numero)
    return lista


numeros = int(input("Ingrese el numero de valores que quiere que contenga la lista:"))
numero_a = int(input("Ingrese el inicio del rango: "))
numero_b = int(input("Ingrese el limite del rango: "))

lista_numeros = cargar_numeros(numero_a, numero_b, numeros)

if lista_numeros:
    print("Los números ingresados fueron", lista_numeros)
else:
    print("La lista se encuentra vacía. ")
