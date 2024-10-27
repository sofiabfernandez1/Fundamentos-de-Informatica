import random

def registrar_usuario(usuarios):
    print("---- Registro de Usuario ----")
    tipo = input("Ingrese la opción que corresponda: Inquilino - Propietario - Inmobiliaria: ")

    # Validar tipo de usuario
    while tipo != "Inquilino" and tipo != "Propietario" and tipo != "Inmobiliaria":
        print("Ingrese una opción válida.")
        tipo = input("Ingrese la opción que corresponda: Inquilino - Propietario - Inmobiliaria: ")

    # Pedir nombre según el tipo de usuario
    if tipo == "Inquilino" or tipo == "Propietario":
        nombre = input("Ingrese su nombre completo: ")
    elif tipo == "Inmobiliaria":
        nombre = input("Ingrese el nombre de la inmobiliaria: ")
    
    correo = input("Ingrese su correo electrónico: ")

    # Verificar que el correo no esté registrado
    for usuario in usuarios:
        if usuario['correo'] == correo:
            print("Error: El correo electrónico ingresado ya se encuentra registrado. Ingrese un correo válido. ")
            while correo == usuario['correo']:
                correo = input("Ingrese su correo electrónico: ")

    contrasenia = input("Ingrese su contraseña: ")
    telefono = input("Ingrese su número de teléfono: ")

    # Crear un nuevo ID para el usuario
    nuevo_id = len(usuarios) + 1  # Asignar un ID único
    nuevo_usuario = {
        'id': nuevo_id,
        'tipo': tipo,
        'nombre': nombre,
        'correo': correo,
        'contrasenia': contrasenia,
        'telefono': telefono
    }
    
    usuarios.append(nuevo_usuario)

    return "Usuario creado exitosamente."


def menu():
    print("----------------------------------------")
    print("------------- | ALQUILEX | -------------")
    print("----------------------------------------")
    
    

lista_usuarios = []


menu()

registrar_usuario(lista_usuarios)

print(lista_usuarios)
