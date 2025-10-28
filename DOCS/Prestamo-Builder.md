
---

# Préstamo Builder y Test Unitario

## 1. Objetivo

El objetivo de esta implementación es construir objetos **Préstamo** complejos de manera controlada y flexible, permitiendo configurar distintos atributos opcionales como:

* **Socio**
* **Libro**
* **Fecha de inicio**
* **Fecha de vencimiento**

El patrón **Builder** se eligió para:

1. Separar la construcción del objeto de su uso en la lógica de negocio.
2. Facilitar la creación de objetos con diferentes configuraciones sin multiplicar constructores.
3. Mejorar la legibilidad y el mantenimiento del código.
4. Permitir la reutilización del builder para construir múltiples objetos de manera consistente.

---

## 2. Implementación

Se definió la clase `PrestamoBuilder` dentro de `prestamoBuild.py`, la cual incluye **métodos encadenables** para establecer cada atributo, permitiendo construir el objeto `Prestamo` paso a paso:

```python
builder = PrestamoBuilder()
prestamo = (
    builder
    .set_socio("Juan Perez")
    .set_libro("1984 - George Orwell")
    .build()
)
```

* `set_socio()`: asigna el socio que realiza el préstamo.
* `set_libro()`: asigna el libro prestado.
* `build()`: construye el objeto `Prestamo` con los valores configurados y calcula la fecha de vencimiento automáticamente (7 días por defecto).

---

## 3. Pruebas Unitarias

Se formalizó un **test unitario** utilizando `unittest` para garantizar que:

1. El objeto `Prestamo` se construye correctamente con los valores por defecto.
2. La fecha de vencimiento se calcula correctamente (7 días después de la fecha de inicio).

### Ejemplo de test

```python
import unittest
from datetime import date, timedelta
from SRC.services.prestamoService.prestamoBuild import PrestamoBuilder

class TestPrestamoBuilder(unittest.TestCase):

    def test_creacion_basica(self):
        builder = PrestamoBuilder()
        prestamo = (
            builder
            .set_socio("Juan Perez")
            .set_libro("1984 - George Orwell")
            .build()
        )

        self.assertEqual(prestamo.socio, "Juan Perez")
        self.assertEqual(prestamo.libro, "1984 - George Orwell")
        self.assertEqual(prestamo.fecha_vencimiento, date.today() + timedelta(days=7))

if __name__ == "__main__":
    unittest.main()
```

### Comando para ejecutar los tests

```bash
python -m unittest discover -s tests
```

Este comando busca automáticamente todos los tests dentro de la carpeta `tests` y los ejecuta.

---
