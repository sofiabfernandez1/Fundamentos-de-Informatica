#Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico del libro es de $500, más $20,20 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo en $200. Además, si el número de páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en $336. Desarrollar un programa que calcule el costo de un libro dado el número de páginas.   

# Solicitar al usuario el número de páginas
num_paginas = int(input("Ingrese el número de páginas del libro: "))

# Costo básico y por página
costo_basico = 500
costo_por_pagina = 20.20

# Calcular el costo inicial (costo básico + costo por página)
costo_total = costo_basico + (num_paginas * costo_por_pagina)

# Verificar si se necesita encuadernación en tela
if num_paginas > 300:
    costo_total += 200

# Verificar si se necesita el procedimiento especial de encuadernación
if num_paginas > 600:
    costo_total += 336

# Mostrar el costo total del libro
print(f"El costo total del libro es: ${costo_total:.2f}")