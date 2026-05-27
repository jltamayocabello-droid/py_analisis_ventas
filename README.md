# 📊 Sales Analyzer — Informe de Ventas Mensuales

![Estado del Proyecto](https://img.shields.io/badge/Estado-Completado-success)
![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Pandas%20%7C%20Matplotlib-blue)
![Análisis](https://img.shields.io/badge/Datos-CSV%20%7C%20Estad%C3%ADsticas-orange)
![Gráficos](https://img.shields.io/badge/Visualizaci%C3%B3n-Matplotlib%20%7C%20PNG-brightgreen)

**Curso:** [Cursor con Python: desarrollo inteligente con IA](https://www.santanderopenacademy.com/) — **Santander Open Academy**

---

# Descripción del proyecto

Script de automatización y análisis de datos en **Python** diseñado para procesar, limpiar y visualizar métricas de negocio a partir de un conjunto de transacciones históricas en formato CSV (`ventas.csv`). 

El proyecto calcula de forma autónoma ingresos por mes, clasifica los productos de mayor impacto estratégico y exporta informes visuales automáticos en formato de alta resolución. Forma parte del itinerario formativo del curso y pone en práctica la manipulación avanzada de datos estructurados con la suite científica de Python.

---

### 🎯 Objetivos del Proyecto

El principal objetivo es construir un pipeline de análisis de datos robusto y portable que automatice las siguientes tareas:
* ✅ **Ingesta y Limpieza Coercitiva:** Cargar transacciones comerciales y mitigar errores de formatos e inconsistencias tipográficas.
* ✅ **Análisis de Tendencias Temporales:** Cuantificar la evolución económica del negocio en intervalos agrupados de carácter mensual.
* ✅ **Identificación de Hitos comerciales:** Determinar de manera precisa qué productos lideran la facturación y cuáles dominan el volumen de unidades.
* ✅ **Generación de Reportes Gráficos:** Exportar de forma desatendida las representaciones visuales para la toma de decisiones empresariales.

---

### 📋 Cumplimiento de los Objetivos del Módulo

Este proyecto cumple rigurosamente con los objetivos de desarrollo de scripts y análisis de datos del módulo:

* ✅ **Manipulación y Limpieza con Pandas:** Uso avanzado de DataFrames, transformaciones de tipo (`pd.to_numeric` con coerción) e indexación temporal.
* ✅ **Agrupaciones y Métricas:** Cálculos estadísticos compuestos y agregaciones complejas usando `.groupby()` y métodos de selección vectorial como `.idxmax()` y `.nlargest()`.
* ✅ **Visualización Científica con Matplotlib:** Parametrización de figuras, configuración de lienzos y personalización de ejes gráficos.
* ✅ **Gestión Agnóstica del Entorno:** Integración de la biblioteca estándar `pathlib` para asegurar la portabilidad del script e impedir fallos por rutas absolutas hardcoded en distintos sistemas operativos.
* ✅ **Control de Calidad del Dato:** Gestión inteligente de valores nulos o corruptos (`NaN`) para garantizar que la ejecución no se interrumpa ante datos del mundo real.

---

### 🛠️ Stack Tecnológico

* **Python 3:** Lenguaje y motor de ejecución del script de procesamiento.
* **Pandas:** Biblioteca clave para el filtrado, manipulación, limpieza y estructuración de los DataFrames.
* **Matplotlib:** Motor gráfico de nivel profesional encargado de modelar, maquetar y exportar las visualizaciones.
* **Pathlib:** Módulo estándar de Python para la resolución dinâmica de rutas en sistemas Unix y Windows.
* **Git / GitHub:** Control de versiones distribuido y almacenamiento remoto de la base del código.

---

### 📂 Estructura del Proyecto

```text
analisis_ventas/
│
├── analisis.py          # Script principal con la lógica de procesamiento, limpieza y visualización
├── ventas.csv           # Conjunto de datos histórico (transacciones en formato CSV)
├── requirements.txt     # Dependencias necesarias para reproducir el entorno (Pandas, Matplotlib)
├── README.md            # Documentación completa del proyecto (este archivo)
│
├── ventas_por_mes.png   # Gráfico generado: Evolución histórica de ingresos por mes (PNG)
└── top5_productos.png   # Gráfico generado: Top 5 de productos con mayor facturación (PNG)
```

---

### 📊 Modelo de Datos y Lógica

#### 1. Ingesta de Datos (`ventas.csv`)
La aplicación espera un archivo de datos tabulares con la siguiente estructura de columnas:

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `fecha` | `datetime64[ns]` | Registro temporal de la transacción comercial (Formato: YYYY-MM-DD) |
| `producto` | `object` | Identificador único o denominación comercial del artículo (ej. A, B, C, D) |
| `cantidad` | `float64` / `int64` | Volumen unitario vendido en la transacción (filtrado coercitivo) |
| `precio` | `float64` | Tarifa unitaria aplicada en euros (filtrado coercitivo) |

#### 2. Lógica del Pipeline y Métricas Clave
Durante la ejecución del script `analisis.py`, se calculan y exponen las siguientes métricas de rendimiento:

| Métrica Calculada | Expresión / Lógica en Pandas | Objetivo Estratégico |
| :--- | :--- | :--- |
| **Ingreso por Línea** | `df['cantidad'] * df['precio']` | Determinar el importe total acumulado en cada transacción particular. |
| **Ventas por Período** | `df.groupby(df['fecha'].dt.to_period('M'))` | Segmentar las ganancias del negocio agrupándolas por mes/año natural de forma cronológica. |
| **Producto Líder en Volumen** | `ventas_prod['cantidad'].idxmax()` | Detectar el producto con mayor volumen de rotación en el almacén (unidades vendidas). |
| **Producto Líder en Valor** | `ventas_prod['ingreso'].idxmax()` | Detectar la referencia estrella del catálogo comercial (mayor impacto financiero). |
| **Top 5 de Facturación** | `ventas_prod.nlargest(5, 'ingreso')` | Listar jerárquicamente los cinco productos de mayor rendimiento económico. |

---

### 📊 Características Clave del Script

| Característica | Descripción |
| :--- | :--- |
| 🧹 **Limpieza Inteligente** | Convierte de forma automática caracteres corruptos, celdas vacías o tipos erróneos a `NaN` mediante `errors='coerce'`, evitando excepciones críticas. |
| 📅 **Segmentación Temporal** | Utiliza `to_period('M')` para agrupar ventas mensuales de forma consistente, la práctica estándar para reportes corporativos y financieros. |
| 🥇 **Productos Estrella** | Identifica en un solo paso las referencias críticas del catálogo de manera discriminada por volumen y por margen de ingresos. |
| 📈 **Doble Reporte Visual** | Exporta gráficos de barras optimizados para presentaciones de negocio en formato de imagen de alta resolución PNG. |
| 📂 **Rutas Relativas Dinámicas** | Implementa `Path(__file__).parent` para que el script pueda ser ejecutado desde cualquier directorio sin romper los enlaces de archivos. |

---

### 🚀 Instalación y Ejecución Local

Sigue los pasos a continuación para preparar tu entorno e iniciar el análisis de ventas en tu máquina local:

#### 1. Clonar el repositorio
```bash
git clone https://github.com/jltamayocabello-droid/py_analisis_ventas.git
cd py_analisis_ventas
```

#### 2. Configurar el Entorno Virtual

> [!TIP]
> El uso de un entorno virtual garantiza que las bibliotecas científicas utilizadas no interfieran con otras dependencias instaladas en tu sistema global.

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Windows (Git Bash), Linux o macOS:**
```bash
python -m venv venv
source venv/Scripts/activate   # Para Git Bash en Windows
# source venv/bin/activate     # Para Linux / macOS
```

#### 3. Instalar Dependencias
Instala los paquetes necesarios definidos en el archivo de requerimientos:
```bash
pip install -r requirements.txt
```

#### 4. Ejecutar el Script de Análisis
Lanza el flujo automatizado:
```bash
python analisis.py
```

#### 5. Resultados Obtenidos:
* **En Consola:** Visualizarás de forma secuencial la verificación de tipos de datos (`dtypes`), el número total de registros cargados con éxito, la matriz consolidada de ventas mensuales y el podio de los productos líderes.
* **En el Sistema de Archivos:** Se generarán (o actualizarán si ya existen) dos archivos en formato de imagen: `ventas_por_mes.png` y `top5_productos.png`.
* **En Pantalla:** Se abrirá una interfaz gráfica interactiva de Matplotlib mostrando los gráficos generados para su exploración inmediata.

---

### 💡 Decisiones de Diseño

#### Coerción de Tipos de Datos con `errors='coerce'`
* **Decisión:** Emplear `pd.to_numeric(df['columna'], errors='coerce')` para las variables de `cantidad` y `precio`.
* **Justificación:** Los datos de transacciones reales suelen contener imperfecciones, entradas de texto accidental o campos nulos. Esta estrategia transforma de forma segura los valores defectuosos en `NaN`, permitiendo computar estadísticas matemáticas limpias sin detener de manera súbita el script de producción.

#### Agrupamiento Temporal con `dt.to_period('M')`
* **Decisión:** Extraer el año y mes para el agrupamiento en lugar de utilizar fechas exactas del calendario.
* **Justificación:** La agrupación mensual estabiliza las fluctuaciones diarias no representativas, permitiendo identificar patrones estacionales e incrementos reales de rendimiento mensual, siendo el estándar en reportes analíticos de negocio.

#### Cierre y Persistencia de Gráficos Secuenciales
* **Decisión:** Dibujar y persistir las figuras con `plt.savefig()` de forma inmediata y postergar la llamada de bloqueo `plt.show()` al final del script.
* **Justificación:** Evita la experiencia de usuario molesta donde el script se detiene de forma indefinida esperando a que el operador cierre manualmente la primera ventana gráfica antes de poder procesar, guardar y pintar el segundo diagrama de la ejecución.

#### Portabilidad nativa con Pathlib
* **Decisión:** Utilizar `Path(__file__).parent` de la librería estándar `pathlib` para la resolución de rutas de lectura y escritura.
* **Justificación:** Previene errores fatales de "Archivo no encontrado" (`FileNotFoundError`) causados por llamadas desde terminales abiertas en directorios raíz diferentes al del script o al ejecutar el código en diferentes entornos operativos (Windows vs Unix).

---

### 🧪 Testing Manual y Verificación de Resultados

Para asegurar que todo funcione correctamente y que la integridad de tus datos está a salvo, realiza los siguientes chequeos tras ejecutar el script:

1. **Activación de Entorno:** Cerciórate de que tu prompt de consola tenga el prefijo del entorno virtual activo `(venv)`.
2. **Carga Completa:** La terminal debe imprimir en primera instancia los tipos de datos correctos e indicar que se han procesado exitosamente la totalidad de registros históricos (`Registros: 265`).
3. **Impresión de Métricas:** Valida que la terminal devuelva la tabla estructurada con los periodos mensuales y sus ingresos en euros sin valores indeterminados.
4. **Almacenamiento de Gráficos:** Comprueba que en la raíz del proyecto aparezcan con la marca de tiempo actual los archivos físicos `ventas_por_mes.png` y `top5_productos.png`.
5. **Rendimiento Visual:** Confirma que el gráfico de "Top 5 Productos" muestre una distribución ordenada de barras y que el eje de ordenadas represente correctamente los ingresos monetarios.
6. **Ventanas Interactivas:** Asegúrate de que las ventanas de interfaz de usuario de Matplotlib emerjan de forma conjunta e independiente, permitiendo realizar zooms interactivos antes de finalizar.

---

### 📚 Recursos y Referencias

* [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
* [Guía de Uso de Matplotlib](https://matplotlib.org/stable/users/index.html)
* [Manipulación de rutas con Pathlib (Python Docs)](https://docs.python.org/3/library/pathlib.html)
* [Markdown Guide — Sintaxis Extendida](https://www.markdownguide.org/)
* Repositorio del Gestor de Tareas de Referencia: [gestor_tareas](https://github.com/jltamayocabello-droid/gestor_tareas)

---

## ✒️ Autor

**Jorge Tamayo Cabello**

_Desarrollador Front-End_

---

## 📄 Licencia

Este proyecto es parte de un trabajo formativo del curso **"Cursor con Python: desarrollo inteligente con IA"** de **Santander Open Academy** y está disponible únicamente con fines educativos y de demostración técnica.

---

## 🙏 Agradecimientos

* **Santander Open Academy** por la excelente oportunidad de formación y desarrollo continuo en ecosistemas de Python e Inteligencia Artificial aplicada.
* **Pandas Development Team** y **Matplotlib Core Devs** por brindar herramientas analíticas de código abierto excepcionalmente potentes y flexibles.
* **Comunidad Python** por mantener la documentación y recursos libres accesibles a desarrolladores en crecimiento.