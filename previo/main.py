# Inventario de libros
import os

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

def obtener_id_libro():
    # Obtiene el próximo ID secuencial desde el archivo
    if os.path.exists("./base_de_datos.txt"):
        with open("./base_de_datos.txt", "r") as file:
            lineas = file.readlines()
        return len(lineas) + 1  # ID secuencial
    return 1

def guardar_libro(libro):
    # Guarda el libro en el archivo base_de_datos.txt
    with open("./base_de_datos.txt", "a") as file:
        file.write(f"{libro['id']},{libro['titulo']},{libro['autor']},{libro['anio']},{libro['editorial']},{libro['isbn']},{libro['unidades']},{libro['precio']}\n")

def listar_libros():
    # Lista todos los libros almacenados en base_de_datos.txt
    if os.path.exists("./base_de_datos.txt"):
        with open("./base_de_datos.txt", "r") as file:
            lineas = file.readlines()
        print(150*"-")
        print("|                                                                  LISTADO DE LIBROS                                                                 |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
        print("| ID  | TÍTULO                                     | AUTOR                      | AÑO  | EDITORIAL                 | ISBN          | STOCK | PRECIO  |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
        for linea in lineas:
            datos = linea.strip().split(",")
            print(f"| {datos[0]:<3} | {datos[1]:<42} | {datos[2]:<26} | {datos[3]:<4} | {datos[4]:<25} | {datos[5]:<13} |   {datos[6]:<3} | ${datos[7]:<6} |")
        print("+-----+--------------------------------------------+----------------------------+------+---------------------------+---------------+-------+---------+")
    else:
        print("NO HAY LIBROS REGISTRADOS")

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
