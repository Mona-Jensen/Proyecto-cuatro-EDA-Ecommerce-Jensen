# Análisis de comportamiento de clientes de e-commerce

Proyecto académico de **Gianina Jensen Guzmán**. Reúne revisión de calidad, estadística descriptiva, visualización y un modelo de regresión lineal para estudiar la relación entre artículos comprados y gasto total.

[Ver portafolio profesional](https://github.com/Mona-Jensen/m-dulos)

## Trabajo desarrollado

1. Auditoría de tipos de datos y valores faltantes.
2. Exploración de la distribución del gasto y valores atípicos.
3. Matriz de correlación de variables numéricas.
4. Ajuste de una regresión lineal mediante statsmodels.
5. Comparación visual del gasto según membresía.
6. Generación de seis entregables gráficos y un informe.

## Archivos

- [Código Python](Analisis_Predictivo_Ecommerce_Jensen.py).
- [Informe del análisis](Informe_Final_Análisis_de_Comportamiento_y_Predicción_de_Ventas.pdf).
- [Conjunto de datos utilizado](E-commerce%20Customer%20Behavior%20-%20Sheet1.csv).
- Seis imágenes PNG con las salidas del trabajo.

## Tecnologías

Python, pandas, NumPy, Seaborn, Matplotlib y statsmodels.

## Ejecución aislada

Para conservar intactos los entregables originales, copiar el script y el CSV a una carpeta local `scratch/ejecucion/`. Desde esa carpeta, usar un entorno con las dependencias instaladas y ejecutar:

```bash
python Analisis_Predictivo_Ecommerce_Jensen.py
```

El script escribe seis archivos PNG en su directorio de trabajo. En un entorno sin pantalla puede utilizarse el backend no interactivo de Matplotlib mediante `MPLBACKEND=Agg`.

## Hallazgos de la entrega original

La documentación registra dos valores faltantes en satisfacción, una correlación aproximada de 0,97 entre artículos comprados y gasto, y un R² de 0,9456. Estos valores no se volvieron a calcular durante la revisión del portafolio.

**R² describe el ajuste del modelo a los datos utilizados; no es un porcentaje de acierto predictivo.** El código ajusta OLS con el conjunto completo y no incorpora separación entrenamiento/prueba ni validación cruzada. Por tanto, no acredita desempeño con clientes nuevos ni una relación causal.

## Próximas mejoras técnicas

Documentar la procedencia y licencia del dataset, separar un conjunto de evaluación, medir error fuera de muestra y registrar las versiones de dependencias para facilitar la reproducción.
