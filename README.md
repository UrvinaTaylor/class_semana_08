Sistema Restaurante App
Descripción
Sistema desarrollado en Python para la gestión básica de un restaurante mediante Programación Orientada a Objetos.

Permite registrar y listar productos, bebidas y clientes utilizando un menú interactivo desde consola.

Estructura del proyecto
restaurante_app │ │---------modelos/ │ ├--producto.py │ ├-- bebida.py │ └--cliente.py │ ├─-------- servicios/ │ └--restaurante.py │ ├----------main.py └----------README.md

Clases implementadas
Producto
Clase base que representa los productos del restaurante.

Atributos:

Código
Nombre
Categoría
Precio
Bebida
Clase que hereda de Producto y agrega información específica:

Tamaño
Aplica herencia y polimorfismo mediante el método ##Mostrar_informacion().

Cliente
Representa los datos de los clientes registrados.

Atributos:

Identificación
Nombre
Correo
Restaurante
Clase encargada de administrar:

Lista de productos.
Lista de clientes.
Registro y validación de datos.
Listado de información.
Principios SOLID aplicados
Responsabilidad única
Cada clase cumple una función específica dentro del sistema.

Abierto/cerrado
La clase Bebida amplía la clase Producto sin modificar la lógica principal.

Sustitución de Liskov
Los objetos Bebida pueden utilizarse como objetos Producto.

Ejecución
Ejecutar el archivo principal:

Autor
Urvina Santi Gilmar Taylor de segundo semestre - Carrera de Sistemas
