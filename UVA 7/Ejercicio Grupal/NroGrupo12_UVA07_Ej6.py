"""Una escuela necesita conocer cuántos alumnos cumplen años en cada mes, con el propósito de ofrecerles un agasajo especial en su día. 
Desarrollar un programa que lea el nombre, día y mes de cumpleaños de cada uno de los alumnos que concurren a dicha escuela. 
La carga finaliza ingresando una cadena vacía en el nombre del alumno (es decir, presionando solo la tecla ENTER). 
A medida que se ingresan los datos se deberá ir cargando en una lista (podría usar 2 también si lo considera necesario) la cantidad de cumpleaños por mes, 
según los datos ingresados en el programa hasta ese momento. 
Al finalizar, deberá imprimir el contenido de esa lista/s, de forma tal de informar cuántos alumnos cumplen años según el mes.  

Validar que se ingrese un mes correcto. Opcional: validar que no se ingrese un día que no corresponde a ese mes (ejemplo: no permitir 31 de septiembre).  
Nota: obviamente en este ejercicio no se deberán utilizar las funciones pedidas en los puntos 1 y 2.   """

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

nombre = str(input("Ingrese el nombre del alumno: "))
while nombre != "":
    dia = int(input("Ingrese el día de nacimiento: "))
    mes = int(input("Ingrese el mes de nacimiento: "))
    anio = int(input("Ingrese el año de nacimiento: "))
    if mes > 0 and mes <= 12:
        if dia > 0 and dia <= 31:
            print("Fecha valida")
            total_cumpleanios[mes - 1] += 1

    nombre = str(input("Ingrese el nombre del alumno: "))

mostrar_titulo(37, " | Informe de cumpleaños mes a mes | ")

for i in range(len(meses)):
    print(meses[i], ":", total_cumpleanios[i])
    print()

mayor_cantidad = calcular_maximo(total_cumpleanios)
print("El mes con mayor cantidad de cumpleaños es", meses[mayor_cantidad])