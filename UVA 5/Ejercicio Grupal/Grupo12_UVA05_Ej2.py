#Un banco otorga a sus clientes una categoría de acuerdo al nivel de depósitos mensuales. Desarrollar un programa que permita ingresar importes positivos hasta que se ingrese -1. Si la suma de esos importes es mayor a 1.000.000 la categoría será “Oro”, si está entre 500.000 y 1.000.000 la categoría será “Platino” y en el resto de los casos “Estándar”. Mostrar la categoría. Realizar la prueba de escritorio para comprobar el correcto funcionamiento del programa. 

depositos = 0

importe = float(input("Ingrese los importes de la cuenta: "))
while importe != -1:
    depositos += importe
    importe = float(input("Ingrese los importes de la cuenta: "))

if depositos > 1000000:
    print("La categoría del cliente es ORO.")
elif depositos >= 500000 and depositos < 1000000:
    print("La categoría del cliente es PLATINO.")
else: 
    print("La categoría del cliente es ESTANDAR")