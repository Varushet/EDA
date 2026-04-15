# EDA W40K - Memoria del Análisis Exploratorio de Datos

## Resumen General

Este análisis exploratorio de datos (EDA) examina una colección de miniaturas de Warhammer 40K (946 registros), libros de lore (234 registros), estadísticas de facciones (28 registros) y datos del mercado 3D (10 registros). El objetivo es probar múltiples hipótesis sobre las relaciones entre miniaturas, facciones, precios, poder y lore.

---

## Obtención de Datos

La recopilación de datos para este análisis exploratorio presentó múltiples desafíos. Los datos provienen de diversas fuentes, incluyendo páginas web oficiales, foros de la comunidad y gráficos publicados en redes sociales. Para integrar esta información:

- **Web Scraping**: Se utilizó scraping para extraer datos de tablas y listas en páginas web.
- **Procesamiento Manual**: Algunos datos, como los obtenidos de gráficos, tuvieron que ser transcritos manualmente.
- **Imágenes**: Se descargaron imágenes relevantes para complementar el análisis.

A continuación, se presenta una tabla con los DataSets disponibles en la carpeta `data`:

| Archivo            | Descripción                                         | Método de Obtención | Fuentes                                                                                                                                             |
| ------------------ | --------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| DS_Models.csv      | Información sobre modelos.                          | Limpieza            | https://www.kaggle.com/datasets/theredmage/warhammer-40k?spm=a2ty_o01.29997173.0.0.36d75171zRtsw0&select=Wahapedia+Data+Export+-+DS_Model+Costs.csv |
| DS_Model_Costs.csv | Costos asociados a los modelos.                     | Limpieza            | https://www.kaggle.com/datasets/theredmage/warhammer-40k?spm=a2ty_o01.29997173.0.0.36d75171zRtsw0&select=Wahapedia+Data+Export+-+DS_Model+Costs.csv |
| faction_own.csv    | Estadísticas de facciones.                          | Descarga de img     | Comunidad de jugadores                                                                                                                              |
| precios_of.csv     | Precios oficiales de productos.                     | Web Scraping        | https://www.warhammer.com/es-ES/shop/warhammer-40000                                                                                                |
| prices.csv         | Precios recopilados de diversas fuentes.            | PDF to CSV          | https://es.scribd.com/document/435486621/price-list                                                                                                 |
| Win_Rate.csv       | Tasas de victoria por facción.                      | descarga de img     | Estadísticas de torneos.                                                                                                                            |
| lore_books.csv     | Libros de historia.                                 | Web Scraping        | https://wh40k.lexicanum.com/wiki/List_of_Novels                                                                                                     |
| print3d_market.csv | Estudio de tendencias del mercado de impresoras 3d. | Descarga de img     | https://www.grandviewresearch.com/horizon/outlook/3d-printing-market-size/global                                                                    |

---

## DataSet Limpios

| Dataset                      | Registros | Columnas |
| ---------------------------- | --------- | -------- |
| Miniaturas (df_mini)         | 946       | 11       |
| Libros de Lore (df_lore)     | 234       | 7        |
| Stats Facciones (df_faction) | 28        | 12       |
| Mercado 3D (df_market)       | 10        | 2        |

---

## Hipótesis Analizadas

### HIPÓTESIS 1: Relación entre venta de Impresoras 3D y figuras

- **Pregunta**: ¿Existe relación entre el mercado de impresoras 3D y la cantidad/precio de miniaturas?
- **Método**: Correlación de Pearson entre tamaño del mercado 3D (EUR) y cantidad/precio de miniaturas por año
- **Resultado**:
  - Correlación Mercado 3D ↔ Cantidad Miniaturas: **-0.834** (correlación negativa fuerte)
  - Correlación Mercado 3D ↔ Precio Medio: **-0.275**
- **Conclusión**: Existe una correlación negativa significativa entre el crecimiento del mercado 3D y la producción de miniaturas oficiales, acentuada en los 3 ultimos años, pero faltan datos para establecer una causalidad.

---

### HIPÓTESIS 2: Probabilidad de renovación de facción

- **Pregunta**: ¿Qué probabilidad hay de que tu facción favorita sea renovada?
- **Método**: Score heurístico basado en frecuencia histórica, recencia y soporte de ediciones
- **Top 5 Facciones con Mayor Probabilidad**:
  1. Space Marines
  2. Necrons
  3. Orks
  4. Craftworlds
  5. Astra Militarum
- **Bottom 5**:
  1. Inquisition
  2. Supplement Marines
  3. Harlequins
  4. Imperial Assassins
  5. Ynnari

---

### HIPÓTESIS 3: Soporte de facciones

- **Pregunta**: ¿Qué facciones reciben más soporte?
- **Métricas**: Cantidad de miniaturas, precio promedio, índice de soporte, win rate
- **Top 5 por Índice de Soporte**:
  1. Space Marines (78.00)
  2. Necrons (66.61)
  3. Orks (57.92)
  4. Craftworlds (54.85)
  5. Astra Militarum (53.73)
