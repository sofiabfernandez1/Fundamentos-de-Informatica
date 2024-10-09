#Una mueblería necesita un sistema para ingresar 10 productos. Se pide ingresar categoría (A, B o C) y precio. Validar que el ingreso de la categoría sea de alguna de esas tres letras y que el precio sea positivo. Al finalizar, mostrar la cantidad de productos ingresados de cada categoría y el total de importes.  
categoria_A = 0
total_A = 0
categoria_B = 0
total_B = 0
categoria_C = 0
total_C = 0


for i in range(10):
    categoria = input("Ingrese la categoria del producto: ")
    if categoria == 'A' or categoria == 'B' or categoria == 'C':
        precio = float(input("Ingrese el precio del producto: "))
        if precio > 0:
            if categoria == 'A':
                categoria_A += 1
                total_A += precio
            elif categoria == "B":
                categoria_B += 1
                total_B += precio
            else:
                categoria_C += 1
                total_C += precio
        else:
            print("El precio ingresado debe ser mayor a 0.")
    else:
        print("La categoría ingresada es incorrecta.")

print("Productos ingresados para la Categoria A:", categoria_A, " - Importe total: ", total_A)

print("Productos ingresados para la Categoria B:", categoria_B, " - Importe total: ", total_B) 

print("Productos ingresados para la Categoria A:", categoria_C, " - Importe total: ", total_C)