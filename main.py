from funciones import agregar_libro, mostrar_libros, guardar_en_archivo, cargar_desde_archivo, estadisticas_libros


def menu():
    cargar_desde_archivo()  # Intentamos cargar si existe

    while True:
        print("\n📚 MENÚ PRINCIPAL")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Guardar en archivo")
        print("4. Cargar desde archivo")
        print("5. Ver estadísticas")
        print("6. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            guardar_en_archivo()
        elif opcion == "4":
            cargar_desde_archivo()
        elif opcion == "5":
            estadisticas_libros()
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()

