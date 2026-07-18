from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def registrar_producto(servicio: Restaurante) -> None:
    print("\n-- Registrar Producto --")
    try:
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = float(input("Precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
    except ValueError as error:
        print(f"Error: {error}")
        return
    if servicio.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print(f"Ya existe un producto con el codigo '{producto.codigo}'.")


def registrar_bebida(servicio: Restaurante) -> None:
    print("\n-- Registrar Bebida --")
    try:
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = float(input("Precio: "))
        tamano = input("Tamano (ej. 500ml, grande): ")
        tipo_envase = input("Tipo de envase (ej. botella, vaso, lata): ")
        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
    except ValueError as error:
        print(f"Error: {error}")
        return
    if servicio.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
    else:
        print(f"Ya existe un producto con el codigo '{bebida.codigo}'.")


def registrar_cliente(servicio: Restaurante) -> None:
    print("\n-- Registrar Cliente --")
    try:
        identificacion = input("Identificacion: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        cliente = Cliente(identificacion, nombre, correo)
    except ValueError as error:
        print(f"Error: {error}")
        return
    if servicio.registrar_cliente(cliente):
        print("Cliente registrado correctamente.")
    else:
        print(f"Ya existe un cliente con la identificacion '{cliente.identificacion}'.")


def listar_productos(servicio: Restaurante) -> None:
    print("\n-- Lista de Productos --")
    registros = servicio.listar_productos()
    if not registros:
        print("No hay productos registrados.")
        return
    for registro in registros:
        print(registro)


def listar_clientes(servicio: Restaurante) -> None:
    print("\n-- Lista de Clientes --")
    registros = servicio.listar_clientes()
    if not registros:
        print("No hay clientes registrados.")
        return
    for registro in registros:
        print(registro)


def main() -> None:
    servicio = Restaurante()
    opciones = {
        "1": registrar_producto,
        "2": registrar_bebida,
        "3": registrar_cliente,
        "4": listar_productos,
        "5": listar_clientes,
    }
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ").strip()
        if opcion == "6":
            print("\nHasta luego.")
            break
        accion = opciones.get(opcion)
        if accion:
            accion(servicio)
        else:
            print("Opcion no valida. Intente de nuevo.")


if __name__ == "__main__":
    main()
