# Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista: métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma descendente? 

def ordenar_por_seleccion(lista):
    for i in range(len(lista) - 1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]: # Para descendente, cambiar a <
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


def ordenar_por_insercion(lista):
    for i in range(1,len(lista)):
        valorInsertar = lista[i]
        j = i
        while j > 0 and lista[j-1] > valorInsertar: # Para descendente, cambiar a <
            lista[j] = lista[j-1]
            j = j-1
        lista[j] = valorInsertar
    return lista

def ordenar_por_burbuja(lista):
    for recorrido in range(1,len(lista)):
        for i in range(len(lista) - recorrido):
            if lista[i] > lista[i+1]: # Para descendente, cambiar a <
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista


lista1 = [3,5,73,2,4,34,5]
lista2 = [6,5,2,4,31,4,21]
lista3 = [56,32,1,2,55,3,43]

# Ordenar ascendente
print("Lista ordenada por seleccion - ascendente: ", ordenar_por_seleccion(lista1))
print("Lista ordenada por insercion - ascendente: ", ordenar_por_insercion(lista2))
print("Lista ordenada por burbuja - ascendente: ", ordenar_por_burbuja(lista3))