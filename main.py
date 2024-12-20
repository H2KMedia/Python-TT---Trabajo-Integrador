import os
import sqlite3

# Función para crear la base de datos y la tabla si no existen
def inicializar_bd():
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            autor TEXT NOT NULL,
            titulo TEXT NOT NULL,
            editorial TEXT,
            edicion INTEGER,
            isbn INTEGER,
            stock INTEGER,
            precio REAL
        )
    ''')
    conn.commit()
    conn.close()

# Función para agregar un nuevo registro
def agregar_registro():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        autor = input("INGRESE EL AUTOR: ")
        titulo = input("INGRESE EL TITULO: ")
        editorial = input("INGRESE LA EDITORIAL: ")
        edicion = int(input("INGRESE LA EDICIÓN: "))
        isbn = int(input("INGRESE EL CÓDIGO ISBN: "))
        stock = int(input("INGRESE EL STOCK: "))
        precio = float(input("INGRESE EL PRECIO: "))

        confirmar = input("¿DESEA GUARDAR EL REGISTRO? (S/N): ")
        if confirmar.upper() == 'S':
            conn = sqlite3.connect('stock.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO registros (autor, titulo, editorial, edicion, isbn, stock, precio)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (autor, titulo, editorial, edicion, isbn, stock, precio))
            conn.commit()
            conn.close()
            print("REGISTRO GUARDADO CORRECTAMENTE")

        otro = input("¿DESEA CARGAR OTRO REGISTRO? (S/N): ")
        if otro.upper() != 'S':
            break

# Función para modificar un registro
def modificar_registro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("OPCIONES DE BÚSQUEDA: ")
    print(" 1. ID")
    print(" 2. AUTOR ")
    print(" 3. TÍTULO")
    opcion = int(input("SELECCIONE UNA OPCIÓN: "))

    if opcion == 1:
        referencia = input("INGRESE EL ID: ")
        campo_busqueda = "id"
    elif opcion == 2:
        referencia = input("INRESE EL AUTORr: ")
        campo_busqueda = "autor"
    elif opcion == 3:
        referencia = input("INGRESE EL TÍTULO: ")
        campo_busqueda = "titulo"
    else:
        print("OPCIÓN NO VÁLIDA, INTENTE NUEVAMENTE")
        return

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT * FROM registros WHERE {campo_busqueda} = ?
    ''', (referencia,))
    registro = cursor.fetchone()

    if registro:
        id_registro = registro[0]
        print(f"ID: {registro[0]}, AUTOR: {registro[1]}, TITULO: {registro[2]}, EDITORIAL: {registro[3]}, EDICIÓN: {registro[4]}, ISBN: {registro[5]}STOCK: {registro[6]}, PRECIO: {registro[7]}")
        
        nuevo_autor = input("INGRESE EL NUEVO AUTOR (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[1]
        nuevo_titulo = input("INGRESE EL NUEVO TÍTULO (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[2]
        nuevo_editorial = input("INGRESE LA NUEVA EDITORIAL (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[3]
        nuevo_edicion = input("INGRESE EL NUEVO AÑO DE EDICIÓN (DEJAR EN BLANCO PARA NO MODIFICAR): ")
        nuevo_edicion = int(nuevo_edicion) if nuevo_edicion else registro[4]
        nuevo_isbn = input("INGRESE EL NUEVO CÓDIGO ISBN (DEJAR EN BLANCO PARA NO MODIFICAR): ")
        nuevo_isbn = int(nuevo_isbn) if nuevo_isbn else registro[5]
        nuevo_stock = input("INGRESE EL NUEVO STOCK (DEJAR EN BLANCO PARA NO MODIFICAR): ")
        nuevo_stock = int(nuevo_stock) if nuevo_stock else registro[6]
        nuevo_precio = input("INGRESE EL NUEVO PRECIO (DEJAR EN BLANCO PARA NO MODIFICAR: ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else registro[7]

        print(f"AW MODIFICARÁN LOS DATOS: AUTOR: {nuevo_autor}, TÍTULO: {nuevo_titulo}, EDITORIAL: {nuevo_editorial}, EDICIÓN: {nuevo_edicion}, ISBN: {nuevo_isbn}, STOCK: {nuevo_stock}, PRECIO: {nuevo_precio}")
        confirmar = input("¿DESEA GUARDAR LOS CAMBIOS? (S/N): ")

        if confirmar.upper() == 'S':
            cursor.execute('''
                UPDATE registros SET autor = ?, titulo = ?, editorial = ?, edicion = ?, isbn = ?, stock = ?, precio = ?
                WHERE id = ?
            ''', (nuevo_autor, nuevo_titulo, nuevo_editorial, nuevo_edicion, nuevo_isbn, nuevo_stock, nuevo_precio, id_registro))
            conn.commit()
            print("REGISTRO MODIFICADO.")
    else:
        print("REGISTRO NO ENCONTRADO.")
    
    conn.close()

# Función para eliminar un registro
def eliminar_registro():
    os.system('cls' if os.name == 'nt' else 'clear')
    id_eliminar = input("INGRESE EL ID DEL REGISTRO A ELIMINAR: ")

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM registros WHERE id = ?
    ''', (id_eliminar,))
    registro = cursor.fetchone()

    if registro:
        print(f"ID: {registro[0]}, AUTOR: {registro[1]}, TITULO: {registro[2]}, EDITORIAL: {registro[3]}, EDICIÓN: {registro[4]}, ISBN: {registro[5]}STOCK: {registro[6]}, PRECIO: {registro[7]}")
        confirmar = input("¿DESEA ELIMINAR ESTE REGISTRO? (S/N): ")

        if confirmar.upper() == 'S':
            confirmar_dos = input("¿ESTÁ SEGURO QUE DESEA ELIMINAR ESTE REGISTRO? (ESTA ACCIÓN NO SE PUEDE DESHACER) (S/N): ")
            if confirmar_dos.upper() == 'S':
                cursor.execute('''
                    DELETE FROM registros WHERE id = ?
                ''', (id_eliminar,))
                conn.commit()
                print("REGISTRO ELIMINADO")
    else:
        print("REGISTRO NO ENCONTRADO")
    
    conn.close()

# Función para listar registros
def listar_registros():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("OPCIONES DE LISTADO: ")
    print(" 1. TODOS LOS REGISTROS ")
    print(" 2. REPORTE DE STOCK MÍNIMO")
    opcion = int(input("SELECCIONE UNA OPCIÓN: "))

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    
    if opcion == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        cursor.execute('''
            SELECT * FROM registros ORDER BY id
        ''')
    elif opcion == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        stock_limite = int(input("INGRESE LA CANTIDAD LÍMITE DE STOCK: "))
        cursor.execute('''
            SELECT * FROM registros WHERE stock <= ? ORDER BY id
        ''', (stock_limite,))
    else:
        print("OPCIÓN NO VÁLIDA.")
        input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
        os.system('cls' if os.name == 'nt' else 'clear')
        conn.close()
        return
    
    registros = cursor.fetchall()
    for registro in registros:
        print(f"ID: {registro[0]}, AUTOR: {registro[1]}, TITULO: {registro[2]}, EDITORIAL: {registro[3]}, EDICIÓN: {registro[4]}, ISBN: {registro[5]}STOCK: {registro[6]}, PRECIO: {registro[7]}")
    
    conn.close()

# Función principal del menú
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\nMENÚ PRINCIPAL:")
        print("1. ALTA")
        print("2. MODIFICAR")
        print("3. ELIMINAR")
        print("4. LISTADOS")
        print("0. SALIR")
        opcion = int(input("SELECCIONE UNA OPCIÓN: "))

        if opcion == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            agregar_registro()
        elif opcion == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            modificar_registro()
        elif opcion == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            eliminar_registro()
        elif opcion == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            listar_registros()
        elif opcion == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("...::: SALIENDO DEL PROGRAMA :::...")
            print()
            print("´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶")
            print("´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´¶¶")
            print("´´´´´´¶¶¶¶¶´´´´´´´¶¶´´´´´´´´´´´´´´¶¶")
            print("´´´´´¶´´´´´¶´´´´¶¶´´´´´¶¶´´´´¶¶´´´´´¶¶")
            print("´´´´´¶´´´´´¶´´´¶¶´´´´´´¶¶´´´´¶¶´´´´´´´¶¶")
            print("´´´´´¶´´´´¶´´¶¶´´´´´´´´¶¶´´´´¶¶´´´´´´´´¶¶")
            print("´´´´´´¶´´´¶´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´¶¶")
            print("´´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´¶¶")
            print("´´´¶´´´´´´´´´´´´¶´¶¶´´´´´´´´´´´´´¶¶´´´´´¶¶")
            print("´´¶¶´´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´¶¶´´´´´¶¶")
            print("´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶´´´´´´´´¶¶´´´´´´´¶¶")
            print("´¶´´´´´´´´´´´´´´´¶´´´´´¶¶¶¶¶¶¶´´´´´´´´´¶¶")
            print("´¶¶´´´´´´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´¶¶")
            print("´´¶´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´¶¶")
            print("´´¶¶´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´´´´´¶¶")
            print("´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´¶¶")
            print("´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶")
            print()
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
            break
        else:
            print("OPCIÓN NO VÁLIDA")
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

# Ejecución del programa
if __name__ == '__main__':
    inicializar_bd()
    menu()
