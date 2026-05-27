# Análisis de Datos – Informe de Ventas Mensuales

Curso: **Cursor con Python: desarrollo inteligente con IA** — Santander Open Academy

Proyecto de análisis de datos desarrollado con Python, utilizando las bibliotecas `pandas` y `matplotlib`. Este script permite procesar un conjunto de datos de ventas (`ventas.csv`), limpiar la información, calcular métricas clave de negocio y visualizar los resultados mediante gráficos de barras. El proyecto forma parte del itinerario formativo del curso y pone en práctica los fundamentos del análisis de datos con Python.

## 🎯 Objetivos del Proyecto

Desarrollar un script automatizado que permita a los usuarios extraer información valiosa a partir de un archivo CSV de transacciones de ventas. 
El script realiza lo siguiente:
- ✅ **Carga y limpieza de datos:** Analiza fechas y asegura que las columnas de cantidad y precio sean numéricas.
- ✅ **Análisis temporal:** Calcula y muestra los ingresos totales agrupados por mes.
- ✅ **Análisis de productos:** Identifica el producto más vendido en unidades y el que genera más ingresos.
- ✅ **Visualización de datos:** Genera automáticamente gráficos en formato PNG para el informe.

## 🛠️ Stack Tecnológico

- **Python 3:** Lenguaje base para el script de análisis.
- **Pandas:** Biblioteca principal para manipulación, limpieza y agrupación de datos (DataFrames).
- **Matplotlib:** Herramienta para generar gráficos de barras y visualizar tendencias.
- **Git / GitHub:** Control de versiones y publicación del código.

## 📂 Estructura del Proyecto

```text
analisis_ventas/
├── analisis.py          # Script principal con la lógica de procesamiento y gráficos
├── ventas.csv           # Conjunto de datos de entrada (fuente de información)
├── requirements.txt     # Dependencias necesarias para ejecutar el proyecto
├── README.md            # Documentación del proyecto
├── ventas_por_mes.png   # Gráfico de salida (generado automáticamente)
└── top5_productos.png   # Gráfico de salida (generado automáticamente)
```

## 📊 Modelo de Datos y Lógica

El archivo `ventas.csv` contiene al menos las siguientes columnas:
- `fecha`: Fecha de la transacción (procesada como `datetime`).
- `producto`: Nombre o identificador del producto.
- `cantidad`: Unidades vendidas (forzado a tipo numérico entero).
- `precio`: Precio unitario (forzado a tipo numérico flotante).

En el flujo de ejecución, el script:
1. Crea la columna `mes` extrayendo el período de la fecha.
2. Agrupa por mes para obtener los ingresos (multiplicando `cantidad * precio`).
3. Crea la columna `ingreso` por transacción.
4. Agrupa por producto para obtener totales de volumen y dinero, encontrando los máximos con `idxmax()`.
5. Filtra el top 5 usando `nlargest()`.

## 🚀 Instalación y Ejecución Local

Para ejecutar el análisis en tu entorno local:

### 1. Clonar el repositorio:
```bash
git clone https://github.com/jltamayocabello-droid/py_analisis_ventas.git
cd py_analisis_ventas
```

### 2. Crear y activar el entorno virtual:
**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Git Bash) / Linux / macOS:**
```bash
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
# source venv/bin/activate    # Linux / macOS
```

### 3. Instalar dependencias:
```bash
pip install -r requirements.txt
```
*(Asegúrate de que `pandas` y `matplotlib` estén en tu archivo requirements.txt)*

### 4. Ejecutar el script:
```bash
python analisis.py
```

### 5. Resultados:
- Se imprimirán en la terminal (consola) los reportes de ventas y productos.
- Aparecerán ventanas interactivas con los gráficos correspondientes.
- Se guardarán en la carpeta los archivos `ventas_por_mes.png` y `top5_productos.png`.

## 💡 Decisiones de Diseño

### Coerción de Tipos de Datos
**Decisión:** Utilizar `pd.to_numeric(..., errors='coerce')` para las columnas de cantidad y precio.
**Justificación:** En conjuntos de datos del mundo real, es común encontrar errores de tipado o valores nulos. Esta aproximación convierte dichos errores en `NaN` (Not a Number), permitiendo que el análisis numérico continúe sin romper la ejecución del programa.

### Uso de dt.to_period('M')
**Decisión:** Extraer el año y mes en lugar de agrupar por fechas exactas.
**Justificación:** Agrupar los datos por período mensual es la norma para los informes financieros y de ventas, ya que estabiliza las métricas y permite descubrir tendencias a lo largo del tiempo de manera legible.

### Múltiples Gráficos en Script Secuencial
**Decisión:** Ejecutar los métodos `.plot()` de Matplotlib y hacer un único `plt.show()` al final del script.
**Justificación:** Evita que el usuario tenga que cerrar cada ventana de gráfico para que el script pueda continuar. Los gráficos se calculan, se guardan en el sistema de archivos como PNGs y, al final, se presentan todos juntos.

## 🔗 Repositorio GitHub
[https://github.com/jltamayocabello-droid/py_analisis_ventas](https://github.com/jltamayocabello-droid/py_analisis_ventas)

## ✒️ Autor
Jorge Tamayo Cabello

Desarrollador Front-End

## 📄 Licencia
Este proyecto es parte de un trabajo formativo del curso "Cursor con Python: desarrollo inteligente con IA" de Santander Open Academy y está disponible con fines educativos.