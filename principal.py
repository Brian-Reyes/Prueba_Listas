import funciones as fn

libro = []

while True:
        print("(1) Registrar libro")
        print("(2) Listar Libro")
        print("(3) Registrar venta")
        print("(4) Imprimir reporte de ventas")
        print("(5) Generar archivo txt")
        print("(6) Salir")

        opcion=int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            fn.Registrarlibro(libro)
        elif opcion == 2:
            fn.ListarLibros(libro)
        elif opcion == 3:
            fn.RegistrarVenta(libro)
        elif opcion == 4:
            fn.imprimir_reporte_ventas(libro)
        elif opcion == 6:
            print("Saliendo del programa.")
            break