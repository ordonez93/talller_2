import mysql.connector 
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12523',
    database='blog',
    port=3306
)

def crearUsuario(nombre, email, contrasena):
    cursor = db.cursor()
    
    cursor.execute('''insert into 
        usuarios(nombre, email, contrasena)
        values(%s, %s, %s)''', (
          nombre,
          email,
          contrasena
        ))
    db.commit()
    cursor.close()


def listarUsuarios():
    cursor = db.cursor()
    cursor.execute('select * from usuarios')
    usuarios = cursor.fetchall()
    print(usuarios)
    cursor.close()


def modificarUsuario(nombre, email, contrasena,id):
    cursor = db.cursor()
    
    cursor.execute('''UPDATE usuarios set nombres = %s, email= %s,contasena = %s WHERE ID = %s''', (
          nombre,
          email,
          contrasena,
          id
        ))
    db.commit()

    cursor.close()

def eliminarUsuario(id):
    cursor = db.cursor()

    cursor.execute('''delete from usuarios where id = %s''', (
    id
    ))
    db.commit()
    cursor.close()

#crearUsuario('Jeyson', 'jeyson13@gmail.com', '12345678')

cursor = db.cursor()

cursor.execute('select * from usuarios')

usuarios = cursor.fetchall()

print(usuarios)



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

        input('Contacto guardado correctamente. Presione enter para continuar..')
    elif opcion == 2:
        print(contactos)