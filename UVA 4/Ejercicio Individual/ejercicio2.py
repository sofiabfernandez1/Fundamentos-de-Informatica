#Leer un número entero e imprimir un mensaje indicando si es par o impar.  

numero = int(input("Ingrese un numero entero:"))

if numero % 2 == 0:
    print("El numero ingresado es par.")
else:
    print("El numero ingresado es impar. ")