import pandas as pd

def cargaUsuarios():
    df_usuarios = pd.read_csv('./data/row/usuarios_datos_sucios.csv')
    df_usuarios.info()
    return df_usuarios

def cargaPerfiles():
    df_perfiles = pd.read_csv('./data/row/perfiles_datos_sucios.csv')
    df_perfiles.info()
    return df_perfiles

def cargaCursos():
    df_cursos = pd.read_csv('./data/row/cursos_datos_sucios.csv')
    df_cursos.info()
    return df_cursos

def cargaCalificaciones():
    df_calificaciones = pd.read_csv('./data/row/calificaciones_datos_sucios.csv')
    df_calificaciones.info()
    return df_calificaciones

def cargaEstudiantes():
    df_estudiantes = pd.read_csv('./data/proccesed/estudiantes_limpios.csv')
    return df_estudiantes