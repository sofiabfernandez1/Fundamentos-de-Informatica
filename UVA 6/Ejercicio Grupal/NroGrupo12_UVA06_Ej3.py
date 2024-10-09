"""Diseñar dos funciones llamadas descuento y recargo: ambas recibirán un precio y un porcentaje (número entero entre 1 y 30). La primera devolverá el precio con el descuento aplicado, mientras que la segunda lo hará con el recargo aplicado.  
Desarrollar un programa principal que solicite precios hasta ingresar -1. Además, deberá solicitar el tipo de operación: 1: Descuento y 2: Recargo. Luego de cada ingreso deberá mostrar el precio con descuento o recargo de acuerdo a lo ingresado por el usuario. Validar que puedan ingresar solamente esas dos opciones. Mostrar la suma total de precios considerando todos los descuentos y recargos aplicados.  """

def descuento(precio,porcentaje):
    valor_descuento = precio * (porcentaje / 100)
    return precio - valor_descuento

def recargo(precio,recargo):
    valor_recargo = precio * (recargo / 100)
    return precio + valor_recargo

total_productos = 0

precio = int(input("Ingrese el precio del producto (Ingrese -1 para salir): "))

while precio != -1:
    operacion = int(input("Ingrese el tipo de operación: 1: Descuento - 2: Recargo: "))
    if operacion == 1:
        porcentaje_descuento = int(input("Ingrese el porcentaje del descuento (entre 1 y 30): "))
        if 1 <= porcentaje_descuento <= 30:
            precio_final = descuento(precio,porcentaje_descuento)
            total_productos += precio_final
            print("El valor de $", precio, "con un descuento del %",porcentaje_descuento, " es: $", precio_final)
        else:
            print("El porcentaje debe encontrarse entre 1 y 30.")
    elif operacion == 2:
        porcentaje_recargo = int(input("Ingrese el porcentaje del recargo (entre 1 y 30): "))
        if 1 <= porcentaje_recargo <= 30:
            precio_final = recargo(precio, porcentaje_recargo)
            total_productos += precio_final
            print("El valor de $", precio, "con un recargo del %",porcentaje_recargo, " es: $", precio_final)
        else:
            print("El porcentaje debe encontrarse entre 1 y 30.")
    else:
        print("Se ha ingresado una operación incorrecta.")
    precio = int(input("Ingrese el precio del producto (Ingrese -1 para salir): "))

if total_productos > 0:
    print("El total de los productos con descuento y recargo es: $", total_productos)
else:
    print("No se ha ingresado ningún producto.")