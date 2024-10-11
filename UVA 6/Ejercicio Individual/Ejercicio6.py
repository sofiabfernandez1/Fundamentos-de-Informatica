"""Hora de jugar. Una calculadora tiene cuatro operaciones básicas (a saber: sumar, restar, multiplicar, dividir). Desarrolle una función para realizar cada operación, que reciba como parámetros dos números ingresados por el usuario y devuelva el resultado de la operación. Resuelva la división por restas sucesivas (investigar cómo se resuelve).  
Desarrollar un programa principal con un menú que permita realizar una operación y posea una opción para Salir. Luego de cada operación realizada se debe volver a presentar el menú. """

def sumar(numeroA,numeroB):
    return numeroA + numeroB

def restar(numeroA, numeroB):
    return numeroA - numeroB

def multiplicar(numeroA, numeroB):
    return numeroA * numeroB

def dividir(numeroA, numeroB):
    if numeroB == 0:
        return "No se puede dividir por cero."
    
    cociente = 0

    if numeroA >= 0:
        dividendo = numeroA
    else:
        dividendo = -numeroA

    if numeroB >= 0:
        divisor = numeroB
    else:
        divisor = -numeroB
    
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1
    
    if(numeroA < 0 and numeroB > 0) or (numeroA > 0 and numeroB < 0):
        cociente = -cociente

    return cociente

def mostrar_titulo(longitud,texto):
    print("*" * longitud)
    print(texto)
    print("*" * longitud)


salir = False
while not salir:
    mostrar_titulo(17, " | Calculadora | ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir (por restas sucesivas)")
    print("5. Salir")
    print()
    opcion = int(input("Ingrese una opción: "))
    print()
    if opcion == 5:
        print("Sesión terminada.")
        salir = True
    elif opcion == 1:
        mostrar_titulo(4, "Suma")
        numeroA = int(input("Ingrese un numero:"))
        numeroB = int(input("Ingrese un numero:"))
        print("La suma de ", numeroA, "y", numeroB, "es:", sumar(numeroA,numeroB))
        print()
    elif opcion == 2:
        mostrar_titulo(5, "Resta")
        numeroA = int(input("Ingrese un numero:"))
        numeroB = int(input("Ingrese un numero:"))
        print("La resta de ", numeroA, "y", numeroB, "es:", restar(numeroA,numeroB))
        print()
    elif opcion == 3:
        mostrar_titulo(11, "Multiplicar")
        numeroA = int(input("Ingrese un numero:"))
        numeroB = int(input("Ingrese un numero:"))
        print("La multiplicación de ", numeroA, "y", numeroB, "es:", multiplicar(numeroA,numeroB))
        print()
    elif opcion == 4:
        mostrar_titulo(7, "Dividir")
        numeroA = int(input("Ingrese un numero:"))
        numeroB = int(input("Ingrese un numero:"))
        print("La división de ", numeroA, "y", numeroB, "es:", dividir(numeroA,numeroB))
        print()
    else:
        print("Se ha ingresado una opción inválida.")
        print()
