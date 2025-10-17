"""
Módulo que define la clase Pedido para gestionar los pedidos en la tienda online.
"""
from models.Usuario import Cliente
from models.Producto import Producto
import uuid
from datetime import datetime

class Pedido:
    """Clase que representa los pedidos."""
    def __init__(self, fecha: datetime, cliente: Cliente):
        """
        Constructor de la clase Pedido.
        Args:
            fecha (datetime): Fecha del pedido.
            cliente (Cliente): Cliente que realiza el pedido.
        """
        self.id: uuid.UUID = uuid.uuid4()
        self.fecha: datetime = fecha
        self.cliente: Cliente = cliente
        self.productos: dict[Producto, int] = {}

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        """Agrega un producto al pedido.
        Args:
            producto (Producto): El producto a agregar.
            cantidad (int): La cantidad del producto a agregar.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
        
        if producto.hay_stock(cantidad):
            if producto in self.productos:
                self.productos[producto] += cantidad
            else:
                self.productos[producto] = cantidad
            producto.actualizar_stock(producto.stock - cantidad)
        else:
            raise ValueError(f"No hay suficiente stock de {producto.nombre}.")

    def calcular_total(self) -> float:
        """Calcula el total del pedido.
        Returns:
            float: Total del pedido.
        """
        return sum(producto.precio * cantidad for producto, cantidad in self.productos.items())

    def __str__(self) -> str:
        """Representación de la información del pedido."""
        productos_resumen = "\n".join(
            [f"- {producto.nombre} x {cantidad} = {producto.precio * cantidad}€"
             for producto, cantidad in self.productos.items()]
        )
        return(
            f"Pedido ID: {self.id}\n"
            f"Fecha: {self.fecha}\n"
            f"Cliente: {self.cliente}\n"
            f"Productos:\n{productos_resumen if productos_resumen else 'Ninguno'}\n"
            f"Total: {self.calcular_total()}€"
        )

        
# ahora = Pedido(2002-6-12, "Fulano")

# print(ahora)
    