Nombre de la aplicación: Tienda online

Autor: Celso Esteban Costas González

Descripción: Este proyecto consiste en una aplicación Python diseñada para gestionar una tienda
online. Implementa un sistema de usuarios, productos y pedidos, que permite registrar clientes y
administradores, añadir y eliminar productos del inventario, y gestionar pedidos realizados por 
los clientes. La aplicación está estructurada en módulos que representan usuarios, productos y
pedidos, además de un servicio proncipar denominado TiendaService.

Contenerización con Docker

Los pasos para construir, ejecutar y probar la aplicación dentro de un 
contenedor de Docker son los siguientes:

Contrucción de la imagen Docker:
docker build -t esteban/tienda-online:1.0 .
Esto generará una imagen con la etiqueta esteban/tienda-online:1.0

Ejecución del contenedor
docker run --rm esteban/tienda-online:1.0
El contenedor iniciará y ejecutará el archivo:
src/main.py

Pruebas y comportamiento esperado
Al ejecutar la imagen el programa debería:
    Crear usuarios utilizando la clase TiendaService
    Añadir productos al inventario
    Generar pedidos de ejemplo
    Imprimir resultados por consola

Variables de entorno
No requiere variables de entorno para su ejecución

Estructura del proyecto:
El proyecto debe mantener la siguiente estructura:
esteban-devops-practica/
Dockerfile
.dockerignore
requirements.txt
README.md
src/
main.py
Services/
models/