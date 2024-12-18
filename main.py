import os
import sqlite3

conexion = sqlite3.connect('stock_libros.db')
cursor = conexion.cursor()
'''
def get_connection():
    return sqlite3.connect('stock_libros.db')

def crear_tabla_libros():'''
query = """ CREATE TABLE libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                autor TEXT NOT NULL,
                titulo TEXT NOT NULL,
                editorial TEXT NOT NULL,
                edicion integer NOT NULL,
                isbn INTEGER NOT NULL,
                stock INTEGER NOT NULL,
                precio  REAL NOT NULL)"""

try:
    conexion.execute(query)
    print("se creó la tabla artículos")
except sqlite3.OperationalError:
    print("La tabla artículos ya existe")
    
conexion.close()



        
def insertar(autor, titulo, editorial, edicion, isbn, stock, precio):
    query = """INSERT INTO libros(autor, titulo, editorial, edicion, isbn, stock, precio) VALUES (?,?,?,?,?,?,?)"""
    cursor.execute(query, (autor, titulo, editorial, edicion, isbn, stock, precio))   
    conexion.commit()
    print("Registros añadidos")
    
def cargar_datos():
    autor = input("AUTOR: ")
    titulo = input("TITULO: ")
    editorial = input("EDITORIAL: ")
    edicion = int(input("EDICIÓN: "))
    isbn = int(input("ISBN: "))
    stock = int(input("STOCK: "))
    precio = float(input("PRECIO: "))
    #mostrar los datos ingresaados
    insertar(autor, titulo, editorial, edicion, isbn, stock, precio)






def funcion_1():
    cargar_datos()
    print("Ejecutando Función 1")

def funcion_2():
    print("Ejecutando Función 2")

def funcion_3():
    print("Ejecutando Función 4")

def funcion_4():
    print("Ejecutando Función 4")

def funcion_5():
    print("Ejecutando Función 5")

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. carga de registros")
    print("2. modificación de registros")
    print("3. consultar registros")
    print("4. eliminar registr")
    print("5. listado bajo stock")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == '1':
            funcion_1()
        elif opcion == '2':
            funcion_2()
        elif opcion == '3':
            funcion_3()
        elif opcion == '4':
            funcion_4()
        elif opcion == '5':
            funcion_5()
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

