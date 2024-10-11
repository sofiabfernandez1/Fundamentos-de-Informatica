# Calcular la suma de los números de una lista.  

import random

def cargar_numeros(a,b,n,lista):
    lista = []
    if a >= b:
        print("El rango ingresado es inválido.")
    else:
        for i in range (n):
            numero = random.randint(a, b)
            lista.append(numero)
    return lista

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = int(input("Ingrese el numero de valores que quiere que contenga la lista:"))
numero_a = int(input("Ingrese el inicio del rango: "))
numero_b = int(input("Ingrese el limite del rango: "))

lista_numeros = cargar_numeros(numero_a, numero_b, numeros)

if lista_numeros:
    suma = suma_lista(lista_numeros)
    if suma:
        print("La suma de los numeros de la lista es ", suma)
else:
    print("La lista se encuentra vacía. ")