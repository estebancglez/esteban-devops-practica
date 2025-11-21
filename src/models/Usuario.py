"""
Define las clases para los usuarios, clientes y administradores
"""
from typing import Optional
import uuid

class Usuario:
    """Clase base para los usuarios."""
    def __init__(self, nombre: str, correo: str):
        """
        Constructor de la clase Usuario.
        Args:
            nombre (str): Nombre del usuario.
            correo (str): Correo electrónico del usuario.  
        """
        self.id: uuid.UUID = uuid.uuid4()
        self.nombre: str = nombre
        self.correo: str = correo
    
    def __str__(self) -> str:
        """Representación de la información del usuario."""
        return f"{self.nombre} (ID: {self.id}) - Correo: {self.correo}"

    def is_admin(self) -> bool:
        """Método para verificar si el usuario es administrador.
        Returns:
            bool: Siempre False para usuarios normales.
        """
        return False

class Cliente(Usuario):
    """Clase para los clientes, hereda de Usuario."""
    def __init__(self, nombre: str, correo: str, direccion_postal: str):
        """
        Constructor de la clase Cliente.
        Args:
            nombre (str): Nombre del cliente.
            correo (str): Correo electrónico del cliente.
            direccion_postal (str): Dirección postal del cliente.
        """
        super().__init__(nombre, correo)
        self.direccion_postal: str = direccion_postal
    
    def __str__(self) -> str:
        """Representación de la información del cliente."""
        return f"{super().__str__()} - Dirección Postal: {self.direccion_postal}"

class Administrador(Usuario):
    """Clase para los administradores, hereda de Usuario."""
    def is_admin(self) -> bool:
        """
        Método para verificar si el usuario es administrador.
        Returns:
            bool: Siempre True para administradores.
        """
        return True
    
    def __str__(self) -> str:
        """Representación de la información del administrador."""
        return f"{super().__str__()} - Administrador"
