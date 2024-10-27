"""Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros 5 números pertenecientes a 
la lista B. Crear una lista C, donde cada posición es el resultado de la suma del número en la misma posición en la lista 
A con el número en la misma posición en la lista B. 
Ejemplo: Se crea A = [1, 2, 3, 4, 5] y B = [4, 7, 1, 3, 6]  C = [5, 9, 4, 7, 11]  """

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

def sumar_listas(lista_A, lista_B):
    lista_C = []

    for i in range(len(lista_A)):
        suma = lista_A[i] + lista_B[i]
        lista_C.append(suma)

    return lista_C

numero_a = int(input("Ingrese el inicio del rango: "))
numero_b = int(input("Ingrese el limite del rango: "))

lista_A = cargar_numeros(numero_a,numero_b,5)
lista_B = cargar_numeros(numero_a,numero_b,5)

if lista_A and lista_B:
    lista_C = sumar_listas(lista_A, lista_B)
    print("Lista A: ", lista_A)
    print("Lista B: ", lista_B)
    print("Lista C: ", lista_C)
else:
    print("Las listas A y B se encuentran vacías.")