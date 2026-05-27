from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Definir la ruta del archivo CSV (asumiendo que está en el mismo directorio que este script)
ARCHIVO_VENTAS = Path(__file__).parent / "ventas.csv"

# Cargar los datos del CSV y convertir la columna 'fecha' a tipo datetime
df = pd.read_csv(ARCHIVO_VENTAS, parse_dates=["fecha"])

# Asegurar que cantidad y precio sean numéricos (convierte errores a NaN)
df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
df["precio"] = pd.to_numeric(df["precio"], errors="coerce")

print("Tipos de datos (df.dtypes):")
print(df.dtypes)
print("-" * 30)

# Mostrar información básica del conjunto de datos cargado
print(f"Registros: {len(df)}")
print(f"Meses distintos: {df['fecha'].dt.to_period('M').nunique()}")
print(df.head())

# --- Cálculo de ventas totales por mes ---
# Extraer solo el año y el mes de la fecha en una nueva columna
df['mes'] = df['fecha'].dt.to_period('M')

# Agrupar por mes y sumar el producto de cantidad por precio
ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad'] * d['precio']).sum())

# Ordenar cronológicamente
ventas_por_mes = ventas_por_mes.sort_index()

print("\nVentas por mes:")
print(ventas_por_mes)

# --- Análisis de productos (más vendido vs mayores ingresos) ---
# Calcular el ingreso por cada transacción
df['ingreso'] = df['cantidad'] * df['precio']

# Agrupar por producto y sumar tanto la cantidad total como el ingreso total
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
})

# Identificar qué producto tiene el valor máximo en cada categoría
mas_vendido = ventas_prod['cantidad'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()

print(f"\nProducto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad']})")
print(f"Producto con mayores ingresos: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f} €)")

# --- Gráfico de Ventas por Mes ---
# Convertir el índice (Period) a string para un mejor manejo en matplotlib
ventas_por_mes.index = ventas_por_mes.index.astype(str)

plt.figure(figsize=(6,4))
ventas_por_mes.plot(kind='bar')

plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas (€)")
plt.tight_layout()

# Guardar el gráfico en un archivo PNG
plt.savefig(Path(__file__).parent / "ventas_por_mes.png")

# --- Gráfico de Top 5 Productos por Ingresos ---
top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(6,4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos (€)")
plt.xlabel("Producto")
plt.tight_layout()

plt.savefig(Path(__file__).parent / "top5_productos.png")
plt.show()
