"""La Comisión Nacional de Investigaciones Espaciales de Argentina, está rastreando varias naves espaciales en la Galaxia Andrómeda y necesita un programa en Python que permita al usuario ingresar el nombre de una nave espacial, la distancia en millones de kilómetros desde la Tierra hasta la nave y la velocidad en kilómetros por hora a la que se está moviendo la nave. El programa deberá calcular el tiempo que tardaría la nave en llegar a la Tierra desde su ubicación actual. El programa deberá preguntar al usuario si desea ingresar otra nave. Si la respuesta no es 'Si' o 'si' para continuar o 'No' o 'no' para terminar, el programa deberá mostrar un mensaje de advertencia y volver a solicitar la entrada.

Al finalizar el programa debe realizar determinar también:

Cuál es la nave que tardara más en llegar a la tierra, indicando nombre, tiempo y distancia de la nave.
Cuantas naves se ingresaron para verificación
Cuantas están a más de 110km de km de distancia
 

Se requiere que el programa informe como comentarios lo que va realizando en cada paso que corresponda indicar y también un resumen de lo que realiza el programa explicando el paso a paso. Indicar también las variables utilizadas y de que tipo son."""

"""Datos a ingresar:
- Nombre de la nave espacial.
- Distancia en millones kilometros desde la tierra hasta la nave.
- Velocidad de kilometros por hora a la que se está moviendo la nave.

Calcular:
- Tiempo que tardaría en llegar la nave a la tierra desde su ubicación actual.
- Cual es la nave que tarda mas en llegar a la tierra.
- Cuantas naves se ingresaron.
- Cuantas están a más de 110km de distancia. 


El programa deberá:
- Preguntar al usuario si desea ingresar otra nave.
- "Si" o "No"
"""

nave_lenta = 0 # variable integer
nombre_nave_lenta = "" # variable string
tiempo_nave_lenta = 0 # variable float
distancia_nave_lenta = 0.0 # variable float
tiempo_nave_lenta = 0.0 # variable float
cantidad_naves = 0 # variable integer
naves_mayor_110km = 0 # variable integer

# Introduzco los datos de la nave
nombre_nave = str(input("Ingrese el nombre de la nave: ")) # variable: String
distancia_tierra = float(input("Ingrese la distancia de la nave con la tierra: ")) # variable: integer
velocidad_nave = float(input("Ingrese la velocidad en kilómetros con la que se está desplazando la nave: ")) #variable float

# Calculo el tiempo que tarda en llegar la nave a la tierra y lo imprimo en pantalla
tiempo_nave = (distancia_tierra * 1_000_000) / velocidad_nave #variable float
print("El tiempo en que la nave ", nombre_nave, "tarda en llegar a la tierra es ", tiempo_nave)

# Calculo cual es la nave más lenta
if tiempo_nave > tiempo_nave_lenta:
    tiempo_nave_lenta = tiempo_nave #actualizo el valor de la variable por el nuevo valor
    nombre_nave_lenta = nombre_nave #actualizo el valor de la variable por el nuevo valor
    distancia_nave_lenta = distancia_tierra #actualizo el valor de la variable por el nuevo valor

# Calculo la cantidad de naves que están a más de 110 millones de km
if distancia_tierra > 110:
    naves_mayor_110km += 1 # incremento el valor de la variable en caso de que se cumpla la condición.

cantidad_naves += 1 # variable integer. Sumo 1 a la cantidad de naves ingresadas.

# Pregunto si se desea ingresar otra nave.
opcion = str(input("¿Desea ingresar otra nave? (Si/No): ")) # variable string

# Valido las opciones. El while se corre si la opción ingresada es diferente a Si, si, No o No.
while opcion != "Si" and opcion != "si" and opcion != "No" and opcion != "no":
    print("ADVERTENCIA: Se ha ingresado una opción inválida.")
    opcion = str(input("¿Desea ingresar otra nave? (Si/No): ")) # variable string

# En caso de que se deseen ingresar más nave, se entra al siguiente loop
while opcion == "Si" or opcion == "si":
    # Introduzco los datos de la nave
    nombre_nave = str(input("Ingrese el nombre de la nave: ")) # Tipo de variable: String
    distancia_tierra = float(input("Ingrese la distancia de la nave con la tierra: ")) # tipo de variable: integer
    velocidad_nave = float(input("Ingrese la velocidad en kilómetros con la que se está desplazando la nave: "))
    
    # Calculo el tiempo que tarda en llegar la nave a la tierra y lo imprimo en pantalla   
    tiempo_nave = (distancia_tierra * 1_000_000) / velocidad_nave
    print("El tiempo en que la nave ", nombre_nave, "tarda en llegar a la tierra es ", tiempo_nave)

    # Calculo cual es la nave más lenta
    if tiempo_nave > tiempo_nave_lenta:
        tiempo_nave_lenta = tiempo_nave #actualizo el valor de la variable por el nuevo valor
        nombre_nave_lenta = nombre_nave #actualizo el valor de la variable por el nuevo valor
        distancia_nave_lenta = distancia_tierra #actualizo el valor de la variable por el nuevo valor

    # Calculo la cantidad de naves que están a más de 110 millones de km
    if distancia_tierra > 110:
        naves_mayor_110km += 1 # incremento el valor de la variable en caso de que se cumpla la condición.

    cantidad_naves += 1 # variable integer. Sumo 1 a la cantidad de naves ingresadas.
    
    # Pregunto si se desea ingresar otra nave.
    opcion = input("¿Desea ingresar otra nave? (Si/No): ") # variable string

    # Valido las opciones. El while se corre si la opción ingresada es diferente a Si, si, No o No.
    while opcion != "Si" and opcion != "si" and opcion != "No" and opcion != "no":
        print("ADVERTENCIA: Se ha ingresado una opción inválida.") # Imprimo una advertencia si la opción ingresada es inválida.
        opcion = str(input("¿Desea ingresar otra nave? (Si/No): ")) # variable string


# Resultados finales

print("----------------------")
print("----- RESULTADOS -----")
print("----------------------")

print("La nave que tardará más en llegar a la tierra es ", nombre_nave_lenta, " a una distancia de ", distancia_nave_lenta, " con tiempo de llegada ", tiempo_nave_lenta, "." )
print("Se ingresaron ", cantidad_naves, " para verificación.")
if naves_mayor_110km: # Si hay naves a más de 110 millones de km, ingreso al if. Sino se enseña el mensaje del else.
    print(naves_mayor_110km, " naves se encuentran a más de 110km de distancia.")
else:
    print("Ninguna nave se encuentra a más de 100 millones de kilometros de la tierra.")
