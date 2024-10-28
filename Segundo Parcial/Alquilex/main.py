import random

def verificar_correo(usuarios,correo):
    for usuario in usuarios:
        if usuario['correo'] == correo:
            print("Error: El correo electrónico ingresado ya se encuentra registrado. Ingrese un correo válido. ")
            while correo == usuario['correo']:
                correo = input("Ingrese su correo electrónico: ")

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
    nuevo_usuario = {
        'id': nuevo_id,
        'tipo': tipo,
        'nombre': nombre,
        'correo': correo,
        'contrasenia': contrasenia,
        'telefono': telefono,
        'online': False
    }
    
    usuarios.append(nuevo_usuario)

    print("Usuario creado exitosamente.")

def verificar_sesion(usuarios, correo, contrasenia):
    """
    Verifica si el correo y contraseña son correctas.
    Si coinciden, actualiza el campo "status" del usuario a True y retorna el usuario.
    Retorna el usuario si las credenciales coinciden, o None si no.
    """
    for usuario in usuarios:
        if usuario['correo'] == correo and usuario['contrasenia'] == contrasenia:
            usuario['status'] = True  # Cambiar "status" a True al iniciar sesión correctamente
            return usuario
    return None

def iniciar_sesion(usuarios):
    intentos_fallidos = 0
    LIMITE_INTENTOS = 3

    print("---- Inicio de Sesión ----")
    while intentos_fallidos < LIMITE_INTENTOS:
        correo = str(input("Ingrese su correo electrónico: "))
        contrasenia = str(input("Ingrese su contraseña: "))

        # Verificar credenciales
        usuario = verificar_sesion(usuarios, correo, contrasenia)
        
        if usuario is not None:
            print("Inicio de sesión exitoso.")
            return usuario  # Retorna el usuario para que el sistema pueda usar sus datos si es necesario
        
        else:
            intentos_fallidos += 1
            print("Credenciales incorrectas. Intento", intentos_fallidos, "de", LIMITE_INTENTOS)

    print("Demasiados intentos fallidos. Acceso bloqueado temporalmente.")
    return None  # Retorna None si se supera el límite de intentos

def ver_perfil(usuario):
    """
    Muestra la información del perfil del usuario.
    """
    print("_______________________________")
    print("\n----- Perfil de Usuario -----")
    print("_______________________________")
    print("Nombre: ", usuario['nombre'])
    print("Correo: ",usuario['correo'])
    print("Teléfono: ",usuario['telefono'])
    print("Tipo de usuario: ",usuario['tipo'])
    print("\n_______________________________")

def editar_perfil(usuario):
    """
    Permite al usuario editar su perfil (teléfono y contraseña).
    """
    print("_______________________________")
    print("\n------- Editar Perfil -------")
    print("_______________________________")
    usuario['telefono'] = input("Ingrese el nuevo número de teléfono: ")
    usuario['contrasenia'] = input("Ingrese la nueva contraseña: ")
    print("Perfil actualizado exitosamente.")
    print("\n_______________________________")

def obtener_propiedades_por_usuario(propiedades, id_usuario):
    for propiedad in propiedades:
        if propiedad['id_usuario'] == id_usuario:  # Verificar si el id_usuario coincide
            print("-------------------")
            print("----- Propiedad", propiedad['id_propiedad'], "-----") 
            print("-------------------")
            print("Ubicacion: ", propiedad['ubicacion'])
            print("Precio:", propiedad['precio'])
            print("Servicios: ", propiedad['servicio'])
            print("Acceso a transporte: ", propiedad['acceso_transporte'])
            print("Tipo de propiedad: ", propiedad['tipo_propiedad'])
            print()


def opciones_usuario(usuario):
    """
    Muestra el menú de opciones solo si el usuario ha iniciado sesión (status=True).
    """
    if usuario['status']:
        print("\n---- Menú de Opciones ----")
        print("1. Ver perfil")
        print("2. Editar perfil")
        print("3. Propiedades contactadas")
        if usuario['tipo'] in ['Propietario', 'Inmobiliaria']:
            print("4. Propiedades publicadas")
            print("5. Publicar Propiedad")
            print("6. Cerrar Sesión")
            opcion = input("Seleccione una opción (1-6): ")
        else:
            print("4. Cerrar Sesión.")
            opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            print("Mostrando perfil de usuario...")
            ver_perfil(usuario)
        elif opcion == '2':
            print("Redirigiendo a la edición del perfil...")
            editar_perfil(usuario)
        elif opcion == "3":
            print("Propiedades contactadas.")
        elif usuario['tipo'] in ['Propietario', 'Inmobiliaria']:
            if opcion == '4':
                print("Propiedades publicadas.")
                obtener_propiedades_por_usuario(propiedades, usuario['id'])
            elif opcion == '5':
                print("Publicar propiedad.")
                cargar_propiedad(propiedades,usuario['id'])
            elif opcion == '6':
                usuario['status'] = False  # Cerrar sesión
                print("Sesión cerrada exitosamente.")
            else:
                print("Opción inválida.")
        else:
            if opcion == '4':
                usuario['status'] = False  # Cerrar sesión
                print("Sesión cerrada exitosamente.")
            else:
                print("Opción inválida.")
    else:
        print("Acceso denegado. Por favor, inicie sesión primero.")

def cargar_servicios(servicios):
    salir = False
    
    while not salir:
        opcion = input("¿Desea ingresar un servicio? (Sí - No): ")
        
        if opcion == "Sí":
            servicio = input("Ingrese un servicio: ")
            if servicio not in servicios:
                servicios.append(servicio)
                print("Servicio agregado exitosamente.")
            else:
                print("El servicio ya se encuentra en la lista.")
        
        elif opcion == "No":
            salir = True
            
        else:
            print("Opción inválida. Ingrese 'Sí' o 'No'.")
    
    return servicios
        
