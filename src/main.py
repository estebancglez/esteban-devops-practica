"""
Archivo principal para ejecutar la tienda online.
"""
from Services.Tienda_service import TiendaService
from models.Producto import Producto, ProductoRopa, ProductoElectronico

# Crear servicio
tienda = TiendaService()

# Registrar usuarios
cliente1 = tienda.registro_usuario("cliente", "Guille", "guille@gmail.com", "Calle García Barbón, 123")
cliente2 = tienda.registro_usuario("cliente", "Inés", "ines@gmail.com", "Calle Urzaiz 45, 456")
cliente3 = tienda.registro_usuario("cliente", "Miguel", "miguel@gmail.com", "Calle Florida 3, 789")
admin = tienda.registro_usuario("administrador", "Admin", "admin@gmail.com")

# Ver ids de usuarios
print(f"ID Cliente 1: {cliente1.id}")
print(f"ID Cliente 2: {cliente2.id}")
print(f"ID Cliente 3: {cliente3.id}")
print(f"ID Administrador: {admin.id}")

# Añadir productos
p1 = Producto("Manzana", 2.5, 10)
p2 = ProductoRopa("Camiseta", 20, 5, "M", "Azul")
p3 = ProductoElectronico("Portatil", 1200, 3, 24)
p4 = ProductoRopa("Pantalón", 35, 7, "L", "Negro")
p5 = ProductoElectronico("Auriculares", 150, 8, 12)

tienda.añadir_productos(p1)
tienda.añadir_productos(p2)
tienda.añadir_productos(p3)
tienda.añadir_productos(p4)
tienda.añadir_productos(p5)

# Listar productos
print("\n Inventario inicial:")
for productos in tienda.listar_productos():
    print(productos)

# Hacer pedidos
pedido1 = tienda.hacer_pedido(cliente1.id, {p1.id: 3, p2.id: 1})
pedido2 = tienda.hacer_pedido(cliente2.id, {p3.id: 1, p5.id: 2})
pedido3 = tienda.hacer_pedido(cliente1.id, {p4.id: 2, p1.id: 2})

print("\n Resumen de pedidos realizados:")
print(pedido1)
print("\n", pedido2)
print("\n", pedido3)

# Listar pedidos de un cliente
print("\n Histórico de pedidos de Fulano:")
for p in tienda.listar_pedidos_usuario(cliente1.id):
    print("\n", p)

# Mostrar stock actualizado
print("\n Inventario actualizado:")
for productos in tienda.listar_productos():
    print(productos)

# Probar método Eliminar un producto
tienda.eliminar_producto_id(p2.id)
print("\n Inventario tras eliminar un producto:")
for productos in tienda.listar_productos():
    print(productos)