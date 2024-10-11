"""Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa. 
Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe. 
La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.  """

import random

def cargar_numeros(a,b,n):
    lista = []
    if a >= b:
        print("El rango ingresado es inválido.")
    else:
        for i in range (n):
            numero = random.randint(a, b)
            if numero != 0:
                lista.append(numero)
            else:
                break
    return lista


def valor_minimo(lista):
    minimo = lista[0]
    posicion_repetido = [0]

    for i in range(1,len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            posicion_repetido = [i]
        elif lista[i] == minimo:
            posicion_repetido.append(i)

    print("El valor minimo fue ", minimo, " en la posicion ", posicion_repetido)

valores = int(input("Ingrese el número de valores que quiere que contenga la lista: "))
lista = cargar_numeros(0,100,valores)

if lista:
    print("La lista está compuesta por: ", lista)
    valor_minimo(lista)
else:
    print("Las lista se encuentra vacía.")