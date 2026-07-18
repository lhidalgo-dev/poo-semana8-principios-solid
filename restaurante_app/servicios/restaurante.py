from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self._existe_codigo_producto(producto.codigo):
            return False
        self._productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        if self._existe_identificacion_cliente(cliente.identificacion):
            return False
        self._clientes.append(cliente)
        return True

    def listar_productos(self) -> list[str]:
        return [producto.mostrar_informacion() for producto in self._productos]

    def listar_clientes(self) -> list[str]:
        return [cliente.mostrar_informacion() for cliente in self._clientes]

    def _existe_codigo_producto(self, codigo: str) -> bool:
        return any(producto.codigo == codigo for producto in self._productos)

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        return any(cliente.identificacion == identificacion for cliente in self._clientes)
