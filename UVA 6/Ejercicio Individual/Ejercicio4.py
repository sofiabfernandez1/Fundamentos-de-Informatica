"""Desarrollar dos funciones 
Función para sumar los dígitos de un número. Recibe un número y retorna la suma de los dígitos. (NO utilizar cadenas de caracteres str, para lograr el objetivo) 

Extraer un dígito de un número. La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o negativo. Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1. 

Desarrollar un programa para generar valores al azar de 5 dígitos hasta que el dígito central sea cero. Mostrar por pantalla este número y la suma de sus dígitos utilizando ambas funciones creadas y no olvidar mostrar un título al inicio utilizando la función del ejercicio 3 """
import random

def mostrar_titulo(longitud,texto):
    print("*" * longitud)
    print(texto)
    print("*" * longitud)

def sumar_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma

def extraer_digitos(numeroA, numeroB):
    match = False
    posicion = 0
    while numeroA > 0 or match == False:
        digito = numeroA % 10
        # print(digito)
        if digito == numeroB:
            match = True
            posicion_match = posicion
        numeroA = numeroA // 10
        posicion = posicion + 1
    if match:
        return posicion_match
    else:
        return -1


encontrado = False

mostrar_titulo(25, "Aprendiendo sobre digitos")

# numero = int(input("Ingrese un numero: "))
# sumar_digitos(numero)

# numeroA = int(input("Ingrese un numero: "))
# numeroB = int(input("Ingrese la cifra que desea que se extraiga del numero anterior."))

# print(extraer_digitos(numeroA,numeroB))

while not encontrado:
    numero_azar = random.randint(10000,99999)
    print(numero_azar)
    posicion = extraer_digitos(numero_azar,0)

    if posicion == 2:
        print("El número generado fue", numero_azar)
        print("La suma de sus digitos es", sumar_digitos(numero_azar))
        encontrado = True