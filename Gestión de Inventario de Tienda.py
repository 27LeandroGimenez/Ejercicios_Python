import os

inventario = {
    'Camisas': {'nombre': 'Camiseta', 'precio': 20, 'cantidad': 100},
    'Zapatos': {'nombre': 'Zapatos', 'precio': 50, 'cantidad': 50},
    'Pantalones':{'nombre': 'Pantalones', 'precio': 30, 'cantidad': 25}
}

while True:

    print('1. Mostrar inventario actual.')
    print('2. Agregar un nuevo producto al inventario.')
    print('3. Actualizar precio producto.')
    print('4. Actualizar cantidad producto.')
    print('5. Realizar una venta.')
    print('6. Salir')

    print('\n')

    opcion = int(input('Ingrese opcion: '))

    if opcion == 1:
        os.system('cls')
        print('Inventario.')
        for producto, detalles in inventario.items():
            nombre = detalles['nombre']
            precio = detalles['precio']
            cantidad = detalles['cantidad']
            print(f'* {nombre} - Precio: {precio} - Cantidad: {cantidad}')

        print('\n')

    elif opcion == 2:
        os.system('cls')
        nombre = input('Nombre producto: ').capitalize()
        producto = input('Nombre: ').capitalize()
        precio = int(input('Precio: '))
        cantidad = int(input('Cantidad: '))
        inventario[nombre] = {'nombre':producto, 'precio':precio, 'cantidad':cantidad}

    elif opcion == 3:
        os.system('cls')
        producto = input('Nombre del producto al que quieres actualizar el precio: ').capitalize()
        precio_nuevo = int(input('Nuevo precio: '))
        inventario[producto]['precio'] = precio_nuevo
        print('El precio a sido actualizado correctamente.')

    elif opcion == 4:
        os.system('cls')
        producto = input('Nombre del producto al que quieres actualizar su cantidad: ').capitalize()
        cantidad = int(input('Ingrese cantidad: '))
        inventario[producto]['cantidad'] = cantidad
        print('Cantidad actualizada correctamente.')

    elif opcion == 5:
        os.system('cls')
        producto_a_vender = input('Nombre producto a vender: ').capitalize()
        while True:
            try:
                cantidad_a_vender = int(input('Cantidad: '))
                if cantidad_a_vender < 0:
                    print('La cantidad debe ser mayor que cero.')
                elif inventario[producto_a_vender]['cantidad'] >= cantidad_a_vender:
                    inventario[producto_a_vender]['cantidad'] -= cantidad_a_vender
                    costo_venta = cantidad_a_vender * inventario[producto_a_vender]['precio']
                    os.system('cls')
                    print(f'Resumen venta.\nProducto:{producto_a_vender}\nCantidad:{cantidad_a_vender}\nPrecio individual:{inventario[producto_a_vender]["precio"]}\nCosto total de venta: {costo_venta}')
                    break
                else:
                    print(f'No tienes productos suficientes. Cantidad {inventario[producto_a_vender]["cantidad"]}')
            except ValueError:
                print('Cantidad no válida. Ingresa un número entero válido.')

    elif opcion == 6:
        os.system('cls')
        print('Has abandonado el sistema, hasta la proxima.')
        break
    else:
        os.system('cls')
        print("*** Ingrese una opcion valida. ***\n")