"""Escribir una función que solicite ingresar una serie de números entre a y b y guardarlos en una lista. 
En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error y solicitará un nuevo número. 
Para finalizar la carga se deberá ingresar -1. La función no recibe ningún parámetro, y devuelve la lista cargada 
(o vacía, si el usuario no ingresó nada) como valor de retorno. """

def cargar_numeros():
    lista = []
    numero_a = int(input("Ingrese el inicio del rango: "))
    numero_b = int(input("Ingrese el limite del rango: "))
    if numero_a >= numero_b:
        print("El rango ingresado es inválido.")
    else:
        numero = int(input("Ingrese un numero (Ingrese -1 para finalizar):"))
        while numero != -1:
            if numero >= numero_a and numero <= numero_b:
                lista.append(numero)
            else: 
                print("Se ha ingresado un número por fuera del rango establecido.")
            numero = int(input("Ingrese un numero (Ingrese -1 para finalizar):"))
    return lista


lista_numeros = cargar_numeros()

if lista_numeros:
    print("Los números ingresados fueron", lista_numeros)
else:
    print("La lista se encuentra vacía. ")
