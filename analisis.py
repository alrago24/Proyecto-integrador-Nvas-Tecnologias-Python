import pandas as pd


#Sergio
def _preparar_datos():
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

        return df_calificaciones_completas


def analisis_frecuencia():
        # =============================================================
        # 1. ANÁLISIS DE FRECUENCIA
        # ¿Cuál es el curso con mayor cantidad de calificaciones registradas?
        # Con value_counts() se cuenta las calificaciones que tiene cada curso
        # Con idxmax() brinda el nombre del curso con más registros
        # max() devuelve la cantidad de registros
        # nunique() cuenta los estudiantes únicos por curso (sin repetidos)
        # =============================================================
        df_calificaciones_completas = _preparar_datos()
        
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

    
def analisis_agregacion():
        # =============================================================
        # 2. ANÁLISIS DE AGREGACIÓN (GROUPBY)
        # ¿Cuál es la nota promedio por curso?
        # Con groupby() agrupamos los registros por nombre de curso
        # Con mean() calculamos el promedio de nota para cada grupo
        # Con round() redondeamos a 2 decimales para mejor lectura
        # =============================================================

        print("2. ANÁLISIS DE AGREGACIÓN")
        print("   ¿Cuál es la nota promedio por curso?\n")

        df_calificaciones_completas = _preparar_datos()

        nota_promedio_curso = df_calificaciones_completas.groupby('nombre_curso')['nota'].mean().round(2)
        print("   Nota promedio por curso: ")
        print(nota_promedio_curso.to_string())

        # =============================================================
        # 2.1
        # ¿Cuál es la edad promedio por curso?
        # Con groupby() agrupamos los registros por nombre de curso
        # Con mean() calculamos el promedio de edad para cada grupo
        # =============================================================

        print("\n   ¿Cuál es la edad promedio por curso?\n")
        edad_promedio_curso = df_calificaciones_completas.groupby('nombre_curso')['edad'].mean().round(0)
        print("   Edad promedio por curso: ")
        print(edad_promedio_curso.to_string())

    # =============================================================
    # 3. ANÁLISIS CON FILTRADO Y CONTEO
    # ¿Cuántos estudiantes aprobaron el curso 'Bases De Datos Sql'? (nota >= 3.0)
    # Se filtra por nombre del curso y nota mínima aprobatoria
    # len() cuenta cuántos registros cumplen ambas condiciones
    # =============================================================