- **Test estadístico**: Diferencia significativa en win rate entre top y bottom facciones

---

### HIPÓTESIS 4: Predicción de eventos del Lore

- **Pregunta**: ¿Se pueden predecir acontecimientos del Lore en base a las colecciones de figuras?
- **Método**: Correlación Pearson entre libros de lore y miniaturas por facción y año
- **Correlaciones Intra-facción destacadas**:
  - Tau Empire: r=1.00 (significativa)
  - Dark Angels: r=0.56 (no significativa)
  - Space Wolves: r=0.47 (no significativa)
- **Análisis adicional**: Matrices de correlación inter-facción e intra-facción sobre stats de juego
- **Conclusión**: Solo Tau Empire muestra correlación significativa; la mayoría de facciones no muestran relación clara entre lore y miniaturas

---

### HIPÓTESIS 5: Balance del Juego

- **Pregunta**: ¿Está balanceado el juego entre facciones?
- **Análisis**: Distribución de win rates, fuerza relativa entre facciones
- **Resultado**: Se analizó el balance general del juego mediante estadísticas competitivas

---

### HIPÓTESIS 6: Relación poder-precio

- **Pregunta**: ¿Existe relación entre el poder de una figura y su precio? ¿Se puede predecir?
- **Método**: Correlación y regresión lineal entre 'cost' (proxy de poder) y 'price'
- **Resultado**:
  - Correlación Poder ↔ Precio: **0.742** (fuerte correlación positiva)
  - Modelo: Precio = 27.82 + 0.24 × Cost
  - R² del modelo: **0.551**
- **Conclusión**: Existe una relación fuerte entre poder y precio; el modelo explica ~55% de la variabilidad

---

### HIPÓTESIS 7: Lore y Precio

- **Pregunta**: ¿Existe relación entre la cantidad de lore y el precio de las figuras?
- **Método**: Correlación entre cantidad de libros por facción/año y precio medio
- **Resultado**: Se realizó test estadístico de Pearson entre libros y precio

---

### HIPÓTESIS 8: Power Creep Analysis

- **Pregunta**: ¿Las miniaturas nuevas son "más fuertes por el mismo costo"?
- **Métrica clave**: "Eficiencia de Poder" = cost / price
- **Análisis por década**:

| Década | Cost Mean | Price Mean | Power Efficiency Mean |
| ------ | --------- | ---------- | --------------------- |
| 1990   | 114.36    | 52.25      | 2.18                  |
| 2000   | 118.62    | 58.12      | 1.97                  |
| 2010   | ...       | ...        | ...                   |

- **Análisis adicional**:
  - Tendencia de power creep por año
  - Análisis de creep por rol de miniatura
  - Heatmap de power creep por facción
  - Detección de outliers

---

### HIPÓTESIS 9: Value Efficiency Analysis

- **Pregunta**: ¿Pagamos por plástico o por marca?
- **Métrica clave**: "Precio por mm²" (value efficiency)
- **Método**: Cálculo del área de base (asumiendo base circular) y precio por unidad de área
- **Datos válidos**: 771 miniaturas
- **Estadísticas de Precio por mm²**:
  - Media: 0.04
  - Mediana: 0.04
  - Std: 0.03
  - Rango: 0.00 - 0.12
- **Análisis adicional**: Heatmap de eficiencia por tamaño de facción

---

### HIPÓTESIS 13: Primary Players y Soporte

- **Pregunta**: ¿Las facciones con más jugadores "Primary" tienen mejor soporte?
- **Análisis**: Relación entre número de jugadores primarios por facción y métricas de soporte

---

## Visualizaciones Generadas

1. `hipotesis_1_market_analysis.png` - Análisis del mercado 3D vs miniaturas
2. `hipotesis_2_renewal_probability.png` - Probabilidad de renovación por facción
3. `hipotesis_3_faction_support.png` - Soporte por facción
4. `hipotesis_4_correlation_matrix.png` - Matriz de correlación
5. `hipotesis_4_inter_faction_corr.png` - Correlación inter-facción
6. `hipotesis_4_intra_faction_corr.png` - Correlación intra-facción
7. `hipotesis_4_space_marines_sync.png` - Sincronización Space Marines
8. `hipotesis_5_game_balance.png` - Balance del juego
9. `hipotesis_6_power_price.png` - Relación poder-precio
10. `hipotesis_7_lore_price.png` - Relación lore-precio
11. `hipotesis_8_creep_by_role.png` - Power creep por rol
12. `hipotesis_8_efficiency_analysis.png` - Análisis de eficiencia
13. `hipotesis_8_faction_creep_heatmap.png` - Heatmap power creep por facción
14. `hipotesis_8_power_creep_trend.png` - Tendencia de power creep
15. `hipotesis_9_heatmap_faction_size.png` - Heatmap por tamaño de facción

---

## Tecnologías Utilizadas

- **Python**: pandas, numpy, scipy, scikit-learn
- **Visualización**: matplotlib, seaborn
- **Estadística**: Correlación Pearson, regresión lineal, test T
