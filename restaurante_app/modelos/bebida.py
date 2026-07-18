from modelos.producto import Producto


class Bebida(Producto):

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        tipo_envase: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = self._validar_texto(tamano, "El tamano no puede estar vacio.")
        self.tipo_envase = self._validar_texto(tipo_envase, "El tipo de envase no puede estar vacio.")

    def mostrar_informacion(self) -> str:
        return (
            f"{super().mostrar_informacion()} | "
            f"Tamano: {self.tamano} | "
            f"Tipo de envase: {self.tipo_envase}"
        )
