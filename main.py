import carga
import limpieza
import analisis

isLoader  = False
isCleaned = False

df_usuarios = df_perfiles = df_cursos = df_calificaciones = None

while True:
    print("\n========================================")
    print("     SISTEMA DE GESTIÓN EDUCATIVA")
    print("========================================")
    print("  1. Cargar datos")
    print("  2. Limpiar datos")
    print("  3. Guardar datos limpios")
    print("  4. Análisis de Frecuencia")
    print("  5. Análisis de Agregación")
    print("  6. Análisis con Filtrado y Conteo")
    print("  7. Salir")
    print("========================================")

    opcion = input("Seleccione la opción deseada: ")

    match opcion:

        case '1':
            df_usuarios       = carga.cargaUsuarios()
            df_perfiles       = carga.cargaPerfiles()
            df_cursos         = carga.cargaCursos()
            df_calificaciones = carga.cargaCalificaciones()
            isLoader  = True
            isCleaned = False
            df_usuarios.info()
            df_perfiles.info()
            df_cursos.info()
            df_calificaciones.info()
            print("✅ Carga completa")

        case '2':
            if not isLoader:
                print("\n⚠️  Primero debes realizar la carga (opción 1)")
            else:
                limpieza.limpiar_usuarios(df_usuarios)
                limpieza.limpieza_perfiles(df_perfiles)
                limpieza.limpieza_cursos(df_cursos)
                limpieza.limpieza_calificaciones(df_calificaciones)
                isCleaned = True
                print("\n✅ Limpieza completa")

        case '3':
            if not isCleaned:
                print("\n⚠️  Primero debes realizar la limpieza (opción 2)")
            else:
                print("\n✅ ¡Proceso finalizado! Revisa la carpeta 'proccesed'.")

        case '4':
            if not isCleaned:
                print("\n⚠️  Primero debes cargar y limpiar los datos (opciones 1 y 2)")
            else:
                analisis.analisis_frecuencia()

        case '5':
            if not isCleaned:
                print("\n⚠️  Primero debes cargar y limpiar los datos (opciones 1 y 2)")
            else:
                analisis.analisis_agregacion()

        case '6':
            if not isCleaned:
                print("\n⚠️  Primero debes cargar y limpiar los datos (opciones 1 y 2)")
            else:
                analisis.analisis_filtrado()

        case '7':
            print("\n👋 Saliendo del sistema. ¡Hasta luego!")
            break

        case _:
            print("\n⚠️  Opción inválida. Selecciona una opción del 1 al 7.")
