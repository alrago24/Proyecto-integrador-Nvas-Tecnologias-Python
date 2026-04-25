# 📚 Proyecto Integrador Python — Gestión Educativa
 
Proyecto de análisis de datos desarrollado en Python orientado a la gestión educativa. Permite cargar, limpiar y analizar información de usuarios, perfiles, cursos, estudiantes y calificaciones a partir de datasets en formato CSV.
 
---
 
## 🗂️ Estructura del proyecto
 
```
Proyecto-Integrador-Python/
│
├── data/
│   ├── row/                        # Datasets con datos sucios (entrada)
│   │   ├── usuarios_datos_sucios.csv
│   │   ├── perfiles_datos_sucios.csv
│   │   ├── cursos_datos_sucios.csv
│   │   └── calificaciones_datos_sucios.csv
│   │
│   └── proccesed/                  # Datasets limpios (salida)
│       ├── usuarios_limpios.csv
│       ├── perfiles_limpios.csv
│       ├── cursos_limpios.csv
│       ├── estudiantes_limpios.csv
│       └── calificaciones_limpias.csv
│
├── analisis.py                     # Análisis de frecuencia, agregación y filtrado
├── limpieza.py                     # Funciones de limpieza por dataset
├── carga.py                        # Funciones de carga de datasets
├── main.py                         # Menú principal del sistema
└── requirements.txt                # Dependencias del proyecto
```
 
---
 
## 📊 Datasets utilizados
 
| Dataset | Descripción |
|---|---|
| `usuarios` | Información personal de todos los usuarios del sistema |
| `perfiles` | Dirección y teléfono asociados a cada usuario |
| `cursos` | Cursos disponibles en la plataforma |
| `estudiantes` | Relación entre estudiantes y sus usuarios |
| `calificaciones` | Notas de cada estudiante por curso (escala 1.0 – 5.0) |
 
---
 
## ⚙️ Configuración del entorno
 
### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd Proyecto-Integrador-Python
```
 
### 2. Crear y activar el entorno virtual
```bash
# Crear entorno virtual
python -m venv .venv
 
# Activar en Windows
.venv\Scripts\activate
 
# Activar en Mac/Linux
source .venv/bin/activate
```
 
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
 
---
 
## ▶️ Ejecución
 
### Opción A — Ejecutar el sistema completo (menú interactivo)
```bash
python main.py
```
El menú permite realizar paso a paso la carga, limpieza y análisis de los datos:
```
1. Cargar datos
2. Limpiar datos
3. Guardar datos limpios
4. Análisis de Frecuencia
5. Análisis de Agregación
6. Análisis con Filtrado y Conteo
7. Salir
```
 
### Opción B — Ejecutar solo el análisis directamente
```bash
python analisis.py
```
Requiere que los datasets limpios ya estén disponibles en `./data/proccesed/`.
 
---
 
## 🔍 Análisis realizados
 
1. **Frecuencia** — Identifica el curso con mayor cantidad de calificaciones registradas y la cantidad de estudiantes por curso.
2. **Agregación** — Calcula la nota promedio y la edad promedio de los estudiantes agrupados por curso.
3. **Filtrado y Conteo** — Determina cuántos estudiantes aprobaron y reprobaron cada curso con base en una nota mínima aprobatoria de 3.5.
---
 
## 🛠️ Tecnologías utilizadas
 
- Python 3.13
- Pandas
- CSV
---
 
## 👤 Autores
- Alison Diaz
- Sergio Atehortua
- Yeisson Angel Ossa
- David Andrés Marín
 
Proyecto desarrollado como parte del programa **Técnica en Asistente de Desarrollo de Software** — Semestre III, Nuevas Tecnologías.