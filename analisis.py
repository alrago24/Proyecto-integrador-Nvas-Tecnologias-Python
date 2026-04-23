import pandas as pd

if __name__ == '__main__':

# Carga de los datos ya limpios
    df_usuarios = pd.read_csv('./data/proccesed/usuarios_limpios.csv')
    df_perfiles = pd.read_csv('./data/proccesed/perfiles_limpios.csv')
    df_cursos = pd.read_csv('./data/proccesed/cursos_limpios.csv')
    df_estudiantes = pd.read_csv('./data/proccesed/estudiantes_limpios.csv')
    df_calificaciones = pd.read_csv('./data/proccesed/calificaciones_limpias.csv')

    # --- COMBINACIÓN (MERGE) ---

    # Renombrar 'nombre' en cursos antes del merge para evitar conflicto
    # con la columna 'nombre' que viene de usuarios
    df_cursos = df_cursos.rename(columns={'nombre': 'nombre_curso'})

    # drop_duplicates() elimina filas repetidas dejando solo un registro por curso_id
    # así evitamos que el merge multiplique las calificaciones
    df_cursos_unicos = df_cursos[['id', 'nombre_curso']].drop_duplicates(subset='id')

    # Se unen los estudiantes con usuarios para obtener el nombre del estudiante

    df_estudiante_usuarios = pd.merge(df_estudiantes, df_usuarios, left_on='usuario_id', right_on='id', suffixes=('_estudiante', '_usuario'))

    # Unir calificaciones con la tabla anterior para tener nombre del estudiante
    df_calificaciones_completas = pd.merge(df_calificaciones, df_estudiante_usuarios, left_on='estudiante_id', right_on='id_estudiante')

    # Se une con cursos únicos para tener el nombre del curso sin duplicar registros -
    df_calificaciones_completas = pd.merge(df_calificaciones_completas, df_cursos_unicos, left_on='curso_id', right_on='id', suffixes=('', '_curso'))

    # =============================================================
    # 1. ANÁLISIS DE FRECUENCIA
    # ¿Cuál es el curso con mayor cantidad de calificaciones registradas?
    # Con value_counts() se cuenta las calificaciones que tiene cada curso
    # Con idxmax() brinda el nombre del curso con más registros
    # max() devuelve la cantidad de registros
    # nunique() cuenta los estudiantes únicos por curso (sin repetidos)
    # =============================================================

    print("1. ANÁLISIS DE FRECUENCIA")
    print("   ¿Cuál es el curso con más calificaciones registradas?\n")

    cuenta_cursos = df_calificaciones_completas['nombre_curso'].value_counts()
    curso_mas_calificaciones = cuenta_cursos.idxmax()
    cantidad_calificaciones = cuenta_cursos.max()

    print(f"   El curso con más calificaciones es: '{curso_mas_calificaciones}' con {cantidad_calificaciones} registros")
    print(f"\n   Cantidad completa por curso:\n{cuenta_cursos.to_string()}\n")

    print("   ¿Cuál es la cantidad de estudiantes por curso?\n")

    # Cantidad de estudiantes únicos por curso
    # nunique() evita contar el mismo estudiante más de una vez si tuviera varias calificaciones

    estudiantes_por_curso = df_calificaciones_completas.groupby('nombre_curso')['estudiante_id'].nunique()
    print(f"   Cantidad de estudiantes por curso:\n{estudiantes_por_curso.to_string()}\n")

