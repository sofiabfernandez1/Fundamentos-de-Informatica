""""Desarrollar dos funciones: 
Diseñar una función que solicite por teclado un número y lo retorne solo si el número ingresado es natural, caso contrario la función deberá seguir solicitando el número. 

Función para sumar los primeros N números naturales de un valor. Retorna la suma. Desarrollar un programa principal para ingresar una cantidad de valores naturales (la cantidad se solicita al usuario). Para cada valor informar la suma de los primeros N valores naturales. Al finalizar informar cuántos valores se ingresaron y cuál es el mayor valor ingresado. """

def numero_natural():
    numero = int(input("Ingrese un número natural: "))
    while numero < 0:
        print("Ha ingresado un número no natural. ")
        numero = int(input("Ingrese un número natural: "))
    return numero

def sumar_numeros_naturales(numero,n):
    suma = 0
    for _ in range(n):
        suma += numero
    return suma

def mostrar_titulo(longitud,texto):
    print("*" * longitud)
    print(texto)
    print("*" * longitud)

mostrar_titulo(35, "Aprendiendo sobre numeros naturales")

maximo = -1
cantidad_Valores = int(input("¿Cuantos números naturales desea generar?:"))

for _ in range(cantidad_Valores):
    numero = numero_natural()
    n = int(input("Ingrese cuantas veces desea sumar el numero:"))
    print("La suma de los primeros ", n, "valores naturales de", numero, "es", sumar_numeros_naturales(numero, n))
    if numero > maximo:
        maximo = numero

print("Se ingresaron", cantidad_Valores, "numeros.")
print("El número maximo ingresado fue", maximo)