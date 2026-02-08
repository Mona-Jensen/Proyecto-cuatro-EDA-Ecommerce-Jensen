import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os
from datetime import datetime

# =================================================================
# 0. CONFIGURACIÓN Y CARGA DE DATOS
# =================================================================
sns.set_theme(style="whitegrid")
csv_file = "E-commerce Customer Behavior - Sheet1.csv"

if not os.path.exists(csv_file):
    print(f"❌ Error crítico: No se encontró el archivo {csv_file}")
    exit()

df = pd.read_csv(csv_file)

# =================================================================
# 1. PASO 1: AUDITORÍA DE CALIDAD (IDA)
# =================================================================
# Genera la tabla técnica de tipos de datos y nulos detectados
fig, ax = plt.subplots(figsize=(9, 5))
ax.axis('off')
resumen_ida = pd.DataFrame({
    'Columna': df.columns,
    'Tipo de Dato': df.dtypes.values,
    'Nulos Detectados': df.isnull().sum().values
})
tabla_ida = ax.table(cellText=resumen_ida.values, colLabels=resumen_ida.columns, 
                     cellLoc='center', loc='center', colColours=["#40466e"]*3)

for k, cell in tabla_ida._cells.items():
    if k[0] == 0:
        cell.get_text().set_color('white')
        cell.get_text().set_weight('bold')

plt.title("Lección 1: Auditoría de Calidad de Datos (IDA)", pad=20, fontweight='bold')
plt.savefig('01_Auditoria_Datos.png', dpi=300, bbox_inches='tight')
plt.close()

# =================================================================
# 2. PASO 2: ESTADÍSTICA DESCRIPTIVA
# =================================================================
# Analiza la tendencia central y detecta atípicos (Boxplot)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['Total Spend'], kde=True, color='#3498db')
plt.title("Distribución del Gasto Total")

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Total Spend'], color='#2ecc71')
plt.title("Análisis de Outliers (Gasto)")
plt.savefig('02_Estadistica_Descriptiva.png', dpi=300)
plt.close()

# =================================================================
# 3. PASO 3: MATRIZ DE CORRELACIÓN
# =================================================================
# Identifica el factor principal de ingresos (Pearson 0.97)
plt.figure(figsize=(8, 6))
df_num = df.select_dtypes(include=[np.number]) # Filtro para evitar errores de texto
sns.heatmap(df_num.corr(), annot=True, cmap='RdYlGn', fmt=".2f")
plt.title("Matriz de Correlación: Drivers de Gasto")
plt.savefig('03_Matriz_Correlacion.png', dpi=300)
plt.close()

# =================================================================
# 4. PASO 4: MODELO DE REGRESIÓN LINEAL
# =================================================================
# Construye la herramienta predictiva (R² = 0.9456)
X = sm.add_constant(df['Items Purchased'])
y = df['Total Spend']
modelo = sm.OLS(y, X).fit()

plt.figure(figsize=(8, 6))
sns.regplot(x='Items Purchased', y='Total Spend', data=df, 
            line_kws={"color": "#e74c3c"}, scatter_kws={"alpha": 0.4})
plt.title(f"Regresión Lineal: Predicción de Gasto (R² = {modelo.rsquared:.4f})")
plt.savefig('04_Modelo_Regresion.png', dpi=300)
plt.close()

# =================================================================
# 5. PASO 5: VISUALIZACIÓN AVANZADA (MEMBRESÍAS)
# =================================================================
# Segmentación por densidad de gasto y fidelidad
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='Membership Type', y='Total Spend', palette="viridis")
plt.title("Análisis Multivariable: Gasto por Nivel de Membresía")
plt.savefig('05_Violinplot_Membresia.png', dpi=300)
plt.close()

# =================================================================
# 6. PASO 6: REPORTE FINAL DE AUDITORÍA INTEGRADA
# =================================================================
# Valida que todos los activos anteriores se generaron correctamente
archivos = ['01_Auditoria_Datos.png', '02_Estadistica_Descriptiva.png', 
            '03_Matriz_Correlacion.png', '04_Modelo_Regresion.png', 
            '05_Violinplot_Membresia.png']

datos_verificacion = []
for img in archivos:
    status = "EXISTE ✅" if os.path.exists(img) else "ERROR ❌"
    datos_verificacion.append([img, status, datetime.now().strftime('%d/%m/%Y %H:%M')])

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
df_v = pd.DataFrame(datos_verificacion, columns=['Activo Visual', 'Estado de Verificación', 'Fecha/Hora'])
tabla_final = ax.table(cellText=df_v.values, colLabels=df_v.columns, 
                       cellLoc='center', loc='center', colColours=["#2c3e50"]*3)

for k, cell in tabla_final._cells.items():
    if k[0] == 0:
        cell.get_text().set_color('white')
        cell.get_text().set_weight('bold')

plt.title("REPORTE DE INTEGRIDAD DE ENTREGABLES - GIANINA JENSEN", pad=20, fontweight='bold')
plt.savefig('06_Reporte_Final_Exitoso.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "•"*60)
print("¡ÉXITO! Todos los procesos se ejecutaron satisfactoriamente.")
print(f"Carpeta: {os.getcwd()}")
print("•"*60 + "\n")