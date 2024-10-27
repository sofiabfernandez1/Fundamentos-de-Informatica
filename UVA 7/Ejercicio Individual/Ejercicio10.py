# Utilizando búsqueda binaria sobre una lista ordenada realizar la búsqueda de valores e informar si se encuentran o no en la lista, finalizar las búsquedas con -1 e informar cuantas búsquedas fueron exitosas y en cuantas no se encontró el valor buscado. 
def ordenar_por_seleccion(lista):
    for i in range(len(lista) - 1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]: # Para descendente, cambiar a <
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


def busqueda_binaria(lista,valor):
    pos = -1
    izq = 0
    der = len(lista)-1
    while izq <= der and pos == -1:
        centro = (izq+der)//2
        if lista[centro] == valor:
            pos = centro
        elif valor > lista[centro]:
            izq = centro + 1
        else:
            der = centro - 1
    return pos



lista = [3,5,73,2,4,34,5,56,32,1,2,55,3,43]
lista_ordenada = ordenar_por_seleccion(lista)

busquedas_exitosas = 0
busquedas_fallidas = 0

valor = int(input("Ingrese un valor a buscar: "))
while valor == -1:
    valor = int(input("Ingrese un valor a buscar: "))

while valor != -1:
    if busqueda_binaria(lista_ordenada,valor) != -1:
        busquedas_exitosas += 1
    else:
        busquedas_fallidas += 1
    valor = int(input("Ingrese un valor a buscar: "))

print("Búsquedas exitosas:", busquedas_exitosas )
print("Búsquedas fallidas:", busquedas_fallidas)

