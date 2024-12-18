import sqlite3

# Conexión a la base de datos (la crea si no existe)
conn = sqlite3.connect('stck.db')
c = conn.cursor()

# Creación de la tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                autor TEXT,
                titulo TEXT,
                stock INTEGER,
                precio REAL
            )''')

def alta():
    while True:
        autor = input("Ingrese autor: ")
        titulo = input("Ingrese título: ")
        stock = int(input("Ingrese stock: "))
        precio = float(input("Ingrese precio: "))
        confirmar = input(f"Confirmar alta de registro: {autor}, {titulo}, {stock}, {precio} (s/n): ")
        if confirmar.lower() == 's':
            c.execute("INSERT INTO registros (autor, titulo, stock, precio) VALUES (?, ?, ?, ?)",
                      (autor, titulo, stock, precio))
            conn.commit()
            print("Registro guardado exitosamente.")
        otro = input("¿Desea cargar otro registro? (s/n): ")
        if otro.lower() != 's':
            break

def modificar():
    criterio = input("Buscar registro por (id, autor, titulo): ")
    referencia = input(f"Ingrese {criterio} a buscar: ")
    if criterio == 'id':
        c.execute("SELECT * FROM registros WHERE id = ?", (referencia,))
    elif criterio == 'autor':
        c.execute("SELECT * FROM registros WHERE autor LIKE ?", ('%' + referencia + '%',))
    elif criterio == 'titulo':
        c.execute("SELECT * FROM registros WHERE titulo LIKE ?", ('%' + referencia + '%',))
    else:
        print("Criterio de búsqueda no válido.")
        return
    registros = c.fetchall()
    if not registros:
        print("No se encontraron registros.")
        return
    for registro in registros:
        print(f"ID: {registro[0]}, Autor: {registro[1]}, Título: {registro[2]}, Stock: {registro[3]}, Precio: {registro[4]}")
        nuevo_autor = input("Nuevo autor (deje en blanco para no modificar): ") or registro[1]
        nuevo_titulo = input("Nuevo título (deje en blanco para no modificar): ") or registro[2]
        nuevo_stock = input("Nuevo stock (deje en blanco para no modificar): ") or registro[3]
        nuevo_precio = input("Nuevo precio (deje en blanco para no modificar): ") or registro[4]
        confirmar = input(f"Confirmar modificación de registro: {nuevo_autor}, {nuevo_titulo}, {nuevo_stock}, {nuevo_precio} (s/n): ")
        if confirmar.lower() == 's':
            c.execute("UPDATE registros SET autor = ?, titulo = ?, stock = ?, precio = ? WHERE id = ?",
                      (nuevo_autor, nuevo_titulo, nuevo_stock, nuevo_precio, registro[0]))
            conn.commit()
            print("Registro modificado exitosamente.")

def eliminar():
    id_eliminar = input("Ingrese el ID del registro a eliminar: ")
    c.execute("DELETE FROM registros WHERE id = ?", (id_eliminar,))
    conn.commit()
    print("Registro eliminado exitosamente.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Alta")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            alta()
        elif opcion == '2':
            modificar()
        elif opcion == '3':
            eliminar()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
conn.close()
