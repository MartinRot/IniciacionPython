# Iniciación a la Programación con Python 🐍

Repositorio para las actividades, prácticas y entregas del curso de Iniciación a la Programación con Python.

---

## 📋 Pre-entrega de Proyecto: Sistema de Gestión Básica de Productos

### 🎯 Contexto y Objetivo
Este proyecto consiste en diseñar un sistema interactivo por consola que permita gestionar la información inicial sobre los productos de la empresa.

---

### 📌 Requerimientos del Sistema

1. **Ingreso de datos de productos:**
   - Permite ingresar datos básicos: **nombre**, **categoría** y **precio** (número entero, sin centavos).
   - Los datos deben almacenarse en una lista principal (`productos = []`), donde cada producto esté representado como una sublista de tres elementos:  
     `[nombre, categoria, precio]`

2. **Visualización de productos registrados:**
   - Mostrar en pantalla todos los productos ingresados de manera ordenada y legible.
   - Cada producto debe aparecer numerado (ej. `1. Nombre: ..., Categoría: ..., Precio: $...`).
   - Si la lista está vacía, debe indicarse claramente al usuario.

3. **Búsqueda de productos:**
   - Permite buscar productos por su nombre.
   - Si encuentra coincidencias, muestra la información completa del o los productos coincidentes.
   - Si no hay coincidencias, informa que no se encontraron resultados.

4. **Eliminación de productos:**
   - Permite eliminar un producto de la lista identificándolo por su **posición (número)** en la lista.
   - Debe verificar que la posición ingresada sea válida antes de proceder con la eliminación.

5. **Control de ejecución y salida:**
   - El programa debe mantenerse en ejecución dentro de un bucle hasta que el usuario elija explícitamente la opción de salir.

---

### ⚙️ Requisitos Técnicos

- **Estructuras de datos:** Usar listas para almacenar y gestionar los datos (lista de sublistas).
- **Bucles:** Incorporar bucles `while` (para el menú interactivo) y `for` (para recorrer y mostrar productos).
- **Validaciones:** Validar todas las entradas del usuario para asegurar que no se ingresen datos vacíos o tipos incorrectos (evitando que el programa falle).
- **Condicionales:** Emplear `if`, `elif` y `else` para gestionar las opciones del menú y las validaciones.

---

### 🖥️ Menú de Opciones

```text
=======================================
Sistema de gestión básica de productos
=======================================
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
=======================================
```

---

## 📁 Estructura del Repositorio

```text
iniciacionPython/
│
├── .gitignore               # Configuración de exclusiones para Git
├── README.md                # Consignas y documentación del proyecto
└── preentrega/              # Archivos y desarrollo de la pre-entrega
    └── gestor_productos.py
```
