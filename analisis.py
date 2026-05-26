from pathlib import Path

import pandas as pd

ARCHIVO_VENTAS = Path(__file__).parent / "ventas.csv"

df = pd.read_csv(ARCHIVO_VENTAS, parse_dates=["fecha"])

print(f"Registros: {len(df)}")
print(f"Meses distintos: {df['fecha'].dt.to_period('M').nunique()}")
print(df.head())
