# Inventario de libros
import os
import sqlite3

def crear_conexion():
    # Crear la carpeta "bases" si no existe
    if not os.path.exists("bases"):
        os.makedirs("bases")
    
    # Crear una conexión a la base de datos SQLite
    conexion = sqlite3.connect("./bases/base_main.db")
    cursor = conexion.cursor()
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
            unidades INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()
# Menú de opciones:
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
    
def obtener_siguiente_id():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT MAX(id) FROM libros')
    ultimo_id = cursor.fetchone()[0]
    conexion.close()
    if ultimo_id:
        return ultimo_id + 1
    return 1

def registrar_libro():
    while True:
        mostrar_submenu_registrar()
        siguiente_id = obtener_siguiente_id()
        print(f"ID DEL NUEVO LIBRO: {siguiente_id}")
        titulo = input("TÍTULO: ").upper()
        autor = input("AUTOR: ").upper()
        anio = input("AÑO DE EDICIÓN: ").upper()
        editorial = input("EDITORIAL: ").upper()
        isbn = validar_isbn()
        unidades = input("CANTIDAD DE UNIDADES: ").upper()
        precio = input("PRECIO VENTA: ").upper()

        print("\nDATOS INGRESADOS:")
        print(f"ID: {siguiente_id}")
        print(f"TÍTULO: {titulo}")
        print(f"AUTOR: {autor}")
        print(f"AÑO: {anio}")
        print(f"EDITORIAL: {editorial}")
        print(f"ISBN: {isbn}")
        print(f"UNIDADES: {unidades}")
        print(f"PRECIO: {precio}")

        confirmar_guardar = input("¿DESEA GUARDAR ESTE LIBRO? (S/N): ").upper()
        if confirmar_guardar == 'S':
            conexion = crear_conexion()
            cursor = conexion.cursor()
            cursor.execute('''
                INSERT INTO libros (id, titulo, autor, anio, editorial, isbn, unidades, precio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (siguiente_id, titulo, autor, anio, editorial, isbn, unidades, precio))
            conexion.commit()
            conexion.close()
            print("LIBRO REGISTRADO EXITOSAMENTE")
            continuar = input("¿DESEA REGISTRAR OTRO LIBRO? (S/N): ").upper()
            if continuar == 'N':
                break
        else:
            confirmar_salir = input("¿DESEA SALIR DE LA CARGA DE DATOS? (S/N): ").upper()
            if confirmar_salir == 'S':
                break

def registrar_libro():
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

    if not libros:
        print(150*"-")
        print("|                                                          NO HAY LIBROS REGISTRADOS                                                                 |")
        print(150*"-")
    else:
        print(150*"-")
        print("|                                                                  LISTADO DE LIBROS                                                                 |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
        print("| ID  | TÍTULO                                     | AUTOR                      | AÑO  | EDITORIAL                 | ISBN          | STOCK | PRECIO  |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
        for libro in libros:
            print(f"| {str(libro[0]).upper():<3} | {libro[1][:42].upper():<42} | {libro[2][:26].upper():<26} | {libro[3][:4].upper():<4} | {libro[4][:25].upper():<25} | {libro[5][:13].upper():<13} |   {str(libro[6]).upper():<3} | ${str(libro[7]).upper():<6} |")
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

    if os.path.exists("./base_de_datos.txt"):
        with open("./base_de_datos.txt", "r") as file:
            lineas = file.readlines()

        libros_encontrados = []
        for linea in lineas:
            datos = linea.strip().split(",")
            if criterio == '1' and datos[0] == valor_busqueda:
                libros_encontrados.append(datos)
            elif criterio == '2' and datos[4].upper() == valor_busqueda:
                libros_encontrados.append(datos)
            elif criterio == '3' and datos[1].upper() == valor_busqueda:
                libros_encontrados.append(datos)
            elif criterio == '4' and datos[2].upper() == valor_busqueda:
                libros_encontrados.append(datos)

        if libros_encontrados:
            print(150*"-")
            print("|                                                      RESULTADOS DE LA BÚSQUEDA                                                                     |")
            print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
            print("| ID  | TÍTULO                                     | AUTOR                      | AÑO  | EDITORIAL                 | ISBN          | STOCK | PRECIO  |")
            print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
            for datos in libros_encontrados:
                print(f"| {datos[0]:<3} | {datos[1]:<42} | {datos[2]:<26} | {datos[3]:<4} | {datos[4]:<25} | {datos[5]:<13} |   {datos[6]:<3} | ${datos[7]:<6} |")
            print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
        else:
            print("NO SE ENCONTRARON LIBROS QUE COINCIDAN CON EL CRITERIO DE BÚSQUEDA")
    else:
        print("NO HAY LIBROS REGISTRADOS")

    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

def modificar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                           SUBMENÚ : ACTUALIZAR LIBRO                                                                 |")
    print(150*"-")
    print("|                                                        SELECCIONE CRITERIO DE BÚSQUEDA:                                                            |")
    print(150*"-")
    print("|                                                      1 - ID                                                                                         |")
    print("|                                                      2 - ISBN                                                                                       |")
    print(150*"-")

    criterio = input("SELECCIONE UNA OPCIÓN: ")
    valor_busqueda = input("INGRESE EL VALOR DE BÚSQUEDA: ").upper()

    if os.path.exists("./base_de_datos.txt"):
        with open("./base_de_datos.txt", "r") as file:
            lineas = file.readlines()

        libro_a_modificar = None
        libros_restantes = []
        for linea in lineas:
            datos = linea.strip().split(",")
            if (criterio == '1' and datos[0] == valor_busqueda) or (criterio == '2' and datos[5] == valor_busqueda):
                libro_a_modificar = datos
            else:
                libros_restantes.append(linea)

        if libro_a_modificar:
            print(150*"-")
            print(f"LIBRO SELECCIONADO: ID {libro_a_modificar[0]}, TÍTULO: {libro_a_modificar[1]}, AUTOR: {libro_a_modificar[2]}, AÑO: {libro_a_modificar[3]}, EDITORIAL: {libro_a_modificar[4]}, ISBN: {libro_a_modificar[5]}, STOCK: {libro_a_modificar[6]}, PRECIO: {libro_a_modificar[7]}")
            print(150*"-")
            print()
            print("DEJE EL CAMPO VACÍO SI NO DESEA MODIFICARLO")
            print()
            nuevo_titulo = input("NUEVO TÍTULO: ").upper() or libro_a_modificar[1]
            nuevo_autor = input("NUEVO AUTOR: ").upper() or libro_a_modificar[2]
            nuevo_anio = input("NUEVO AÑO DE EDICIÓN: ").upper() or libro_a_modificar[3]
            nueva_editorial = input("NUEVA EDITORIAL: ").upper() or libro_a_modificar[4]
            nuevo_isbn = input("NUEVO NÚMERO ISBN: ").upper() or libro_a_modificar[5]
            nuevas_unidades = input("NUEVA CANTIDAD DE UNIDADES: ").upper() or libro_a_modificar[6]
            nuevo_precio = input("NUEVO PRECIO VENTA: ").upper() or libro_a_modificar[7]

            nuevo_libro = [libro_a_modificar[0], nuevo_titulo, nuevo_autor, nuevo_anio, nueva_editorial, nuevo_isbn, nuevas_unidades, nuevo_precio]

            print(150*"-")
            print("REGISTRO ORIGINAL")
            print(150*"-")
            print(f"ID {libro_a_modificar[0]}, TÍTULO: {libro_a_modificar[1]}, AUTOR: {libro_a_modificar[2]}, AÑO: {libro_a_modificar[3]}, EDITORIAL: {libro_a_modificar[4]}, ISBN: {libro_a_modificar[5]}, STOCK: {libro_a_modificar[6]}, PRECIO: {libro_a_modificar[7]}")
            print(150*"-")
            print("DESPUÉS DE LA MODIFICACIÓN:")
            print(f"ID {nuevo_libro[0]}, TÍTULO: {nuevo_libro[1]}, AUTOR: {nuevo_libro[2]}, AÑO: {nuevo_libro[3]}, EDITORIAL: {nuevo_libro[4]}, ISBN: {nuevo_libro[5]}, STOCK: {nuevo_libro[6]}, PRECIO: {nuevo_libro[7]}")
            print(150*"-")

            confirmar1 = input("¿CONFIRMA LA MODIFICACIÓN DEL LIBRO? (S/N): ")
            if confirmar1.upper() == 'S':
                confirmar2 = input("¿REALMENTE ESTÁ SEGURO? ESTA ACCIÓN NO SE PUEDE DESHACER. (S/N): ")
                if confirmar2.upper() == 'S':
                    with open("./base_de_datos.txt", "w") as file:
                        for linea in libros_restantes:
                            file.write(linea)
                        file.write(",".join(nuevo_libro) + "\n")
                    print("LIBRO MODIFICADO EXITOSAMENTE")
                else:
                    print("MODIFICACIÓN CANCELADA")
            else:
                print("MODIFICACIÓN CANCELADA")
        else:
            print("NO SE ENCONTRÓ NINGÚN LIBRO CON EL CRITERIO PROPORCIONADO")
    else:
        print("NO HAY LIBROS REGISTRADOS")

    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")


def eliminar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                           SUBMENÚ : ELIMINAR LIBRO                                                                 |")
    print(150*"-")

    id_libro = input("INGRESE EL ID DEL LIBRO A ELIMINAR: ")

    if os.path.exists("./base_de_datos.txt"):
        with open("./base_de_datos.txt", "r") as file:
            lineas = file.readlines()

        libros_restantes = []
        libro_a_eliminar = None
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0] == id_libro:
                libro_a_eliminar = datos
            else:
                libros_restantes.append(linea)
        if libro_a_eliminar:
            print(150*"=")
            print(f" LIBRO SELECCIONADO: ID {libro_a_eliminar[0]},  TÍTULO: {libro_a_eliminar[1]}, AUTOR:  {libro_a_eliminar[2]}")
            print(150*"=")
            print()
            confirmar1 = input("¿ESTÁ SEGURO QUE DESEA ELIMINAR ESTE LIBRO? (S/N): ")
            if confirmar1.upper() == 'S':
                print()
                confirmar2 = input("¿REALMENTE ESTÁ SEGURO? ESTA ACCIÓN NO SE PUEDE DESHACER. (S/N): ")
                if confirmar2.upper() == 'S':
                    print()
                    with open("./base_de_datos.txt", "w") as file:
                        for linea in libros_restantes:
                            file.write(linea)
                    print("LIBRO ELIMINADO EXITOSAMENTE")
                else:
                    print("ELIMINACIÓN CANCELADA")
            else:
                print("ELIMINACIÓN CANCELADA")
        else:
            print("NO SE ENCONTRÓ NINGÚN LIBRO CON EL ID PROPORCIONADO")
    else:
        print("NO HAY LIBROS REGISTRADOS")

    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

def main():
    while True:
        mostrar_menu()
        opcion = input("SELECCIONE UNA OPCIÓN: ")
        if opcion == '1':
            while True:
                mostrar_submenu_registrar()
                titulo = input("TÍTULO: ").upper()
                autor = input("AUTOR: ").upper()
                anio = input("AÑO DE EDICIÓN: ").upper()
                editorial = input("EDITORIAL: ").upper()
                isbn = input("NÚMERO ISBN: ").upper()
                unidades = input("CANTIDAD DE UNIDADES: ").upper()
                precio = input("PRECIO VENTA: ").upper()
                id_libro = obtener_id_libro()
                print(f"NÚMERO DE REGISTRO: {id_libro}")
                confirmar = input("¿CONFIRMA EL REGISTRO DEL LIBRO? (S/N): ")
                if confirmar.upper() == 'S':
                    libro = {
                        "id": id_libro,
                        "titulo": titulo,
                        "autor": autor,
                        "anio": anio,
                        "editorial": editorial,
                        "isbn": isbn,
                        "unidades": unidades,
                        "precio": precio
                    }
                    guardar_libro(libro)
                    print("LIBRO REGISTRADO EXITOSAMENTE")
                else:
                    print("REGISTRO DE LIBRO CANCELADO")
                otro = input("¿DESEA REGISTRAR OTRO LIBRO? (S/N): ")
                if otro.upper() != 'S':
                    break
        elif opcion == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            modificar_libro()
            # actualizar un registro.
        elif opcion == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            eliminar_libro()
            # eliminar un registro.
        elif opcion == '4':
            buscar_libro()
        elif opcion == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            listar_libros()
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
        elif opcion == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("REPORTE DE LIBROS CON BAJO STOCK")
            # reportes de libros con bajo stock
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
            break
        else:
            print("OPCIÓN NO VÁLIDA")
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

if __name__ == "__main__":
    main()
