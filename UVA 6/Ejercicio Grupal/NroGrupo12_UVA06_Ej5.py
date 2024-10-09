"""Desarrollar un programa que permita simular un juego de cartas. Las reglas son las siguientes: 
Las cartas pueden valer 1, 2 o 3, su valor se obtiene de forma aleatoria. 

Se pueden obtener 3 juegos: tres números iguales, tres números distintos o dos números iguales y uno distinto. 

Si se obtienen tres números iguales el jugador gana 10 puntos, si se obtienen tres números distintos el jugador gana 7 puntos 
y si se obtienen dos números iguales y uno distinto el jugador gana 4 puntos. 

Crear una sola función que retorne el puntaje de acuerdo a los valores de las cartas. 

Desarrollar un programa principal que permita simular 5 jugadas. En cada jugada deberá informar los números y el puntaje obtenido.
Al finalizar mostrar el total de puntos acumulados. """


import random

def cartas():
    carta_1 = random.randint(1, 3)
    carta_2 = random.randint(1, 3)
    carta_3 = random.randint(1, 3)

    print("Las cartas obtenidas fueron ", carta_1, ", ", carta_2, " y ", carta_3,".")

    if carta_1 == carta_2 == carta_3:
        print("¡Ganaste 10 puntos!\n")
        return 10
    elif carta_1 != carta_2 and carta_2 != carta_3 and carta_3 != carta_1:
        print("¡Ganaste 7 puntos!\n")
        return 7
    else:
        print("¡Ganaste 4 puntos!\n")
        return 4
    

total_puntos = 0

for i in range(5):
    puntos = cartas()
    total_puntos += puntos

print("El total de puntos obtenidos en 5 jugadas fue ", total_puntos, " puntos.")



