import os
import sqlite3

def crear_conexion():
    # Crear la carpeta "bases" si no existe
    if not os.path.exists("bases"):
        os.makedirs("bases")
    
    # Crear una conexión a la base de datos SQLite
    conexion = sqlite3.connect("./bases/base_main.db")
    return conexion

def crear_tabla():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            anio TEXT NOT NULL,
            editorial TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            genero TEXT NOT NULL,
            unidades INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                       MENÚ DE OPCIONES DISTRIBUIDORA LIBROS                                                        |")
    print(150*"-")
    print("|                                                                                                                                                    |")
    print("|                                                             1 - REGISTRAR LIBRO                                                                    |")
    print("|                                                             2 - ACTUALIZAR LIBRO                                                                   |")
    print("|                                                             3 - ELIMINAR LIBRO                                                                     |")
    print("|                                                             4 - BUSCAR LIBRO                                                                       |")
    print("|                                                             5 - LISTAR LIBROS                                                                      |")
    print("|                                                             6 - REPORTE DE LIBROS CON BAJO STOCK                                                   |")
    print("|                                                             0 - SALIR DE SISTEMA                                                                   |")
    print("|                                                                                                                                                    |")
    print(150*"-")

def mostrar_submenu_registrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                           SUBMENÚ : REGISTRO DE LIBRO                                                              |")
    print(150*"-")
    print("|                                                        INGRESE LOS DATOS DEL NUEVO REGISTRO:                                                       |")
    print(150*"-")
    print()

def registrar_libro(titulo, autor, anio, editorial, isbn, genero, unidades, precio):
    conexion = sqlite3.connect("./bases/base_main.db")
    cursor =conexion.cursor()
    query = '''
        INSER INTo libros (titulo, autor, anio, editorial, isbn, genero, unidades, preio)
        VALUES (?,?,?,?,?,?,?,?)
    '''
    cursor.execute(query, ())
    mostrar_submenu_registrar()
    titulo = input("TÍTULO: ").upper()
    autor = input("AUTOR: ").upper()
    anio = input("AÑO DE EDICIÓN: ").upper()
    editorial = input("EDITORIAL: ").upper()
    isbn = validar_isbn()
    
    unidades = input("CANTIDAD DE UNIDADES: ").upper()
    precio = input("PRECIO VENTA: ").upper()

    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO libros (titulo, autor, anio, editorial, isbn, unidades, precio)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (titulo, autor, anio, editorial, isbn, unidades, precio))
    conexion.commit()
    conexion.close()
    print("LIBRO REGISTRADO EXITOSAMENTE")
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

def listar_libros():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM libros')
    libros = cursor.fetchall()
    conexion.close()

    print(150*"-")
    print("|                                                                  LISTADO DE LIBROS                                                                 |")
    print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
    print("| ID  | TÍTULO                                     | AUTOR                      | AÑO  | EDITORIAL                 | ISBN          | STOCK | PRECIO  |")
    print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
    for libro in libros:
        print(f"| {libro[0]:<3} | {libro[1]:<42} | {libro[2]:<26} | {libro[3]:<4} | {libro[4]:<25} | {libro[5]:<13} |   {libro[6]:<3} | ${libro[7]:<6} |")
    print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")

