# Definición de los datos

## Origen de los datos

Los datos provienen del **Elliptic Dataset**, un conjunto de datos públicos utilizado para la detección de transacciones ilícitas en la red de Bitcoin. Este dataset fue desarrollado a partir de información real de transacciones en blockchain, procesada y etiquetada por la empresa Elliptic en colaboración con instituciones académicas, con el fin de apoyar investigaciones en detección de fraude y lavado de dinero.

Los datos pueden obtenerse a través de la plataforma **Kaggle**, utilizando la herramienta `kagglehub` para descarga programática o descarga manual desde el repositorio correspondiente (`ellipticco/elliptic-data-set`).

## Especificación de los scripts para la carga de datos

El script principal de adquisición de datos se encuentra en:

```
scripts/data_acquisition/main.py
```

Este script realiza las siguientes operaciones:
1. Descarga del dataset desde Kaggle usando `kagglehub`.
2. Carga de los tres archivos CSV principales (features, edges, classes).
3. Mapeo de identificadores de transacciones a índices numéricos.
4. Limpieza de conexiones inválidas en el grafo.
5. Conversión de etiquetas a valores numéricos (1=ilícita, 0=legítima, -1=desconocida).
6. Alineación de datos entre features y classes.
7. Creación de tensores PyTorch (`X`, `y`, `edge_index`) para modelado con GNN.
8. Impresión de un resumen del dataset procesado.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

Los archivos fuente se descargan desde Kaggle y se almacenan localmente en la ruta proporcionada por `kagglehub`:

| Archivo | Ruta relativa | Descripción |
|---------|---------------|-------------|
| `elliptic_txs_features.csv` | `elliptic_bitcoin_dataset/` | Características numéricas de cada transacción (167 columnas) |
| `elliptic_txs_edgelist.csv` | `elliptic_bitcoin_dataset/` | Conexiones (aristas) entre transacciones |
| `elliptic_txs_classes.csv` | `elliptic_bitcoin_dataset/` | Etiquetas de clase para cada transacción |

### Estructura de los archivos de origen

- **Features (elliptic_txs_features.csv):** 203,769 filas × 167 columnas. Sin encabezado. Columna 0 = ID de transacción, Columna 1 = timestep, Columnas 2-166 = características numéricas (94 locales + 72 de agregación de vecinos).
- **Edges (elliptic_txs_edgelist.csv):** 234,355 filas × 2 columnas (`txId1`, `txId2`). Representa el flujo de Bitcoin entre transacciones.
- **Classes (elliptic_txs_classes.csv):** 203,769 filas × 2 columnas (`txId`, `class`). Valores posibles de clase: `"1"` (ilícita), `"2"` (legítima), `"unknown"`.

### Procedimientos de transformación y limpieza

TBD

### Base de datos de destino

TBD

### Resumen del dataset procesado

TBD
