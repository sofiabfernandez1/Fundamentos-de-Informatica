# Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos. Validar que N sea menor o igual a 100. 

import random 

def generar_lista(n):
    if n > 100:
        print("El número ingresado no puede ser mayor a 100.")
        return False
    
    lista = []

    while len(lista) < n:
        numero = random.randint(0,100)
        if numero not in lista:
            lista.append(numero)

    return lista


n = int(input("Ingrese la cantidad de números que desea generar:"))
lista_generada = generar_lista(n)

if lista_generada: 
    print("La lista generada es: ", lista_generada)
else:
    print("No se ha generado ninguna lista.")



