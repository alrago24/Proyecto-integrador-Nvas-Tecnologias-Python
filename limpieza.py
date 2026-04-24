import pandas as pd
import numpy as np

# David
def limpiar_usuarios(df_usuarios):
    #Limpieza de espacio y texto en formato titulo.
    print('Limpieza de espacio y texto en formato titulo')
    df_usuarios['nombre'] = df_usuarios['nombre'].str.strip().str.title()
    df_usuarios['apellido'] = df_usuarios['apellido'].str.strip().str.title()
    df_usuarios['email'] = df_usuarios['email'].str.strip().str.lower()

    #Eliminar datos duplicados
    print('Eliminar datos duplicados')
    df_usuarios = df_usuarios.drop_duplicates()

    print('Reemplazar datos con un valor')
    #Reemplazar datos con un valor
    df_usuarios['edad'] = df_usuarios['edad'].replace('veinte', 20)
    df_usuarios['edad'] = df_usuarios['edad'].replace('-5', 20)
    df_usuarios['edad'] = df_usuarios['edad'].replace('150', 20)
    df_usuarios['edad'] = pd.to_numeric(df_usuarios['edad'], errors='coerce').fillna(0).astype(int)


    print('Tratamiento de Nulos')
    #Tratamiento de Nulos
    df_usuarios['edad'] = df_usuarios['edad'].fillna(df_usuarios['edad'].mean())
    df_usuarios['edad'] = df_usuarios['edad'].replace(0, df_usuarios['edad'].mean())

    # index=False evita guardar el índice de Pandas en el archivo
    df_usuarios.to_csv('data/proccesed/usuarios_limpios.csv', index=False)