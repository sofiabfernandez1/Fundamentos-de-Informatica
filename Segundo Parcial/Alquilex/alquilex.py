usuarios = [
    [1, 'Inquilino', 'Juan Pérez', 'juan.perez@example.com', 'password123', '123456789', False],
    [2, 'Propietario', 'Ana Gómez', 'ana.gomez@example.com', 'securepass', '987654321', False],
    [3, 'Inmobiliaria', 'Inmobiliaria Los Pinos', 'contacto@lospinos.com', 'pinos123', '1122334455', False]
]

propiedades = [
    # Cada sublista representa una propiedad con sus atributos en un orden específico.
    [1, 101, 'Palermo, CABA', 150000, 2, ['Agua Caliente', 'Internet'], True, 'Departamento', 3],
    [2, 102, 'Recoleta, CABA', 200000, 3, ['Calefacción', 'Aire Acondicionado'], True, 'Departamento', 3],
    [3, 103, 'Belgrano, CABA', 250000, 4, ['Seguridad 24 horas', 'Pileta'], False, 'Casa', 3],
    [4, 104, 'San Telmo, CABA', 120000, 1, ['Luz', 'Gas Natural'], True, 'Departamento', 3],
    [5, 105, 'La Boca, CABA', 80000, 2, ['Internet', 'Luz'], True, 'Otros', 2]
]

def verificar_correo(usuarios, correo):
    filas = len(usuarios)
    correo_encontrado = True

    while correo_encontrado:
        correo_encontrado = False
        # Verifica si el correo ya está registrado
        for f in range(filas):
            if usuarios[f][3] == correo:
                print("Error: El correo electrónico ingresado ya se encuentra registrado. Ingrese un correo válido.")
                correo = input("Ingrese su correo electrónico: ")
                correo_encontrado = True
                # Terminamos el `for` de forma natural y volvemos a verificar con el nuevo correo


def validar_tipo(tipo):
    while tipo != "Inquilino" and tipo != "Propietario" and tipo != "Inmobiliaria":
        print("Ingrese una opción válida.")
        tipo = input("Ingrese la opción que corresponda: Inquilino - Propietario - Inmobiliaria: ")

    # Pedir nombre según el tipo de usuario
    if tipo == "Inquilino" or tipo == "Propietario":
        nombre = input("Ingrese su nombre completo: ")
    elif tipo == "Inmobiliaria":
        nombre = input("Ingrese el nombre de la inmobiliaria: ")
    
    return nombre


def registrar_usuario(usuarios):
    print("---- Registro de Usuario ----")
    tipo = input("Ingrese la opción que corresponda: Inquilino - Propietario - Inmobiliaria: ")

    # Validar tipo de usuario y obtener el nombre

    nombre = validar_tipo(tipo)
    
    correo = input("Ingrese su correo electrónico: ")

    # Verificar que el correo no esté registrado
    verificar_correo(usuarios,correo)

    contrasenia = input("Ingrese su contraseña: ")
    telefono = input("Ingrese su número de teléfono: ")

    # Crear un nuevo ID para el usuario
    nuevo_id = len(usuarios) + 1  # Asignar un ID único

    nuevo_usuario = [nuevo_id, tipo, nombre, correo, contrasenia, telefono, False] 

    usuarios.append(nuevo_usuario)

    print("Usuario creado exitosamente.")

def verificar_sesion(usuarios, correo, contrasenia):
    """
    Verifica si el correo y contraseña son correctas.
    Si coinciden, actualiza el campo "status" del usuario a True y retorna el usuario.
    Retorna el usuario si las credenciales coinciden, o None si no.
    """

    for usuario in usuarios:
        if usuario[3] == correo and usuario[4] == contrasenia:
            usuario[6] = True  # Cambiar "status" a True al iniciar sesión correctamente
            return usuario
    return None


def iniciar_sesion(usuarios):
    intentos_fallidos = 0
    limite_intentos = 3

    print("---- Inicio de Sesión ----")
    while intentos_fallidos < limite_intentos:
        correo = str(input("Ingrese su correo electrónico: "))
        contrasenia = str(input("Ingrese su contraseña: "))

        # Verificar credenciales
        usuario = verificar_sesion(usuarios, correo, contrasenia)
        
        if usuario is not None:
            print("Inicio de sesión exitoso.")
            return usuario  # Retorna el usuario para que el sistema pueda usar sus datos si es necesario
        
        else:
            intentos_fallidos += 1
            print("Credenciales incorrectas. Intento", intentos_fallidos, "de", limite_intentos)

    print("Demasiados intentos fallidos. Acceso bloqueado temporalmente.")
    return None  # Retorna None si se supera el límite de intentos


def ver_perfil(usuario):
    """
    Muestra la información del perfil del usuario.
    """
    print("_______________________________")
    print("\n----- Perfil de Usuario -----")
    print("_______________________________")
    print(f"Tipo de Usuario: {usuario[1]}")
    print(f"Nombre: {usuario[2]}")
    print(f"Correo: {usuario[3]}")
    print(f"Número de Teléfono: {usuario[5]}")
    print("\n_______________________________")


def editar_perfil(usuario):
    """
    Permite al usuario editar su perfil (teléfono y contraseña).
    """
    print("_______________________________")
    print("\n------- Editar Perfil -------")
    print("_______________________________")
    usuario[5] = input("Ingrese el nuevo número de teléfono: ")
    usuario[4] = input("Ingrese la nueva contraseña: ")
    print("Perfil actualizado exitosamente.")
    print("\n_______________________________")


def mostrar_usuarios(usuarios):
    print("---- Lista de Usuarios ----")
    for usuario in usuarios:
        print(f"ID: {usuario[0]}")
        print(f"Tipo: {usuario[1]}")
        print(f"Nombre: {usuario[2]}")
        print(f"Correo: {usuario[3]}")
        print(f"Número de Teléfono: {usuario[5]}")
        if usuario[6]:
            print("Estado: Conectado")
        else:
            print("Estado: Desconectado")
        print("---------------------------")



# Ejemplo de uso
usuarios = [
    [1, 'Inquilino', 'Juan Pérez', 'juan.perez@example.com', 'password123', '123456789', False],
    [2, 'Propietario', 'Ana Gómez', 'ana.gomez@example.com', 'securepass', '987654321', False],
    [3, 'Inmobiliaria', 'Inmobiliaria Los Pinos', 'contacto@lospinos.com', 'pinos123', '1122334455', False]
]

opcion = str(input("¿Quieres ingresar un usuario?"))
while opcion == "Si":
    registrar_usuario(usuarios)
    opcion = str(input("¿Quieres ingresar un usuario?"))

mostrar_usuarios(usuarios)