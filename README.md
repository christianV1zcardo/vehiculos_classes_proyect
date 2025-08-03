# Proyecto de Gestión de Flota de Vehículos en Python

Este proyecto es un ejercicio de programación orientada a objetos (POO) en Python que simula un sistema básico de gestión de flotas de vehículos. El objetivo principal es demostrar y aplicar conceptos fundamentales de la POO, como la herencia, el polimorfismo, la composición y el uso de atributos y métodos de clase.

## 🚀 Características Clave

El diseño del proyecto se centra en los siguientes principios de la POO:

  * **Herencia**: La clase `Vehiculo` actúa como una clase base, de la cual heredan clases más específicas como `Automovil`, `Motocicleta` y `Camion`. Esto permite reutilizar el código común y definir comportamientos únicos en las subclases.
  * **Polimorfismo**: El método `mostrar_estado()` es implementado de manera diferente en cada subclase, permitiendo que un solo método se comporte de distintas maneras dependiendo del objeto que lo llama.
  * **Composición**: Las clases `Flota` y `Conductor` no heredan de `Vehiculo`. En su lugar, "contienen" (componen) objetos de tipo `Vehiculo` como atributos, lo cual modela de forma más realista la relación entre estos objetos (un conductor tiene un vehículo, y una flota contiene varios vehículos).
  * **Atributos y Métodos de Clase**: Se utiliza un atributo de clase (`cantidad_vehiculos_creados`) y un método de clase (`mostrar_total_vehiculos_creados`) para llevar un registro global del número de vehículos creados sin depender de una instancia específica.

## 🚗 Clases Principales

El proyecto está estructurado en las siguientes clases:

  * **`Vehiculo`**: La clase base con atributos y métodos genéricos para cualquier vehículo (encender, apagar, acelerar, frenar, etc.).
  * **`Automovil`**: Hereda de `Vehiculo` y añade un atributo para el número de puertas y un método único para tocar la bocina.
  * **`Motocicleta`**: Hereda de `Vehiculo` y añade un atributo booleano para saber si es deportiva y un método para "hacer un caballito".
  * **`Camion`**: Hereda de `Vehiculo`, añade atributos de carga y sobrescribe el método `acelerar()` para reflejar el impacto del peso.
  * **`Flota`**: Utiliza composición para gestionar una lista de vehículos. Incluye métodos para agregar, remover, contar y mostrar el estado de toda la flota.
  * **`Conductor`**: Utiliza composición para representar a un conductor que puede tener un vehículo asignado. Sus métodos orquestan las acciones del vehículo que tiene.

## 🚀 Posibles Mejoras Futuras

  * **Gestión de Combustible**: Añadir un atributo `combustible` a la clase `Vehiculo` y modificar los métodos `encender()`, `acelerar()`, etc., para que lo consuman.
  * **Simulación Interactiva**: Crear una interfaz simple (por línea de comandos o una GUI básica) para que el usuario pueda interactuar con la flota y los conductores en tiempo real.
  * **Archivo de Configuración**: Usar archivos JSON o de texto para cargar la información inicial de los vehículos y conductores, en lugar de definirlos directamente en el código.

---

## 🧑‍💻 Autor

[Christian Vizcardo]
[www.linkedin.com/in/christian-vizcardo]