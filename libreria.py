# 1. Lista de libros (cada libro es un diccionario)
libros = [
    {"titulo": "1984", "autor": "George Orwell", "precio": 12000, "stock": 5},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "precio": 15000, "stock": 2},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "precio": 8000, "stock": 10},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "precio": 11000, "stock": 0},
    {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "precio": 9500, "stock": 3}
]

# 6. Descuentos especiales por autor
descuentos_por_autor = {
    "Gabriel García Márquez": 0.10,  # 10% de descuento
    "Jane Austen": 0.15              # 15% de descuento
}

# Variables globales para la factura
total_pagado = 0
total_ahorro = 0
total_libros_comprados = 0

# 2. Mostrar libros disponibles (stock > 1)
def mostrar_libros_disponibles():
    print("\nLibros disponibles (más de 1 unidad):")
    for libro in libros:
        if libro["stock"] > 1:
            print(f"- {libro['titulo']} por {libro['autor']} (${libro['precio']}) - Stock: {libro['stock']}")

# 3. Filtrar libros por rango de precios
def filtrar_por_precio():
    try:
        minimo = float(input("\nIngrese el precio mínimo: "))
        maximo = float(input("Ingrese el precio máximo: "))
    except ValueError:
        print("⚠️ Ingrese un valor numérico válido.")
        return

    print(f"\nLibros entre ${minimo} y ${maximo}:")
    encontrados = False
    for libro in libros:
        if minimo <= libro["precio"] <= maximo:
            print(f"- {libro['titulo']} (${libro['precio']})")
            encontrados = True
    if not encontrados:
        print("No se encontraron libros en ese rango de precios.")

# 4 y 6. Función para comprar libros
def comprar_libros(titulo, cantidad):
    global total_pagado, total_ahorro, total_libros_comprados

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["stock"] >= cantidad:
                subtotal = libro["precio"] * cantidad
                descuento = descuentos_por_autor.get(libro["autor"], 0)
                ahorro = subtotal * descuento
                total = subtotal - ahorro

                # Actualizar stock y acumuladores
                libro["stock"] -= cantidad
                total_pagado += total
                total_ahorro += ahorro
                total_libros_comprados += cantidad

                print(f"\n✅ Compra exitosa: {cantidad}x '{libro['titulo']}'")
                print(f"Subtotal: ${subtotal:.0f}")
                print(f"Descuento: ${ahorro:.0f}")
                print(f"Total a pagar: ${total:.0f}")
                return
            else:
                print("❌ No hay suficiente stock para esa cantidad.")
                return
    print("❌ Libro no encontrado en el inventario.")

# 5. Bucle principal de compras
def menu_principal():
    while True:
        print("\n--- LIBROS & BYTES ---")
        print("1. Ver libros disponibles")
        print("2. Filtrar por precio")
        print("3. Comprar libro")
        print("4. Finalizar compra y ver factura")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_libros_disponibles()
        elif opcion == "2":
            filtrar_por_precio()
        elif opcion == "3":
            titulo = input("Ingrese el título del libro: ")
            try:
                cantidad = int(input("Ingrese la cantidad a comprar: "))
            except ValueError:
                print("⚠️ La cantidad debe ser un número entero.")
                continue
            comprar_libros(titulo, cantidad)
        elif opcion == "4":
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

# 7. Mostrar factura
def mostrar_factura():
    print("\n🧾 FACTURA FINAL")
    print(f"Libros comprados: {total_libros_comprados}")
    print(f"Monto total pagado: ${total_pagado:.0f}")
    print(f"Ahorro total por descuentos: ${total_ahorro:.0f}")
    print("¡Gracias por su compra!")

# Ejecutar el programa
menu_principal()
mostrar_factura()
