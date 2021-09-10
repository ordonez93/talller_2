opcion = 1

contactos = []

while opcion != 0:
    print('---------------------------------')
    print('Menu de contactos')
    print('1. Crear contactos')
    print('2. Listar contactos')
    print('3. Actualizar contactos')
    print('4. Eliminar contactos')
    print('0. Salir')

    opcion = int(input())

    if opcion == 1:
        nombre = input('Ingrese el nombre del contacto: ')
        apellido = input('Ingrese el apellidos del contacto: ')
        celular = input('Ingrese el celular del contacto: ')
        correo = input('Ingrese el correo del contacto: ')

        contactos.append({
            'nombre': nombre,
            'apellido': apellido,
            'celular': celular,
            'correo': correo,
        })

        input('Contacto guardado correctamente. Presione enter para continuar')
    elif opcion == 2:
        print(contactos)