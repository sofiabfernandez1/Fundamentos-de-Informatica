# Escribir una función para devolver la posición que ocupa un valor pasado como parámetro, utilizando búsqueda secuencial en una lista desordenada. La función debe devolver -1 si el elemento no se encuentra en la lista. 

def buscar_secuencial(lista,valor):
    i = 0
    while i < len(lista) and lista[i] != valor:
        i += 1
    if i < len(lista):
        return i
    else:
        return -1

lista_prueba = [2, 2, 6, 3, 5, 7]


posicion = buscar_secuencial(lista_prueba, 3)

if posicion != -1:
    print("El valor se encuentra en la posición", posicion)
else:
    print("El valor no se encuentra en la lista.")