from pathlib import Path

import pandas as pd

ARCHIVO_VENTAS = Path(__file__).parent / "ventas.csv"

df = pd.read_csv(ARCHIVO_VENTAS, parse_dates=["fecha"])

# Asegurar que cantidad y precio sean numéricos
df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
df["precio"] = pd.to_numeric(df["precio"], errors="coerce")

print("Tipos de datos (df.dtypes):")
print(df.dtypes)
print("-" * 30)

print(f"Registros: {len(df)}")
print(f"Meses distintos: {df['fecha'].dt.to_period('M').nunique()}")
print(df.head())

df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad'] * d['precio']).sum())
ventas_por_mes = ventas_por_mes.sort_index()

print("\nVentas por mes:")
print(ventas_por_mes)
