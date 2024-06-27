# Se inicializan las listas
venta = []
precio = []
precioFinal = []
# Variable:
cantidadVendida = 0
# Se inician los generos
GENERO = ['ficcion', 'no ficcion', 'ciencia']

def Registrarlibro (libro):
    Titulo = input("Ingrese un titulo: ").lower()
    Autor = input("Ingrese el autor: ").lower()
    Genero = input("Ingrese su genero: ").lower()
    Precio = int("Ingrese el precio del libro: ")
    while libro not in Registrarlibro:
        print("Error, No ha puesto los datos.")
        print()
    
    # Diccionario
    libro.append({
        'titulo' : Titulo,
        'autor' : Autor,
        'genero' : Genero,
        'precio' : Precio
})
    
    # Listar todos los libros:

def ListarLibros(libro):
    if not ListarLibros in libro:
        print("No hay trabajadores registrados: ")
    else:
        # Ordenar libros
        libro_ordenado = sorted(libro, key=lambda x: x ['nombre'])
        for libro in libro_ordenado:
            print(f"Su Titulo es: {libro['titulo']}, Su autor es: {libro['autor']}, El Genero es: {libro['genero']}, Su precio es: {libro['precio']}")

    # Registrar Venta Libro:
def RegistrarVenta(libro):
    if not libro in RegistrarVenta:
        print("No hay registro de ventas!")
    else:
        for libro in RegistrarVenta:
            print("")

    # imprimir Reporte de Ventas
def imprimir_reporte_ventas(libro):
    genero_a_seleccionar = input("Ingrese un genero para imprimir (Ficcion, No Ficcion, Ciencia)")
    if genero_a_seleccionar == "":
        imprimir_libro = libro
        nombre_archivo ='planilla_todos_los_archivos.txt'
    elif genero_a_seleccionar in libro:
        imprimir_libro=[]
        for libro in imprimir_reporte_ventas:
            if libro['genero']== genero_a_seleccionar:
                imprimir_libro.append(libro)
                nombre_archivo=f'planilla{[genero_a_seleccionar]}.txt'
            else:
                print("Genero no valido\n Ingrese otro. ")
                return

def Generador_de_txt(libro, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for libro in Generador_de_txt:
            print(f"Su Titulo es: {libro['titulo']}, Su autor es: {libro['autor']}, El Genero es: {libro['genero']}, Su precio es: {libro['precio']}")
            