def analisis_filtrado():
        print("\n3. ANÁLISIS CON FILTRADO Y CONTEO\n")
        print("   ¿Cuántos estudiantes aprobaron el curso 'Bases De Datos Sql' (nota mayor a 3.5)?\n")

        df_calificaciones_completas = _preparar_datos()
        # Se define el curso a analizar y la nota mínima aprobatoria
        curso_BD = 'Bases De Datos Sql'
        curso_python = 'Python Para Data Science'
        curso_frontend = 'Frontend Avanzado'
        curso_git = 'Introducción A Git'
        curso_web = 'Desarrollo Web Con Java'
        curso_software = 'Arquitectura De Software'
        nota_minima_aprobatoria = 3.5

        # Se filtran los registros que corresponden al curso seleccionado y tienen nota mayor o igual a la mínima aprobatoria
        estudiantes_aprobados_BD = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_BD) &
            (df_calificaciones_completas['nota'] >= nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_aprobados_BD = len(estudiantes_aprobados_BD)
        print(f"   Cantidad de estudiantes que aprobaron '{curso_BD}': {cantidad_estudiantes_aprobados_BD}")

        # =============================================================
        # 3.1
        # ¿Cuántos estudiantes reprobaron el curso 'Bases De Datos Sql'? (nota < 3.5)
        # Se filtra por nombre del curso y nota mínima aprobatoria
        # len() cuenta cuántos registros cumplen ambas condiciones
        # =============================================================

        print("   ¿Cuántos estudiantes reprobaron el curso 'Bases De Datos Sql' (nota menor a 3.5)?\n")

        # Se filtran los registros que corresponden al curso seleccionado y tienen nota menor a la mínima aprobatoria
        estudiantes_reprobados_BD = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_BD) &
            (df_calificaciones_completas['nota'] < nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_reprobados_BD = len(estudiantes_reprobados_BD)
        print(f"   Cantidad de estudiantes que reprobaron '{curso_BD}': {cantidad_estudiantes_reprobados_BD}")

        print("\n   ¿Cuántos estudiantes aprobaron el curso 'Python Para Data Science' (nota mayor a 3.5)?\n")
        estudiantes_aprobados_python = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_python) &
            (df_calificaciones_completas['nota'] >= nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_aprobados_python = len(estudiantes_aprobados_python)
        print(f"   Cantidad de estudiantes que aprobaron '{curso_python}': {cantidad_estudiantes_aprobados_python}")
        
        print("   ¿Cuántos estudiantes reprobaron el curso 'Python Para Data Science' (nota menor a 3.5)?\n")

        # Se filtran los registros que corresponden al curso seleccionado y tienen nota menor a la mínima aprobatoria
        estudiantes_reprobados_python = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_python) &
            (df_calificaciones_completas['nota'] < nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_reprobados_python = len(estudiantes_reprobados_python)
        print(f"   Cantidad de estudiantes que reprobaron '{curso_python}': {cantidad_estudiantes_reprobados_python}")

        print("\n   ¿Cuántos estudiantes aprobaron el curso 'Frontend Avanzado' (nota mayor a 3.5)?\n")
        estudiantes_aprobados_frontend = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_frontend) &
            (df_calificaciones_completas['nota'] >= nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_aprobados_frontend = len(estudiantes_aprobados_frontend)
        print(f"   Cantidad de estudiantes que aprobaron '{curso_frontend}': {cantidad_estudiantes_aprobados_frontend}")

        print("   ¿Cuántos estudiantes reprobaron el curso 'Frontend Avanzado' (nota menor a 3.5)?\n")

        # Se filtran los registros que corresponden al curso seleccionado y tienen nota menor a la mínima aprobatoria
        estudiantes_reprobados_frontend = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_frontend) &
            (df_calificaciones_completas['nota'] < nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_reprobados_frontend = len(estudiantes_reprobados_frontend)
        print(f"   Cantidad de estudiantes que reprobaron '{curso_frontend}': {cantidad_estudiantes_reprobados_frontend}")

        print("\n   ¿Cuántos estudiantes aprobaron el curso 'Introducción A Git' (nota mayor a 3.5)?\n")
        estudiantes_aprobados_git = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_git) &
            (df_calificaciones_completas['nota'] >= nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_aprobados_git = len(estudiantes_aprobados_git)
        print(f"   Cantidad de estudiantes que aprobaron '{curso_git}': {cantidad_estudiantes_aprobados_git}")

        print("   ¿Cuántos estudiantes reprobaron el curso 'Introducción A Git' (nota menor a 3.5)?\n")

        # Se filtran los registros que corresponden al curso seleccionado y tienen nota menor a la mínima aprobatoria
        estudiantes_reprobados_git = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_git) &
            (df_calificaciones_completas['nota'] < nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_reprobados_git = len(estudiantes_reprobados_git)
        print(f"   Cantidad de estudiantes que reprobaron '{curso_git}': {cantidad_estudiantes_reprobados_git}")

        print("\n   ¿Cuántos estudiantes aprobaron el curso 'Desarrollo Web Con Java' (nota mayor a 3.5)?\n")
        estudiantes_aprobados_java = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_web) &
            (df_calificaciones_completas['nota'] >= nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_aprobados_java = len(estudiantes_aprobados_java)
        print(f"   Cantidad de estudiantes que aprobaron '{curso_web}': {cantidad_estudiantes_aprobados_java}")

        print("   ¿Cuántos estudiantes reprobaron el curso 'Desarrollo Web Con Java' (nota menor a 3.5)?\n")

        # Se filtran los registros que corresponden al curso seleccionado y tienen nota menor a la mínima aprobatoria
        estudiantes_reprobados_java = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_web) &
            (df_calificaciones_completas['nota'] < nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_reprobados_java = len(estudiantes_reprobados_java)
        print(f"   Cantidad de estudiantes que reprobaron '{curso_web}': {cantidad_estudiantes_reprobados_java}\n")

        print("\n   ¿Cuántos estudiantes aprobaron el curso 'Arquitectura De Software' (nota mayor a 3.5)?\n")
        estudiantes_aprobados_software = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_software) &
            (df_calificaciones_completas['nota'] >= nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_aprobados_software = len(estudiantes_aprobados_software)
        print(f"   Cantidad de estudiantes que aprobaron '{curso_software}': {cantidad_estudiantes_aprobados_software}")

        print("   ¿Cuántos estudiantes reprobaron el curso 'Arquitectura De Software' (nota menor a 3.5)?\n")

        # Se filtran los registros que corresponden al curso seleccionado y tienen nota menor a la mínima aprobatoria
        estudiantes_reprobados_software = df_calificaciones_completas[
            (df_calificaciones_completas['nombre_curso'] == curso_software) &
            (df_calificaciones_completas['nota'] < nota_minima_aprobatoria)
        ]
        cantidad_estudiantes_reprobados_software = len(estudiantes_reprobados_software)
        print(f"   Cantidad de estudiantes que reprobaron '{curso_software}': {cantidad_estudiantes_reprobados_software}\n")

if __name__ == '__main__':
    print("***--- Análisis ---***")
    analisis_frecuencia()
    analisis_agregacion()
    analisis_filtrado()