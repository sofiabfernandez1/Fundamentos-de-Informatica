"""Diseñar una función que reciba dos parámetros numéricos enteros, calcule y devuelva el resultado de la multiplicación de ambos utilizando sólo sumas.  
Desarrollar un programa principal para crear la siguiente serie numérica de N términos, comienza en uno y cada siguiente término se obtiene multiplicando el anterior por la ubicación: 


1	2	6	24	120
*2	*3	*4	*5"""


def multiplicacion_por_suma(numero1, numero2):
    multiplicacion = 0
    for _ in range(numero2):
        multiplicacion += numero1
    return multiplicacion


cantidad = int(input("Ingrese la cantidad de números que desea que tenga la serie numérica:"))

print("Serie numérica:")

inicio = 1

print(inicio)

for i in range(2,cantidad+1):
    numero = multiplicacion_por_suma(inicio,i)
    print(numero, " ")
    inicio = numero