def buscar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                           SUBMENÚ : BÚSQUEDA DE LIBRO                                                              |")
    print(150*"-")
    print("|                                                        SELECCIONE CRITERIO DE BÚSQUEDA:                                                            |")
    print(150*"-")
    print("|                                                      1 - ID                                                                                         |")
    print("|                                                      2 - EDITORIAL                                                                                  |")
    print("|                                                      3 - TÍTULO                                                                                     |")
    print("|                                                      4 - AUTOR                                                                                      |")
    print(150*"-")

    criterio = input("SELECCIONE UNA OPCIÓN: ")
    valor_busqueda = input("INGRESE EL VALOR DE BÚSQUEDA: ").upper()

    conexion = crear_conexion()
    cursor = conexion.cursor()

    if criterio == '1':
        cursor.execute('SELECT * FROM libros WHERE id = ?', (valor_busqueda,))
    elif criterio == '2':
        cursor.execute('SELECT * FROM libros WHERE editorial = ?', (valor_busqueda,))
    elif criterio == '3':
        cursor.execute('SELECT * FROM libros WHERE titulo = ?', (valor_busqueda,))
    elif criterio == '4':
        cursor.execute('SELECT * FROM libros WHERE autor = ?', (valor_busqueda,))

    libros_encontrados = cursor.fetchall()
    conexion.close()

    if libros_encontrados:
        print(150*"-")
        print("|                                                      RESULTADOS DE LA BÚSQUEDA                                                                     |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
        print("| ID  | TÍTULO                                     | AUTOR                      | AÑO  | EDITORIAL                 | ISBN          | STOCK | PRECIO  |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
        for libro in libros_encontrados:
            print(f"| {libro[0]:<3} | {libro[1]:<42} | {libro[2]:<26} | {libro[3]:<4} | {libro[4]:<25} | {libro[5]:<13} |   {libro[6]:<3} | ${libro[7]:<6} |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
    else:
        print("NO SE ENCONTRARON LIBROS QUE COINCIDAN CON EL CRITERIO DE BÚSQUEDA")
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

def eliminar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                           SUBMENÚ : ELIMINAR LIBRO                                                                  |")
    print(150*"-")

    id_libro = input("INGRESE EL ID DEL LIBRO A ELIMINAR: ")

    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM libros WHERE id = ?', (id_libro,))
    libro_a_eliminar = cursor.fetchone()

    if libro_a_eliminar:
        print(150*"-")
        print(f"LIBRO SELECCIONADO: ID {libro_a_eliminar[0]}, TÍTULO: {libro_a_eliminar[1]}, AUTOR: {libro_a_eliminar[2]}")
        confirmar1 = input("¿ESTÁ SEGURO QUE DESEA ELIMINAR ESTE LIBRO? (S/N): ")
        if confirmar1.upper() == 'S':
            confirmar2 = input("¿REALMENTE ESTÁ SEGURO? ESTA ACCIÓN NO SE PUEDE DESHACER. (S/N): ")
            if confirmar2.upper() == 'S':
                cursor.execute('DELETE FROM libros WHERE id = ?', (id_libro,))
                conexion.commit()
                print("LIBRO ELIMINADO EXITOSAMENTE")
            else:
                print("ELIMINACIÓN CANCELADA")
        else:
            print("ELIMINACIÓN CANCELADA")
    else:
        print("NO SE ENCONTRÓ NINGÚN LIBRO CON EL ID PROPORCIONADO")
    conexion.close()
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
    
def validar_isbn():
    while True:
        isbn = input("NÚMERO ISBN: ").upper()
        if isbn.isdigit() and len(isbn) <= 14:
            return isbn
        else:
            print("ERROR: EL ISBN DEBE SER NUMÉRICO Y NO TENER MÁS DE 14 CARACTERES.")

def modificar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                           SUBMENÚ : MODIFICAR LIBRO                                                                 |")
    print(150*"-")
    print("|                                                        SELECCIONE CRITERIO DE BÚSQUEDA:                                                            |")
    print(150*"-")
    print("|                                                      1 - ID                                                                                         |")
    print("|                                                      2 - ISBN                                                                                       |")
    print(150*"-")

    criterio = input("SELECCIONE UNA OPCIÓN: ")
    valor_busqueda = input("INGRESE EL VALOR DE BÚSQUEDA: ").upper()

    conexion = crear_conexion()
    cursor = conexion.cursor()

    if criterio == '1':
        cursor.execute('SELECT * FROM libros WHERE id = ?', (valor_busqueda,))
    elif criterio == '2':
        cursor.execute('SELECT * FROM libros WHERE isbn = ?', (valor_busqueda,))

    libro_a_modificar = cursor.fetchone()
    conexion.close()

    if libro_a_modificar:
        print(150*"-")
        print(f"LIBRO SELECCIONADO: ID {libro_a_modificar[0]}, TÍTULO: {libro_a_modificar[1]}, AUTOR: {libro_a_modificar[2]}")
        nuevo_titulo = input("NUEVO TÍTULO (DEJAR VACÍO PARA NO MODIFICAR): ").upper() or libro_a_modificar[1]
        nuevo_autor = input("NUEVO AUTOR (DEJAR VACÍO PARA NO MODIFICAR): ").upper() or libro_a_modificar[2]
        nuevo_anio = input("NUEVO AÑO (DEJAR VACÍO PARA NO MODIFICAR): ").upper() or libro_a_modificar[3]
        nueva_editorial = input("NUEVA EDITORIAL (DEJAR VACÍO PARA NO MODIFICAR): ").upper() or libro_a_modificar[4]
        nuevo_isbn = validar_isbn() or libro_a_modificar[5]
        nuevas_unidades = input("NUEVAS UNIDADES (DEJAR VACÍO PARA NO MODIFICAR): ").upper() or libro_a_modificar[6]
        nuevo_precio = input("NUEVO PRECIO (DEJAR VACÍO PARA NO MODIFICAR): ").upper() or libro_a_modificar[7]

        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE libros 
            SET titulo = ?, autor = ?, anio = ?, editorial = ?, isbn = ?, unidades = ?, precio = ?
            WHERE id = ?
        ''', (nuevo_titulo, nuevo_autor, nuevo_anio, nueva_editorial, nuevo_isbn, nuevas_unidades, nuevo_precio, libro_a_modificar[0]))
        conexion.commit()
        conexion.close()
        print("LIBRO MODIFICADO EXITOSAMENTE")
    else:
        print("NO SE ENCONTRÓ NINGÚN LIBRO CON EL CRITERIO PROPORCIONADO")

    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

# Crear la base de datos y la tabla si no existen
crear_tabla()

# Menú principal
while True:
    mostrar_menu()
    opcion = input("SELECCIONE UNA OPCIÓN: ").upper()
    if opcion == '1':
        registrar_libro()
    elif opcion == '2':
        modificar_libro()
    elif opcion == '3':
        eliminar_libro()
    elif opcion == '4':
        buscar_libro()
    elif opcion == '5':
        listar_libros()
    elif opcion == '6':
        # Aquí puedes implementar un reporte de libros con bajo stock si lo deseas
        pass
    elif opcion == '0':
        break
    else:
        print("OPCIÓN NO VÁLIDA, INTENTE NUEVAMENTE.")
