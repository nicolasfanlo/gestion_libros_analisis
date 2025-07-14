import json
from collections import Counter
import statistics

libros = []

def agregar_libro():
    """Agrega un nuevo libro a la lista global."""
    global libros
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    try:
        paginas = int(input("Cantidad de páginas: "))
    except ValueError:
        print("⚠️ Ingresá un número válido.")
        return

    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "paginas": paginas
    }
    libros.append(libro)
    print("✅ Libro agregado con éxito.")

def mostrar_libros():
    """Muestra todos los libros cargados."""
    global libros
    if not libros:
        print("No hay libros cargados.")
        return

    for i, libro in enumerate(libros, start=1):
        print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['genero']}, {libro['paginas']} pág.)")

def guardar_en_archivo(nombre_archivo="libros.json"):
    """Guarda la lista de libros en un archivo JSON."""
    global libros
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)
    print(f"💾 Libros guardados en {nombre_archivo}.")

def cargar_desde_archivo(nombre_archivo="libros.json"):
    """Carga libros desde un archivo JSON (si existe)."""
    global libros
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            libros = json.load(f)
            print(f"📂 Se cargaron {len(libros)} libros desde el archivo.")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo. Empezando con una lista vacía.")
    except json.JSONDecodeError:
        print("⚠️ Error al leer el archivo. Verificá el formato JSON.")

def estadisticas_libros():
    """Muestra estadísticas básicas sobre los libros cargados."""
    global libros
    if not libros:
        print("⚠️ No hay libros cargados para analizar.")
        return

    total = len(libros)
    paginas = [libro["paginas"] for libro in libros]
    generos = [libro["genero"] for libro in libros]
    autores = [libro["autor"] for libro in libros]

    print("\n📊 ESTADÍSTICAS DE LIBROS")
    print(f"🔢 Total de libros: {total}")
    print(f"📖 Promedio de páginas: {statistics.mean(paginas):.2f}")

    genero_mas_comun = Counter(generos).most_common(1)[0]
    print(f"📚 Género más frecuente: {genero_mas_comun[0]} ({genero_mas_comun[1]} libros)")

    autor_mas_comun = Counter(autores).most_common(1)[0]
    print(f"🖋️ Autor más frecuente: {autor_mas_comun[0]} ({autor_mas_comun[1]} libros)")
