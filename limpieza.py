import pandas as pd
import numpy as np



def limpiar_usuarios(df_usuarios):
    # Limpieza de espacio y texto en formato titulo.
    print("Limpieza de espacio y texto en formato titulo")
    df_usuarios["nombre"] = df_usuarios["nombre"].str.strip().str.title()
    df_usuarios["apellido"] = df_usuarios["apellido"].str.strip().str.title()
    df_usuarios["email"] = df_usuarios["email"].str.strip().str.lower()

    # Eliminar datos duplicados
    print("Eliminar datos duplicados")
    df_usuarios = df_usuarios.drop_duplicates()

    print("Reemplazar datos con un valor")
    # Reemplazar datos con un valor
    df_usuarios["edad"] = df_usuarios["edad"].replace("veinte", 20)
    df_usuarios["edad"] = df_usuarios["edad"].replace("-5", 20)
    df_usuarios["edad"] = df_usuarios["edad"].replace("150", 20)
    df_usuarios["edad"] = (
        pd.to_numeric(df_usuarios["edad"], errors="coerce").fillna(0).astype(int)
    )

    print("Tratamiento de Nulos")
    # Tratamiento de Nulos
    df_usuarios["edad"] = df_usuarios["edad"].fillna(df_usuarios["edad"].mean())
    df_usuarios["edad"] = df_usuarios["edad"].replace(0, df_usuarios["edad"].mean())

    # index=False evita guardar el índice de Pandas en el archivo
    df_usuarios.to_csv("data/proccesed/usuarios_limpios.csv", index=False)


def limpieza_perfiles(df_perfiles):
    print("Limpieza de espacio y texto en formato titulo")
    df_perfiles["direccion"] = df_perfiles["direccion"].str.strip()

    print("Reemplazar datos con un valor")
    # Reemplazar datos con un valor
    df_perfiles["id"] = df_perfiles["id"].replace("ID_1", 1)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_2", 2)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_3", 3)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_17", 17)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_29", 29)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_32", 32)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_35", 35)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_38", 38)
    df_perfiles["id"] = df_perfiles["id"].replace("ID_49", 49)

    print("Reemplazar datos con un valor")
    # Reemplazar datos con un valor
    # Convertir 'N/A' y celdas vacías en nulos
    df_perfiles["telefono"] = df_perfiles["telefono"].replace(["N/A"], np.nan)
    df_perfiles["telefono"] = df_perfiles["telefono"].replace([""], np.nan)
    df_perfiles["telefono"] = df_perfiles["telefono"].replace([" "], np.nan)
    df_perfiles["direccion"] = df_perfiles["direccion"].replace(
        "", "Sin dirección registrada"
    )

    # Explicación del r'[^\d]': Busca cualquier cosa que NO sea un número y la borra
    df_perfiles["telefono"] = (
        df_perfiles["telefono"].astype(str).str.replace(r"[^\d]", "", regex=True)
    )

    # El paso anterior convierte los NaN en la palabra "nan", hay que devolverlos a nulos
    df_perfiles["telefono"] = df_perfiles["telefono"].replace("nan", np.nan)

    # . Rellenar los que quedaron vacíos después de la limpieza
    df_perfiles["telefono"] = df_perfiles["telefono"].fillna(00000000)

    # Eliminar el 57 al inicio del número de teléfono
    df_perfiles["telefono"] = df_perfiles["telefono"].str.lstrip("57")

    # index=False evita guardar el índice de Pandas en el archivo
    df_perfiles.to_csv("data/proccesed/perfiles_limpios.csv", index=False)

def limpieza_cursos(df_cursos):
        print("Limpieza de espacio y texto en formato titulo")
        df_cursos["nombre"] = df_cursos["nombre"].str.strip().str.title()
        df_cursos["descripcion"] = df_cursos["descripcion"].str.strip().str.capitalize()
        # Se crea un "Mapa de Referencia"
        # Se filtra las filas que si tienen descripción y creamos un diccionario único
        diccionario_descripciones = df_cursos[
            df_cursos["descripcion"].notna() & (df_cursos["descripcion"] != "")
        ]
        diccionario_descripciones = diccionario_descripciones.drop_duplicates(
            "nombre"
        ).set_index("nombre")["descripcion"]

        # Se rellenan los vacios usando el diccionario
        # .fillna() buscará el nombre del curso en nuestro diccionario y pondrá la descripción que corresponda
        df_cursos["descripcion"] = df_cursos["descripcion"].fillna(
            df_cursos["nombre"].map(diccionario_descripciones)
        )

        # Los cursos que nunca tuvieron descripción en ninguna fila, se les asigna un valor por defecto
        df_cursos["descripcion"] = df_cursos["descripcion"].fillna(
            "Descripción pendiente de asignar"
        )

        # index=False evita guardar el índice de Pandas en el archivo
        df_cursos.to_csv("data/proccesed/cursos_limpios.csv", index=False)
def limpieza_calificaciones(df_calificaciones):
        print('Limpieza de notas vacias')
        df_calificaciones['nota'] = df_calificaciones['nota'].replace(['N/A', 'NULL', ''], 1)
        df_calificaciones['nota'] = df_calificaciones['nota'].replace('UNO', 1)
        df_calificaciones['nota'] = df_calificaciones['nota'].replace('DOS', 2)
        df_calificaciones['nota'] = df_calificaciones['nota'].replace('TRES', 3)
        df_calificaciones['nota'] = df_calificaciones['nota'].replace('CUATRO', 4)
        df_calificaciones['nota'] = df_calificaciones['nota'].replace('CINCO', 5)
        df_calificaciones['nota'] = df_calificaciones['nota'].replace('APROBADO', 3.5)

        # Convertir la columna a numérica, forzando los errores a NaN
        df_calificaciones['nota'] = pd.to_numeric(df_calificaciones['nota'], errors='coerce')

        # 4. ELIMINAR NOTAS FUERA DE RANGO (escala 1.0 - 5.0)
        notas_fuera_de_rango = df_calificaciones[~df_calificaciones['nota'].between(1.0, 5.0)]
        df_calificaciones = df_calificaciones[df_calificaciones['nota'].between(1.0, 5.0)]
        print(f"Se encontraron {len(notas_fuera_de_rango)} registros con notas inválidas.")

        print(f"Registros limpios: {len(df_calificaciones)}")
        print(notas_fuera_de_rango)


        # index=False evita guardar el índice de Pandas en el archivo
        df_calificaciones.to_csv('data/proccesed/calificaciones_limpias.csv', index=False)