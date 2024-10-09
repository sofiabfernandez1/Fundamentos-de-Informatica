# Desarrollar un programa que solicite ingresar tres números distintos, e indique por pantalla cuál de ellos es el menor número ingresado. Deberán verificar que los tres números ingresados sean distintos.   

numero_1 = int(input("Ingrese un número: "))

numero_2 = int(input(f"Ingrese un número distinto a {numero_1}: "))

numero_3 = int(input(f"Ingrese un número distinto a {numero_1} y {numero_2}: "))

if numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3:
    print("Los números ingresados deben ser distintos.")
else:
    if numero_1 < numero_2 and numero_1 < numero_3:
        menor = numero_1
    elif numero_2 < numero_1 and numero_2 < numero_3:
        menor = numero_2
    else:
        menor = numero_3

print("El número ingresado de menor valor es: ", menor)
