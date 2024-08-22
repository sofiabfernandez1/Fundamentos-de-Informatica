#Ingresar el valor de un producto. Luego, calcular el IVA (21%) y obtener el total de la factura.

producto = float(input("Ingrese el valor del producto: ")) 

iva = producto * 0.21

total = producto + iva

print("El valor del producto es: ", producto)

print("El IVA (%21) de $", producto, " es ", iva)

print("El valor total de la factura es: ", total)