class Producto:

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo = self._validar_texto(codigo, "El codigo no puede estar vacio.")
        self.nombre = self._validar_texto(nombre, "El nombre no puede estar vacio.")
        self.categoria = self._validar_texto(categoria, "La categoria no puede estar vacia.")
        self.precio = self._validar_precio(precio)

    @staticmethod
    def _validar_texto(valor: str, mensaje_error: str) -> str:
        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(mensaje_error)
        return valor_limpio

    @staticmethod
    def _validar_precio(precio: float) -> float:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        return precio

    def mostrar_informacion(self) -> str:
        return (
            f"Codigo: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoria: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )
