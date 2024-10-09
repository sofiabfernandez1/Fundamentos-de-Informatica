#Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso de que no lo sea.   

# Lista de meses
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# Solicitar al usuario un número de mes
numero_mes = int(input("Ingrese un número de mes (1-12): "))

# Verificar si el número es válido
if 1 <= numero_mes <= 12:
    print(f"El mes {numero_mes} es {meses[numero_mes - 1]}.")
else:
    print("Número de mes inválido. Debe ser entre 1 y 12.")  