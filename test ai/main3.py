import sqlite3

# Función para crear la base de datos y la tabla si no existen
def inicializar_bd():
    conn = sqlite3.connect('stock_libros.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS REGISTROS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AUTOR TEXT,
            TITULO TEXT,
            STOCK INTEGER,
            PRECIO REAL
        )
    ''')
    conn.commit()
    conn.close()

# Función para agregar un nuevo registro
def agregar_registro():
    while True:
        autor = input("INGRESE EL AUTOR: ").upper()
        titulo = input("INGRESE EL TÍTULO: ").upper()
        stock = int(input("INGRESE EL STOCK: "))
        precio = float(input("INGRESE EL PRECIO: "))

        confirmar = input("¿DESEA GUARDAR EL REGISTRO? (S/N): ").upper()
        if confirmar == 'S':
            conn = sqlite3.connect('stock_libros.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO REGISTROS (AUTOR, TITULO, STOCK, PRECIO)
                VALUES (?, ?, ?, ?)
            ''', (autor, titulo, stock, precio))
            conn.commit()
            conn.close()
            print("REGISTRO GUARDADO.")

        otro = input("¿DESEA CARGAR OTRO REGISTRO? (S/N): ").upper()
        if otro != 'S':
            break

# Función para modificar un registro
def modificar_registro():
    print("OPCIONES DE BÚSQUEDA: 1. ID 2. AUTOR 3. TÍTULO")
    opcion = int(input("SELECCIONE UNA OPCIÓN: "))

    if opcion == 1:
        referencia = input("INGRESE EL ID: ")
        campo_busqueda = "ID"
    elif opcion == 2:
        referencia = input("INGRESE EL AUTOR: ").upper()
        campo_busqueda = "AUTOR"
    elif opcion == 3:
        referencia = input("INGRESE EL TÍTULO: ").upper()
        campo_busqueda = "TITULO"
    else:
        print("OPCIÓN NO VÁLIDA.")
        return

    conn = sqlite3.connect('stock_libros.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT * FROM REGISTROS WHERE {campo_busqueda} = ?
    ''', (referencia,))
    registro = cursor.fetchone()

    if registro:
        id_registro = registro[0]
        print(f"ID: {registro[0]}, AUTOR: {registro[1]}, TÍTULO: {registro[2]}, STOCK: {registro[3]}, PRECIO: {registro[4]}")
        
        nuevo_autor = input("INGRESE EL NUEVO AUTOR (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[1]
        nuevo_titulo = input("INGRESE EL NUEVO TÍTULO (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[2]
        nuevo_stock = input("INGRESE EL NUEVO STOCK (DEJAR EN BLANCO PARA NO MODIFICAR): ")
        nuevo_stock = int(nuevo_stock) if nuevo_stock else registro[3]
        nuevo_precio = input("INGRESE EL NUEVO PRECIO (DEJAR EN BLANCO PARA NO MODIFICAR): ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else registro[4]

        print(f"SE MODIFICARÁN LOS DATOS: AUTOR: {nuevo_autor}, TÍTULO: {nuevo_titulo}, STOCK: {nuevo_stock}, PRECIO: {nuevo_precio}")
        confirmar = input("¿DESEA GUARDAR LOS CAMBIOS? (S/N): ").upper()

        if confirmar == 'S':
            cursor.execute('''
                UPDATE REGISTROS SET AUTOR = ?, TITULO = ?, STOCK = ?, PRECIO = ?
                WHERE ID = ?
            ''', (nuevo_autor, nuevo_titulo, nuevo_stock, nuevo_precio, id_registro))
            conn.commit()
            print("REGISTRO MODIFICADO.")
    else:
        print("REGISTRO NO ENCONTRADO.")
    
    conn.close()

# Función para eliminar un registro
def eliminar_registro():
    id_eliminar = input("INGRESE EL ID DEL REGISTRO A ELIMINAR: ")

    conn = sqlite3.connect('stock_libros.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM REGISTROS WHERE ID = ?
    ''', (id_eliminar,))
    registro = cursor.fetchone()

    if registro:
        print(f"ID: {registro[0]}, AUTOR: {registro[1]}, TÍTULO: {registro[2]}, STOCK: {registro[3]}, PRECIO: {registro[4]}")
        confirmar = input("¿DESEA ELIMINAR ESTE REGISTRO? (S/N): ").upper()

        if confirmar == 'S':
            confirmar_dos = input("¿ESTÁ SEGURO QUE DESEA ELIMINAR ESTE REGISTRO? ESTA ACCIÓN NO SE PUEDE DESHACER (S/N): ").upper()
            if confirmar_dos == 'S':
                cursor.execute('''
                    DELETE FROM REGISTROS WHERE ID = ?
                ''', (id_eliminar,))
                conn.commit()
                print("REGISTRO ELIMINADO.")
    else:
        print("REGISTRO NO ENCONTRADO.")
    
    conn.close()

# Función para listar registros
def listar_registros():
    print("OPCIONES DE LISTADO: 1. TODOS LOS REGISTROS 2. STOCK MÍNIMO")
   # opcion = int(input("SELECCIONE