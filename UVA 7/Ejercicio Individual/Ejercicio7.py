"""Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año, 
con el propósito de ofrecerles un agasajo especial en su día. 
Desarrollar un programa que lea el número de legajo y fecha de nacimiento 
(día, mes y año) de cada uno de los alumnos que concurren a dicha escuela. 
La carga finaliza con un número de legajo igual a -1. Emitir un informe 
donde aparezca (mes por mes) cuántos alumnos cumplen años a lo largo del año. 
Mostrar también una leyenda que indique cuál es el mes con mayor cantidad de 
cumpleaños. """

def calcular_maximo(lista):
    maximo = lista[0] 
    indice_maximo = 0  

    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            indice_maximo = i 

    return indice_maximo

def mostrar_titulo(longitud,texto):
    print("*" * longitud)
    print(texto)
    print("*" * longitud)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
total_cumpleanios = [0]*12

legajo = int(input("Ingrese el número de legajo: "))
while legajo != -1:
    dia = int(input("Ingrese el día de nacimiento: "))
    mes = int(input("Ingrese el mes de nacimiento: "))
    anio = int(input("Ingrese el año de nacimiento: "))
    if mes > 0 and mes <= 12:
        if dia > 0 and dia <= 31:
            print("Fecha valida")
            total_cumpleanios[mes - 1] += 1

    legajo = int(input("Ingrese el número de legajo: "))

mostrar_titulo(37, " | Informe de cumpleaños mes a mes | ")

for i in range(len(meses)):
    print(meses[i], ":", total_cumpleanios[i])
    print()

mayor_cantidad = calcular_maximo(total_cumpleanios)
print("El mes con mayor cantidad de cumpleaños es", meses[mayor_cantidad])