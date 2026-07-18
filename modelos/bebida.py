from modelos.producto import Producto


class Bebida(Producto):
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamaño: str
    ):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamaño = tamaño

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Tamaño: {self.tamaño}"
        )