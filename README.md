# Sistema de Restaurante — Semana 8

**Estudiante:** Leython Josue Hidalgo Valdez  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 8 — Organización modular de un sistema orientado a objetos en Python

---

## Descripción del sistema

Sistema de gestión básica para un restaurante desarrollado en Python con POO. Permite registrar y listar productos, bebidas y clientes a través de un menú interactivo ejecutado desde la consola. El proyecto aplica principios SOLID dentro de una arquitectura modular con capas claramente separadas.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

---

## Responsabilidad de cada clase

| Clase / Archivo | Responsabilidad |
|---|---|
| `Producto` | Representa los datos comunes de un producto: codigo, nombre, categoria y precio. Valida sus propios atributos y expone `mostrar_informacion()`. |
| `Bebida` | Especialización de `Producto`. Agrega `tamano` y `tipo_envase`. Sobreescribe `mostrar_informacion()` incluyendo esos atributos. |
| `Cliente` | Representa la información de un cliente: identificacion, nombre y correo. Valida sus propios atributos y expone `mostrar_informacion()`. |
| `Restaurante` | Administra las colecciones de productos y clientes. Registra objetos, valida duplicados y retorna la información mediante listas. |
| `main.py` | Punto de entrada. Muestra el menú, recoge datos con `input()`, crea los objetos y llama al servicio. No gestiona listas ni lógica de negocio. |

---

## Relación entre Producto y Bebida

`Bebida` hereda de `Producto` porque una bebida **es un tipo de producto** del restaurante. Gracias a esa herencia, ambas clases se almacenan en la misma lista `_productos` dentro de `Restaurante`. Al listar, el servicio llama a `mostrar_informacion()` sobre cada elemento sin verificar de qué tipo concreto se trata: `Producto` devuelve sus cuatro campos, y `Bebida` devuelve esos mismos cuatro campos más los suyos propios.

---

## Principios SOLID aplicados

### S — Responsabilidad única (SRP)

Cada clase tiene una única razón para cambiar:

- `Producto` cambia solo si se modifica la estructura de un producto general.
- `Bebida` cambia solo si se modifica lo que hace específica a una bebida.
- `Cliente` cambia solo si se modifica la información de un cliente.
- `Restaurante` cambia solo si se modifica la lógica de administración de colecciones.
- `main.py` cambia solo si se modifica la forma en que el usuario interactúa con el sistema.

Ninguna clase mezcla responsabilidades: la validación de datos está dentro de cada modelo mediante métodos estáticos (`_validar_texto`, `_validar_precio`, `_validar_correo`), la gestión de colecciones está en el servicio y la interacción por consola está en `main.py`.

### O — Abierto/Cerrado (OCP)

El sistema está abierto a la extensión y cerrado a la modificación. La clase `Bebida` amplía el sistema añadiendo atributos propios y sobreescribiendo `mostrar_informacion()` sin modificar `Producto` ni `Restaurante`. Si en el futuro se necesitara agregar una clase `Postre` o `Entrada`, bastaría con crear una nueva clase que herede de `Producto` y la lógica del servicio funcionaría sin cambios, porque opera sobre el tipo `Producto` de forma general.

### L — Sustitución de Liskov (LSP)

Un objeto `Bebida` puede usarse en cualquier lugar donde se espera un `Producto` sin generar errores ni alterar el comportamiento esperado. El servicio recibe `Producto` como tipo de parámetro en `registrar_producto()` y accede a `.codigo` y `.mostrar_informacion()` sin importar si el objeto es un `Producto` o una `Bebida`. La lista `_productos` almacena ambos tipos y el listado los procesa de forma uniforme.

---

## Instrucciones de ejecución

1. Clonar o descargar el repositorio.
2. Ubicarse en la carpeta raíz del proyecto (donde se encuentra `README.md`).
3. Ejecutar con:

```bash
python restaurante_app/main.py
```

4. Usar el menú para registrar productos, bebidas o clientes, y para listarlos.

---

## Reflexión

Diseñar un proyecto con responsabilidades claras hace que cada parte del código sea más fácil de entender, modificar y extender. Cuando una clase tiene un único propósito, un error o un cambio de requisito afecta solo el componente que corresponde. Con herencia bien aplicada, ampliar el sistema no obliga a reescribir lo que ya funciona. Estas decisiones marcan la diferencia entre un proyecto que se mantiene con el tiempo y uno que se vuelve difícil de sostener con cada nueva función que se agrega.
