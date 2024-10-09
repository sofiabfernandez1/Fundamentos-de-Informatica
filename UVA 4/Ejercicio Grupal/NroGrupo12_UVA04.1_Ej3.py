""""Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario. Tiene la siguiente tarifa:  
Viaje mínimo $50 

Si recorre entre 0 y 10 km: $20/km 

Si recorre 10 km o más: $15/km """

print("------------------------------------------------------")
print("---------- Sistema de tarifa por Kilometros ---------- ")
print("------------------------------------------------------\n")

kms = float(input("Ingrese la cantidad de Kilometros del viaje: "))

if kms >=0 and kms < 10:
    tarifa = kms * 20
    print("El total a pagar por ", kms, "kilometros es de:", tarifa)
else:
    tarifa = kms * 15
    print("El total a pagar por ", kms, "kilometros es de:", tarifa)

