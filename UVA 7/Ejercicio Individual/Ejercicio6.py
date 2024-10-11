"""Determinar si una lista es capicúa. """

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

def es_capicua(lista):
    lista_invertida = []

    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])

    if lista == lista_invertida:
        return True
    else:
        return False


numeros = int(input("Ingrese el numero de valores que quiere que contenga la lista:"))
numero_a = int(input("Ingrese el inicio del rango: "))
numero_b = int(input("Ingrese el limite del rango: "))

lista = cargar_numeros(numero_a,numero_b,numeros)

if lista:
    print("Contenido de la lista: ", lista)
    if es_capicua(lista):
        print("La lista es capicúa.")
    else:
        print("La lista no es capicúa.")
else:
    print("Las lista se encuentra vacía.")