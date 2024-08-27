""""
Utilizar la instrucción print para mostrar cada resultado de las siguientes expresiones. Explicar en un comentario de una sola línea el orden que ejecuta el intérprete Python en cada una de ellas. Ejemplo: 12*4+4*5 = 68 orden: multiplicación, suma: 
12 * 4 + 4 * 5 

12 * (4 + 4) * 5 

5 * 4 / 2 

5 * (4 / 2)  

(12 + (12 + 6 * 4)) / 3 

3 * ((4 + 5) / (18 / 6) - 4) 
"""

print(12*4+4*5)
# Orden: Multiplicación, suma

print(12 * (4 + 4) * 5)
# Orden: Paréntesis (suma), multiplicación

print(5 * 4 / 2)  
# Orden: Multiplicación, división

print(5 * (4 / 2))
# Orden: Paréntesis (división), multiplicación

print((12 + (12 + 6 * 4)) / 3)
# Orden: Paréntesis interior (multiplicación, suma), Paréntesis (suma), División

print(3 * ((4 + 5) / (18 / 6) - 4))
# Orden: Paréntesis interior (suma), Paréntesis interior (división), Paréntesis (Resta), Paréntesis (multiplicación)



