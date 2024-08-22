#Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una. 

inversion1 = float(input("Ingresa la inversión de la primera persona: "))
inversion2 = float(input("Ingresa la inversión de la segunda persona: "))
inversion3 = float(input("Ingresa la inversión de la tercera persona: "))

total_inversion = inversion1 + inversion2 + inversion3

porcentaje1 = (inversion1 / total_inversion) * 100
porcentaje2 = (inversion2 / total_inversion) * 100
porcentaje3 = (inversion3 / total_inversion) * 100

print("Porcentaje de inversión de la primera persona: ", porcentaje1, "%")
print("Porcentaje de inversión de la segunda persona: ", porcentaje2, "%")
print("Porcentaje de inversión de la tercera persona: ", porcentaje3, "%")