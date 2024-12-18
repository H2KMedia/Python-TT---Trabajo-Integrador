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
            editorial TEXT NOT NULL,
            edicion INTEGER NOT NULL,
            isbn INTEGER NOT NULL
            stock INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función para agregar un nuevo registro
def agregar_registro():
    while True:
        autor = input("Ingrese el autor: ")
        titulo = input("Ingrese el título: ")
        editorial = input("Ingrese la editorial: ")
        edicion = int(input("Ingrese la edición: "))
        isbn = int(input("Ingrese el codigo isbn: "))
        stock = int(input("Ingrese el stock: "))
        precio = float(input("Ingrese el precio: "))

        confirmar = input("¿Desea guardar el registro? (s/n): ")
        if confirmar.upper() == 's':
            conn = sqlite3.connect('stock.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO registros (autor, titulo, stock, precio)
                VALUES (?, ?, ?, ?)
            ''', (autor, titulo, stock, precio))
            conn.commit()
            conn.close()
            print("Registro guardado.")

        otro = input("¿Desea cargar otro registro? (s/n): ")
        if otro.upper() != 's':
            break

# Función para modificar un registro
def modificar_registro():
    print("Opciones de búsqueda: 1. ID 2. Autor 3. Título")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        referencia = input("Ingrese el ID: ")
        campo_busqueda = "id"
    elif opcion == 2:
        referencia = input("Ingrese el Autor: ")
        campo_busqueda = "autor"
    elif opcion == 3:
        referencia = input("Ingrese el Título: ")
        campo_busqueda = "titulo"
    else:
        print("Opción no válida.")
        return

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT * FROM registros WHERE {campo_busqueda} = ?
    ''', (referencia,))
    registro = cursor.fetchone()

    if registro:
        id_registro = registro[0]
        print(f"ID: {registro[0]}, Autor: {registro[1]}, Título: {registro[2]}, Stock: {registro[3]}, Precio: {registro[4]}")
        
        nuevo_autor = input("Ingrese el nuevo autor (dejar en blanco para no modificar): ") or registro[1]
        nuevo_titulo = input("Ingrese el nuevo título (dejar en blanco para no modificar): ") or registro[2]
        nuevo_stock = input("Ingrese el nuevo stock (dejar en blanco para no modificar): ")
        nuevo_stock = int(nuevo_stock) if nuevo_stock else registro[3]
        nuevo_precio = input("Ingrese el nuevo precio (dejar en blanco para no modificar): ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else registro[4]

        print(f"Se modificarán los datos: Autor: {nuevo_autor}, Título: {nuevo_titulo}, Stock: {nuevo_stock}, Precio: {nuevo_precio}")
        confirmar = input("¿Desea guardar los cambios? (s/n): ")

        if confirmar.upper() == 's':
            cursor.execute('''
                UPDATE registros SET autor = ?, titulo = ?, stock = ?, precio = ?
                WHERE id = ?
            ''', (nuevo_autor, nuevo_titulo, nuevo_stock, nuevo_precio, id_registro))
            conn.commit()
            print("Registro modificado.")
    else:
        print("Registro no encontrado.")
    
    conn.close()

# Función para eliminar un registro
def eliminar_registro():
    id_eliminar = input("Ingrese el ID del registro a eliminar: ")

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM registros WHERE id = ?
    ''', (id_eliminar,))
    registro = cursor.fetchone()

    if registro:
        print(f"ID: {registro[0]}, Autor: {registro[1]}, Título: {registro[2]}, Stock: {registro[3]}, Precio: {registro[4]}")
        confirmar = input("¿Desea eliminar este registro? (s/n): ")

        if confirmar.upper() == 's':
            confirmar_dos = input("¿Está seguro que desea eliminar este registro? Esta acción no se puede deshacer (s/n): ")
            if confirmar_dos.upper() == 's':
                cursor.execute('''
                    DELETE FROM registros WHERE id = ?
                ''', (id_eliminar,))
                conn.commit()
                print("Registro eliminado.")
    else:
        print("Registro no encontrado.")
    
    conn.close()

# Función para listar registros
def listar_registros():
    print("Opciones de listado: 1. Todos los registros 2. Stock mínimo")
    opcion = int(input("Seleccione una opción: "))

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    
    if opcion == 1:
        cursor.execute('''
            SELECT * FROM registros ORDER BY id
        ''')
    elif opcion == 2:
        stock_limite = int(input("Ingrese la cantidad límite de stock: "))
        cursor.execute('''
            SELECT * FROM registros WHERE stock <= ? ORDER BY id
        ''', (stock_limite,))
    else:
        print("Opción no válida.")
        conn.close()
        return
    
    registros = cursor.fetchall()
    for registro in registros:
        print(f"ID: {registro[0]}, Autor: {registro[1]}, Título: {registro[2]}, Stock: {registro[3]}, Precio: {registro[4]}")
    
    conn.close()

# Función principal del menú
def menu():
    while True:
        print("\nMenú:")
        print("1. Alta")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Listar")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_registro()
        elif opcion == 2:
            modificar_registro()
        elif opcion == 3:
            eliminar_registro()
        elif opcion == 4:
            listar_registros()
        elif opcion == 5:
            break
        else:
            print("Opción no válida.")

# Ejecución del programa
if __name__ == '__main__':
    inicializar_bd()
    menu()
