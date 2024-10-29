#Inventario de libros
import os

#Menú de opciones:
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

#Encabezado del menú de carga
def mostrar_submenu_registrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(150*"-")
    print("|                                                           SUBMENÚ : REGISTRO DE LIBRO                                                              |")
    print(150*"-")
    print("|                                                        INGRESE LOS DATOS DEL NUEVO REGISTRO:                                                       |")
    print(150*"-")
    print()

def obtener_id_libro():
    #Obtiene el próximo ID secuencial desde el archivo
    if os.path.exists("./base_de_datos.txt"):
        with open("./base_de_datos.txt", "r") as file:
            lineas = file.readlines()
            return len(lineas) + 1  # ID secuencial
    return 1

def guardar_libro(libro):
    #Guarda el libro en el archivo base_de_datos.txt
    with open("./base_de_datos.txt", "a") as file:
        file.write(f"{libro['id']},{libro['titulo']},{libro['autor']},{libro['anio']},{libro['editorial']},{libro['isbn']},{libro['unidades']},{libro['precio']}\n")

def listar_libros():
    #Lista todos los libros almacenados en base_de_datos.txt
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
        
def main():
    while True:
        mostrar_menu()
        opcion = input("SELECCIONE UNA OPCIÓN: ")
        if opcion == '1':
            while True:
                mostrar_submenu_registrar()
                titulo = input("TÍTULO: ")
                autor = input("AUTOR: ")
                anio = input("AÑO DE EDICIÓN: ")
                editorial = input("EDITORIAL: ")
                isbn = input("NÚMERO ISBN: ")
                unidades = input("CANTIDAD DE UNIDADES: ")
                precio = input("PRECIO VENTA: ")
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
            print("ACTUALIZAR LIBRO SELECCIONADO")
            # actualizar un registro.
        elif opcion == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("EELIMINAR LIBRO SELECCIONADO")
            # eliminar un registro.
        elif opcion == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("BUSCAR LIBRO SELECCIONADO")
            # buscar un registro.
        elif opcion == '5':
            os.system('cls' if os.name == 'nt' else 'clear') 
            listar_libros()
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
        elif opcion == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("RREPORTE DE LIBROS CON BAJO STOCK")
            # reportes de libros con bajo stock
        elif opcion == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("SALIENDO DEL PROGRAMA...")
            print()
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
            break
        else:
            print("OPCIÓN NO VÁLIDA")
            input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")

if __name__ == "__main__":
    main()
