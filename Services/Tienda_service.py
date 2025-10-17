"""
Módulo que define la clase TiendaService para gestionar la tienda online.
"""

from models.Usuario import Cliente, Administrador
from models.Producto import Producto, ProductoElectronico, ProductoRopa
from models.Pedido import Pedido
from datetime import datetime
import uuid
from typing import Optional


class TiendaService:
    """Clase que gestiona la tienda online."""
    def __init__(self):
        """Constructor de la clase TiendaService."""
        self.usuarios: dict[uuid.UUID, Cliente | Administrador] = {} #Diccionario ya que se guarda id y el objeto usuario
        self.productos: dict[uuid.UUID, Producto] = {} #Diccionario ya que se guarda id y el objeto producto
        self.pedidos: list[Pedido] = [] #Lista ya que solo se guardan los objetos pedido

    def registro_usuario(self, tipo: str, nombre: str, correo: str, direccion_postal: int=None) -> Cliente | Administrador:
        """Registra un nuevo usuario en la tienda.
        Args:
            tipo (str): Tipo de usuario ("cliente" o "administrador").
            nombre (str): Nombre del usuario.
            correo (str): Correo electrónico del usuario.
            direccion_postal (str, optional): Dirección postal del cliente. Requerido si el tipo es "cliente".
        Returns:
            Cliente | Administrador: El usuario registrado.
        Raises:
            ValueError: Si el tipo de usuario no es válido o si falta la dirección postal para un cliente.
        """
        
        if tipo.lower() == "cliente":
            if not direccion_postal:
                raise ValueError("Se necesita introducir una dirección postal.")
            usuario = Cliente(nombre, correo, direccion_postal)

        elif tipo.lower() == "administrador":
            usuario = Administrador(nombre, correo)
        
        else:
            raise ValueError("Tipo de usuario no válido. Introduzca cliente o administrador.")
        
        self.usuarios[usuario.id] = usuario
        return usuario

    def añadir_productos(self, producto: Producto) -> None:
        """Añade un producto a la tienda.
        Args:
            producto (Producto): El producto a añadir.
        """
        self.productos[producto.id] = producto

    def eliminar_producto_id(self, producto_id: uuid.UUID) -> None:
        """Elimina un producto de la tienda por su ID."""
        if producto_id in self.productos:
            del self.productos[producto_id]
        else:
            raise ValueError("No se encontró ningún producto con ese ID.")
        
    def listar_productos(self) -> list[Producto]:
        """Lista todos los productos disponibles en la tienda.
        Returns:
            list[Producto]: Lista de productos en la tienda.
        """
        return list(self.productos.values()) #Devuelve una lista con los valores del diccionario de productos

    def hacer_pedido(self, usuario_id: uuid.UUID, productos_cantidades: dict[uuid.UUID, int]) -> Pedido:
        """Crea un nuevo pedido para un usuario.
        Args:
            usuario_id (uuid.UUID): ID del usuario que realiza el pedido.
            productos_cantidades (dict): Diccionario con IDs de productos como claves y cantidades como valores.
        Returns:
            Pedido: El pedido creado.
        Raises:
            ValueError: Si el usuario no existe o si no es un cliente.
        """
        if usuario_id not in self.usuarios:
            raise ValueError("El usuario no existe.")
        
        usuario = self.usuarios[usuario_id]
        if not isinstance(usuario, Cliente): # Verifica si el usuario es un cliente con el método isinstance
            raise ValueError("Solo los clientes pueden realizar pedidos.")

        pedido = Pedido(datetime.now(), usuario) #Se crea un pedido con la fecha y el cliente

        for prod_id, cantidad in productos_cantidades.items(): #Recorre el diccionario de productos y cantidades
            if prod_id not in self.productos: # Verifica si el producto existe en el inventario
                raise ValueError(f"Producto con ID {prod_id} no encontrado.")
            
            producto = self.productos[prod_id] #Obtiene el producto del inventario
            pedido.agregar_producto(producto, cantidad) #Añade el producto al pedido con el método agregar_producto

        self.pedidos.append(pedido) #Añade el pedido a la lista de pedidos
        return pedido

    def listar_pedidos_usuario(self, usuario_id: uuid.UUID) -> list[Pedido]:
        """Lista todos los pedidos realizados por un usuario.
        Args:
            usuario_id (uuid.UUID): ID del usuario cuyos pedidos se quieren listar.
        Returns:
            list[Pedido]: Lista de pedidos del usuario.
        Raises:
            ValueError: Si el usuario no existe.
        """
        if usuario_id not in self.usuarios:
            raise ValueError("El usuario no existe.")
        
        pedidos_usuario = [p for p in self.pedidos if p.cliente.id == usuario_id] #Recorre todos los pedidos y añade los que coinciden con el id del usuario
        return sorted(pedidos_usuario, key=lambda p: p.fecha) #Sorted ordena los pedidos por fecha, del más antiguo al más reciente
    





