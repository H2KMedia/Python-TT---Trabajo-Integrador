import os
import sqlite3

# Función para crear la base de datos y la tabla si no existen
def inicializar_bd():
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            articulo TEXT NOT NULL,
            descripcion TEXT,
            rubro TEXT,
            stock INTEGER,
            precio REAL
        )
    ''')
    conn.commit()
    conn.close()
    
# Menú de opciones
def mostrar_menu():
    #os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                       MENÚ DE OPCIONES PRODUCCION TEXTIL                                                        |")
    print(150*"-")
    print("|                                                                                                                                                    |")
    print("|                                                             1 - REGISTRAR ARTICULOS                                                                    |")
    print("|                                                             2 - ACTUALIZAR ARTÍCULO                                                                   |")
    print("|                                                             3 - ELIMINAR ARTÍCULO                                                                     |")
    print("|                                                             4 - BUSCAR ARTICULO                                                                       |")
    print("|                                                             5 - LISTADOS                                                                      |")
    print("|                                                             0 - SALIR DE SISTEMA                                                                   |")
    print("|                                                                                                                                                    |")
    print(150*"-")
    
# Función para agregar un nuevo registro
def agregar_registro():
    #os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        articulo = input("INGRESE EL ARTÏCULO: ")
        descripcion = input("INGRESE UNA DESCRIPCIÖN DEL ARTICULO: ")
        rubro = input("INGRESE EL RUBRO: ")
        stock = int(input("INGRESE EL STOCK: "))
        precio = float(input("INGRESE EL PRECIO: "))

        confirmar = input("¿DESEA GUARDAR EL REGISTRO? (S/N): ")
        if confirmar.upper() == 'S':
            conn = sqlite3.connect('stock.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO registros (articulo, descripcion, rubro, stock, precio)
                VALUES (?, ?, ?, ?, ?)
            ''', (articulo, descripcion, rubro, stock, precio))
            conn.commit()
            conn.close()
            print("REGISTRO GUARDADO CORRECTAMENTE")

        otro = input("¿DESEA CARGAR OTRO REGISTRO? (S/N): ")
        if otro.upper() != 'S':
            break

# Función para modificar un registro
def modificar_registro():
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("OPCIONES DE BÚSQUEDA: ")
    print(" 1. ID")
    print(" 2. ARTÍCULO ")
    print(" 3. RUBRO")
    opcion = int(input("SELECCIONE UNA OPCIÓN: "))

    if opcion == '1':
        referencia = input("INGRESE EL ID: ")
        campo_busqueda = "id"
    elif opcion == '2':
        referencia = input("INRESE EL ARTÍCULO: ")
        campo_busqueda = "articulo"
    elif opcion == '3':
        referencia = input("INGRESE EL RUBRO: ")
        campo_busqueda = "rubro"
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
        print(f"ID: {registro[0]}, ARTÍCULO: {registro[1]}, DESCRIPCIÓN: {registro[2]}, RUBRO: {registro[3]}, STOCK: {registro[4]}, PRECIO: {registro[5]}")
        
        nuevo_articulo = input("INGRESE EL NUEVO ARTÍCULO (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[1]
        nuevo_descripcion = input("INGRESE LA NUEVA DESCRIPCIÓN DEL ART. (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[2]
        nuevo_rubro = input("INGRESE EL NUEVO RUBROL (DEJAR EN BLANCO PARA NO MODIFICAR): ").upper() or registro[3]
        nuevo_stock = input("INGRESE EL NUEVO STOCK (DEJAR EN BLANCO PARA NO MODIFICAR): ")
        nuevo_stock = int(nuevo_stock) if nuevo_stock else registro[4]
        nuevo_precio = input("INGRESE EL NUEVO PRECIO (DEJAR EN BLANCO PARA NO MODIFICAR: ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else registro[5]

        print(f"SE MODIFICARÁN LOS DATOS: ARTÍCULO: {nuevo_articulo}, DESCRIPCIÓN: {nuevo_descripcion}, RUBRO: {nuevo_rubro}, STOCK: {nuevo_stock}, PRECIO: {nuevo_precio}")
        confirmar = input("¿DESEA GUARDAR LOS CAMBIOS? (S/N): ")

        if confirmar.upper() == 'S':
            cursor.execute('''
                UPDATE registros SET articulo = ?, descripcion = ?, rubro = ?, stock = ?, precio = ?
                WHERE id = ?
            ''', (nuevo_articulo, nuevo_descripcion, nuevo_rubro, nuevo_stock, nuevo_precio, id_registro))
            conn.commit()
            print("REGISTRO MODIFICADO.")
    else:
        print("REGISTRO NO ENCONTRADO.")
    
    conn.close()

# Función para eliminar un registro
def eliminar_registro():
    #os.system('cls' if os.name == 'nt' else 'clear')
    id_eliminar = input("INGRESE EL ID DEL REGISTRO A ELIMINAR: ")

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM registros WHERE id = ?
    ''', (id_eliminar,))
    registro = cursor.fetchone()

    if registro:
        print(f"ID: {registro[0]}, ARTÍCULO: {registro[1]}, DESCRIPCIÓN: {registro[2]}, RUBRO: {registro[3]}, STOCK: {registro[4]}, PRECIO: {registro[5]}")
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
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("OPCIONES DE LISTADO: ")
    print(" 1. TODOS LOS REGISTROS ")
    print(" 2. REPORTE DE STOCK MÍNIMO")
    opcion = int(input("SELECCIONE UNA OPCIÓN: "))

    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()
    
    if opcion == 1:
        #  os.system('cls' if os.name == 'nt' else 'clear')
        cursor.execute('''
            SELECT * FROM registros ORDER BY id
        ''')
    elif opcion == 2:
        #os.system('cls' if os.name == 'nt' else 'clear')
        stock_limite = int(input("INGRESE LA CANTIDAD LÍMITE DE STOCK: "))
        cursor.execute('''
            SELECT * FROM registros WHERE stock <= ? ORDER BY id
        ''', (stock_limite,))
    else:
        print("OPCIÓN NO VÁLIDA.")
        input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
        #os.system('cls' if os.name == 'nt' else 'clear')
        conn.close()
        return
    
    registros = cursor.fetchall()
    for registro in registros:
        print(f"ID: {registro[0]}, ARTÍCULO: {registro[1]}, DESCRIPCIÓN: {registro[2]}, RUBRO: {registro[3]}, STOCK: {registro[4]}, PRECIO: {registro[5]}")
    conn.close()

# Función principal del menú
def menu():
    while True:
        mostrar_menu()
        opcion = input("SELECCIONE UNA OPCIÓN: ")
        if opcion == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            agregar_registro()
        elif opcion == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            modificar_registro()
        elif opcion == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            eliminar_registro()
        elif opcion == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            listar_registros()
        elif opcion == '0':
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
            print()
            break
        else:
            print("OPCIÓN NO VÁLIDA")
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

# Ejecución del programa
if __name__ == '__main__':
    inicializar_bd()
    menu()
