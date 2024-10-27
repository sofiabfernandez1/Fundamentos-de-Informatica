import random


# Crear Matriz

m = [[0,0,0],[0,0,0],[0,0,0]]

print(m)


filas = 3
columnas = 2
matriz3x2 = []

# Crear la matriz con ceros
for fil in range(filas):
    matriz3x2.append([])  # Agregar una lista vacía para cada fila
    for col in range(columnas):
        matriz3x2[fil].append(0)  # Añadir un cero por cada columna

print(matriz3x2)


# Funcion crear matriz

def crear_matriz(filas,columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(0)
    return matriz

# Función llenar matriz

def llenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            numAleatorio = random.randint(1,10)
            matriz[f][c] = numAleatorio

m = crear_matriz(2,2)
llenar_matriz(m)
print(m)

