"""
Módulo que define las clases de productos para la tienda online.
"""
import uuid

class Producto:
    """Clase base para los productos."""
    def __init__(self, nombre: str, precio: float, stock: int):
        """
        Constructor de la clase Producto.
        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            stock (int): Cantidad en stock del producto.
        """
        self.id: uuid.UUID = uuid.uuid4()
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def hay_stock (self, cantidad: int) -> bool:
        """Verifica si hay suficiente stock para una cantidad dada.
        Args:
            cantidad (int): Cantidad a comprobar.
        Returns:
            bool: True si hay suficiente stock, False en caso contrario.
        """
        if cantidad > self.stock: #Se introduce un número, y si el stock es menor a ese número quiere decir que no hay suficientes productos
            return False
        else:
            return True
        
    def actualizar_stock(self, nueva_cantidad: int) -> None:
        """Actualiza la cantidad de stock del producto.
        Args:
            nueva_cantidad (int): Nueva cantidad de stock.
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad de stock no puede ser negativa.")
        self.stock = nueva_cantidad
    
    def __str__(self) -> str:
        """Representación de la información del producto."""
        return f"{self.nombre} (ID: {self.id}) - Precio: {self.precio}€, Stock: {self.stock}"
    
class ProductoElectronico(Producto):
    """Clase para productos electrónicos, hereda de Producto."""
    def __init__(self, nombre: str, precio: float, stock: int, meses_garantia: int):
        """
        Constructor de la clase ProductoElectronico.
        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            stock (int): Cantidad en stock del producto.
            meses_garantia (int): Meses de garantía del producto.
        """
        super().__init__(nombre, precio, stock)
        self.meses_garantia: int = meses_garantia
    def __str__(self) -> str:
        """Representación de la información del producto electrónico."""
        return f"{self.nombre} (ID: {self.id}) - Precio: {self.precio}€, Stock: {self.stock}, Meses de garantía: {self.meses_garantia}"


class ProductoRopa(Producto):
    """Clase para productos de ropa, hereda de Producto."""
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        """
        Constructor de la clase ProductoRopa.
        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            stock (int): Cantidad en stock del producto.
            talla (str): Talla del producto.
            color (str): Color del producto.
        """
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color
    def __str__(self) -> str:
        """Representación de la información del producto de ropa."""
        return f"{self.nombre} (ID: {self.id}) - Precio: {self.precio}€, Stock: {self.stock}, Talla: {self.talla}, Color: {self.color}"