def generar_id_propiedad():
    id_propiedad = random.randint(100, 10000)

    id_unico = False
    
    while not id_unico:
        id_unico = True
        for propiedad in propiedades:
            if propiedad['id_propiedad'] == id_propiedad:
                id_unico = False
                id_propiedad = random.randint(100, 10000)
    
    return id_propiedad

def cargar_propiedad(propiedades, id_usuario):
    print("---- Cargar Nueva Propiedad ----")
    
    servicios = []

    # Solicitar detalles de la propiedad
    id_propiedad = generar_id_propiedad() #Genero el ID de la propiedad

    ubicacion = input("Ingrese la ubicación de la propiedad: ")
    precio = float(input("Ingrese el precio de la propiedad: "))
    habitaciones = int(input("Ingrese el número de habitaciones: "))
    
    servicio = cargar_servicios(servicios)
    acceso_transporte_input = input("¿Acceso a transporte público? (sí/no): ")
    acceso_transporte = acceso_transporte_input == "sí"  # Comparar directamente

    tipo_propiedad = input("Ingrese el tipo de propiedad (Casa/Departamento/Otros): ")

    # Crear un nuevo registro de propiedad
    nueva_propiedad = {
        'id': len(propiedades) + 1,  # Asignar un ID único
        'id_propiedad': id_propiedad,
        'ubicacion': ubicacion,
        'precio': precio,
        'habitaciones': habitaciones,
        'servicio': servicio,
        'acceso_transporte': acceso_transporte,
        'tipo_propiedad': tipo_propiedad,
        'id_usuario': id_usuario  # Asociar la propiedad con el usuario que la publica
    }
    
    # Añadir la nueva propiedad a la lista de propiedades
    propiedades.append(nueva_propiedad)

    return "Propiedad cargada exitosamente."




def menu(usuarios):
    print("----------------------------------------")
    print("------------- | ALQUILEX | -------------")
    print("----------------------------------------")

    salir = False
    while not salir:
        print("1. Registro de Usuario")
        print("2. Iniciar Sesion")
        print("3. Salir")
        print()
        opcion = int(input("Ingrese una opción: "))
        print()
        if opcion == 3:
            print("Sesión terminada.")
            salir = True
        elif opcion == 1:
            registrar_usuario(usuarios)
        elif opcion == 2:
            usuario = iniciar_sesion(usuarios)
            while usuario['status']:
                opciones_usuario(usuario)
        else:
            print("Se ha ingresado una opción inválida.")
            print()
    


#usuarios = []

usuarios = [
    {
        'id': 1,
        'tipo': 'Inquilino',
        'nombre': 'Juan Pérez',
        'correo': 'juan.perez@example.com',
        'contrasenia': 'password123',
        'telefono': '123456789',
        'status': False  # El usuario no ha iniciado sesión aún
    },
    {
        'id': 2,
        'tipo': 'Propietario',
        'nombre': 'Ana Gómez',
        'correo': 'ana.gomez@example.com',
        'contrasenia': 'securepass',
        'telefono': '987654321',
        'status': False  # El usuario no ha iniciado sesión aún
    },
    {
        'id': 3,
        'tipo': 'Inmobiliaria',
        'nombre': 'Inmobiliaria Los Pinos',
        'correo': 'contacto@lospinos.com',
        'contrasenia': 'pinos123',
        'telefono': '1122334455',
        'status': False  # El usuario no ha iniciado sesión aún
    }
]

# Lista de propiedades de ejemplo en CABA, Argentina, con identificador del usuario
propiedades = [
    {
        'id': 1,
        'id_propiedad': 101,
        'ubicacion': 'Palermo, CABA',
        'precio': 150000,
        'habitaciones': 2,
        'servicio': ['Agua Caliente', 'Internet'],
        'acceso_transporte': True,
        'tipo_propiedad': 'Departamento',
        'id_usuario': 3  # ID del usuario que publica la propiedad
    },
    {
        'id': 2,
        'id_propiedad': 102,
        'ubicacion': 'Recoleta, CABA',
        'precio': 200000,
        'habitaciones': 3,
        'servicio': ['Calefacción', 'Aire Acondicionado'],
        'acceso_transporte': True,
        'tipo_propiedad': 'Departamento',
        'id_usuario': 3
    },
    {
        'id': 3,
        'id_propiedad': 103,
        'ubicacion': 'Belgrano, CABA',
        'precio': 250000,
        'habitaciones': 4,
        'servicio': ['Seguridad 24 horas', 'Pileta'],
        'acceso_transporte': False,
        'tipo_propiedad': 'Casa',
        'id_usuario': 3
    },
    {
        'id': 4,
        'id_propiedad': 104,
        'ubicacion': 'San Telmo, CABA',
        'precio': 120000,
        'habitaciones': 1,
        'servicio': ['Luz', 'Gas Natural'],
        'acceso_transporte': True,
        'tipo_propiedad': 'Departamento',
        'id_usuario': 3
    },
    {
        'id': 5,
        'id_propiedad': 105,
        'ubicacion': 'La Boca, CABA',
        'precio': 80000,
        'habitaciones': 2,
        'servicio': ['Internet', 'Luz'],
        'acceso_transporte': True,
        'tipo_propiedad': 'Otros',
        'id_usuario': 2
    }
]


menu(usuarios)

print(usuarios)
