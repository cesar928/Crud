import sqlite3

#  crear la tabla 
def crear_tabla():
    conn.execute('''CREATE TABLE IF NOT EXISTS registros
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NOMBRE TEXT NOT NULL,
             EDAD INT NOT NULL,
             EMAIL TEXT NOT NULL);''')
    print("Tabla creada")

#  agregar un registro 
def agregar_registro():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    email = input("Ingrese el email: ")

    conn.execute("INSERT INTO registros (NOMBRE, EDAD, EMAIL) VALUES (?, ?, ?);", (nombre, edad, email))
    conn.commit()
    print("Registro agregado exitosamente.")

#  listar todos los registros
def listar_registros():
    cursor = conn.execute("SELECT * FROM registros;")
    for row in cursor:
        print("ID:", row[0])
        print("Nombre:", row[1])
        print("Edad:", row[2])
        print("Email:", row[3])
        print()

#  actualizar un registro
def actualizar_registro():
    id_actualizar = int(input("Ingrese el ID del registro a actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nuevo_edad = int(input("Ingrese la nueva edad: "))
    nuevo_email = input("Ingrese el nuevo email: ")

    conn.execute("UPDATE registros SET NOMBRE = ?, EDAD = ?, EMAIL = ? WHERE ID = ?;",
                 (nuevo_nombre, nuevo_edad, nuevo_email, id_actualizar))
    conn.commit()
    print("Registro actualizado exitosamente.")

#  eliminar 
def eliminar_registro():
    id_eliminar = int(input("Ingrese el ID del registro a eliminar: "))
    conn.execute("DELETE FROM registros WHERE ID = ?;", (id_eliminar,))
    conn.commit()
    print("Registro eliminado exitosamente.")

#  buscar 
def buscar_registro():
    id_buscar = int(input("Ingrese el ID del registro a buscar: "))
    cursor = conn.execute("SELECT * FROM registros WHERE ID = ?;", (id_buscar,))
    row = cursor.fetchone()
    if row:
        print("ID:", row[0])
        print("Nombre:", row[1])
        print("Edad:", row[2])
        print("Email:", row[3])
    else:
        print("Registro no encontrado.")

# Conexión 
conn = sqlite3.connect('registros.db')
crear_tabla()

# principal
while True:
    print("Menú:")
    print("1. Agregar registro")
    print("2. Listar registros")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Buscar registro por ID")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_registro()
    elif opcion == '2':
        listar_registros()
    elif opcion == '3':
        actualizar_registro()
    elif opcion == '4':
        eliminar_registro()
    elif opcion == '5':
        buscar_registro()
    elif opcion == '6':
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

#  salir
conn.close()