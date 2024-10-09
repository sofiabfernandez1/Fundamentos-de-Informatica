""""Simular un ahorro de la sig. manera:
El monto para ahorrar debe ser introducido por teclado y debe estar comprendido entre
$80000 y $100000.Los depósitos semanales deben ser entre $5000 y $10000 hasta que se iguale o supere el monto a ahorrar.
Se debe informar el importe de los depósitos que se hicieron, la cantidad de depósitos que se hicieron, el promedio de depósitos, 
el mayor depósito efectuado y su posición, y el menor depósito efectuado y su posición."""

monto = float(input("Ingrese el monto a ahorar (entre $80000 y $100000): "))

while monto < 80000 or monto > 100000:
    print("El monto ingresado debe encontrarse entre $80000 y $100000.")
    monto = float(input("Ingrese el monto (entre $80000 y $100000) para ahorrar: "))

deposito = float(input("Ingrese el deposito para ahorrar (entre $5000 y $10000): "))

while deposito < 5000 or deposito > 10000:
    print("El monto ingresado debe encontrarse entre $5000 y $10000.")
    deposito = float(input("Ingrese el deposito para ahorrar (entre $5000 y $10000): "))

total_depositos = 0
cantidad_depositos = 0
deposito_mayor = 0
deposito_menor = 100000
posicion_mayor = 0
posicion_menor = 0

while total_depositos <= monto:
    if deposito >= 5000 and deposito <= 10000:
        cantidad_depositos += 1
        total_depositos += deposito

        if deposito > deposito_mayor:
            deposito_mayor = deposito
            posicion_mayor = cantidad_depositos
        
        if deposito < deposito_menor:
            deposito_menor = deposito
            posicion_menor = cantidad_depositos
    else:
        print("El monto ingresado debe encontrarse entre $5000 y $10000.")

    deposito = float(input("Ingrese el deposito para ahorrar (entre $5000 y $10000): "))
    print("total depositos: ", total_depositos)

if cantidad_depositos > 0:
    print("------------------------")
    print("Monto a ahorrar: ", monto)
    print("------------------------")
    print("Importe total de los depositos: ", total_depositos)
    print("Cantidad de depositos hechos: ", cantidad_depositos)
    print("Promedio de depositos: ", total_depositos / cantidad_depositos)
    print("El deposito mayor fue ", deposito_mayor, " en la posicion ", posicion_mayor)
    print("El deposito menor fue ", deposito_menor, " en la posicion ", posicion_menor)
else:
    print("No se ha ingresado ningún depósito.")