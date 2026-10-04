import os

# ==============================================================================
# Pre-entrega: Sistema de Gestión Básica de Productos
# Curso: Iniciación a la Programación con Python 
# ==============================================================================

# Lista principal para almacenar los productos.
# Cada elemento será una sublista con el formato: [nombre, categoria, precio]
productos = []

# Bucle principal que mantiene en ejecución el programa hasta que el usuario decida salir
while True:
    print("\n" + "=" * 45)
    print("   SISTEMA DE GESTION BASICA DE PRODUCTOS")
    print("=" * 45)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("6. Limpiar pantalla")
    print("=" * 45)

    opcion = input("Seleccione una opcion (1-6): ").strip()

    # --------------------------------------------------------------------------
    # OPCION 1: AGREGAR PRODUCTO
    # --------------------------------------------------------------------------
    if opcion == "1":
        print("\n--- Agregar nuevo producto ---")
        
        # Validación de nombre (no vacío)
        while True:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if nombre != "":
                break
            print("Error: El nombre no puede estar vacio. Intente nuevamente.")

        # Validación de categoría (no vacía)
        while True:
            categoria = input("Ingrese la categoria del producto: ").strip()
            if categoria != "":
                break
            print("Error: La categoria no puede estar vacia. Intente nuevamente.")

        # Validación de precio (debe ser un número entero positivo)
        while True:
            precio_input = input("Ingrese el precio (entero, sin centavos): ").strip()
            if precio_input.isdigit() and int(precio_input) > 0:
                precio = int(precio_input)
                break
            print("Error: Ingrese un precio numerico entero valido mayor a 0.")

        # Se crea la sublista [nombre, categoria, precio] y se agrega a la lista principal
        nuevo_producto = [nombre, categoria, precio]
        productos.append(nuevo_producto)
        print(f"\n[OK] Producto '{nombre}' agregado exitosamente!")

    # --------------------------------------------------------------------------
    # OPCION 2: MOSTRAR PRODUCTOS
    # --------------------------------------------------------------------------
    elif opcion == "2":
        print("\n--- Lista de productos registrados ---")
        if len(productos) == 0:
            print("No hay productos registrados actualmente.")
        else:
            # Se recorre la lista con un bucle for mostrando cada producto numerado
            for i in range(len(productos)):
                prod = productos[i]
                print(f"{i + 1}. Nombre: {prod[0]} | Categoria: {prod[1]} | Precio: ${prod[2]}")

    # --------------------------------------------------------------------------
    # OPCION 3: BUSCAR PRODUCTO
    # --------------------------------------------------------------------------
    elif opcion == "3":
        print("\n--- Buscar producto ---")
        if len(productos) == 0:
            print("No hay productos registrados para buscar.")
        else:
            while True:
                termino_busqueda = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
                if termino_busqueda != "":
                    break
                print("Error: El termino de busqueda no puede estar vacio.")

            encontrados = 0
            print(f"\nResultados para '{termino_busqueda}':")
            # Recorremos la lista para buscar coincidencias (insensible a mayúsculas/minúsculas)
            for i in range(len(productos)):
                prod = productos[i]
                if termino_busqueda.lower() in prod[0].lower():
                    encontrados += 1
                    print(f"- Posicion [{i + 1}] -> Nombre: {prod[0]} | Categoria: {prod[1]} | Precio: ${prod[2]}")

            if encontrados == 0:
                print(f"No se encontraron resultados para '{termino_busqueda}'.")

    # --------------------------------------------------------------------------
    # OPCION 4: ELIMINAR PRODUCTO
    # --------------------------------------------------------------------------
    elif opcion == "4":
        print("\n--- Eliminar producto ---")
        if len(productos) == 0:
            print("No hay productos registrados para eliminar.")
        else:
            # Mostramos primero los productos disponibles para facilitar la selección
            print("Productos disponibles:")
            for i in range(len(productos)):
                prod = productos[i]
                print(f"  {i + 1}. {prod[0]} (${prod[2]})")

            posicion_input = input("\nIngrese el numero del producto a eliminar: ").strip()
            
            # Validamos que sea un número y que se encuentre dentro del rango válido
            if posicion_input.isdigit():
                posicion = int(posicion_input)
                if 1 <= posicion <= len(productos):                 
                    indice = posicion - 1
                    eliminado = productos.pop(indice)
                    print(f"\n[OK] El producto '{eliminado[0]}' (posicion {posicion}) ha sido eliminado con exito.")
                else:
                    
                    print(f"Error: La posicion {posicion} no existe. Ingrese un valor entre 1 y {len(productos)}.")
            else:
                print("Error: Debe ingresar un valor numerico valido.")

    # --------------------------------------------------------------------------
    # OPCION 5: SALIR
    # --------------------------------------------------------------------------
    elif opcion == "5":
        print("\nGracias por utilizar el Sistema de Gestion de Productos. Hasta pronto!\n")
        break

    # --------------------------------------------------------------------------
    # OPCION 6 (EXTRA): LIMPIAR PANTALLA
    # --------------------------------------------------------------------------
    elif opcion == "6":
        os.system("cls" if os.name == "nt" else "clear")

    # --------------------------------------------------------------------------
    # OPCION INVALIDA
    # --------------------------------------------------------------------------
    else:
        print("\n[!] Opcion no valida. Por favor, ingrese un numero del 1 al 6.")
