# 📚 Sistema de Gestión de Libros

Este proyecto es parte del trabajo final de la materia **Programación** de la Tecnicatura en Análisis de Datos.

Permite cargar, visualizar, guardar y analizar información básica sobre una colección de libros. Está desarrollado aplicando buenas prácticas de programación con Python, haciendo foco en código limpio, modular, documentado y reutilizable.

---

## 🚀 Funcionalidades

- ✅ Agregar libros con título, autor, género y cantidad de páginas.
- ✅ Mostrar todos los libros cargados.
- ✅ Guardar y cargar libros desde un archivo `.json`.
- ✅ Ver estadísticas simples:
  - Total de libros.
  - Promedio de páginas.
  - Género más frecuente.
  - Autor más frecuente.

---

## ⚙️ Requisitos del sistema

- Python 3.8 o superior
- Git (opcional, para clonar el repositorio)

---

## 🛠️ Instalación y ejecución

1. Cloná el repositorio (o descargalo como `.zip`):

```bash
git clone https://github.com/nicolasfanlo/gestion_libros_analisis.git
cd gestion_libros_analisis


Activá un entorno virtual (recomendado):

python -m venv venv
.\venv\Scripts\activate  # En Windows


Ejecutá el programa:

python main.py


Librerías utilizadas

Este programa solo utiliza módulos de la librería estándar de Python:

json

statistics

collections.Counter

Por lo tanto, no es necesario instalar paquetes adicionales.



🧠 Zen de Python aplicado

“Simple is better than complex.”

El programa fue diseñado con una lógica clara y funciones separadas, favoreciendo la simplicidad y legibilidad por sobre la complejidad innecesaria.




📁 Estructura del proyecto:

gestion_libros_analisis/
├── funciones.py         # Todas las funciones del sistema
├── main.py              # Punto de entrada y menú principal
├── libros.json          # Archivo de datos (generado automáticamente)
├── README.md            # Este archivo
└── venv/                # Entorno virtual (no subir a GitHub)




👨‍💻 Autor
Nicolás Saavedra Fanlo
Tecnicatura en Análisis de Datos


🔐 Licencia
Este proyecto es de uso educativo.