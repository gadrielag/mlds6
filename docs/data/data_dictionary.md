# Diccionario de datos

## Tabla 1: Features (elliptic_txs_features.csv)

Contiene las características numéricas de cada transacción de Bitcoin en el grafo. Cada fila representa un nodo (transacción) con 167 columnas: un identificador, un timestep y 165 características numéricas divididas en locales y de agregación.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| Columna 0 (txId) | Identificador único de la transacción | int | Enteros positivos (ej: 230425980) | Elliptic Dataset (Kaggle) |
| Columna 1 (timestep) | Paso temporal al que pertenece la transacción (49 timesteps en total) | int | 1 - 49 | Elliptic Dataset (Kaggle) |
| Columnas 2-94 (local features) | 93 características locales de la transacción (número de inputs/outputs, fees, volumen, etc.). Los nombres están anonimizados | float | Valores numéricos continuos (normalizados) | Elliptic Dataset (Kaggle) |
| Columnas 95-166 (aggregated features) | 72 características de agregación obtenidas de los vecinos directos del nodo en el grafo (estadísticas como media, desviación estándar, etc.) | float | Valores numéricos continuos (normalizados) | Elliptic Dataset (Kaggle) |

- **Dimensiones totales:** 203,769 filas × 167 columnas
- **Nota:** Los nombres de las características están anonimizados por razones de confidencialidad del proveedor de datos.

## Tabla 2: Edges (elliptic_txs_edgelist.csv)

Contiene las conexiones dirigidas entre transacciones, representando el flujo de Bitcoin de una transacción a otra. Cada fila es una arista del grafo.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| txId1 | ID de la transacción origen (nodo fuente) | int | Enteros positivos correspondientes a IDs de transacciones | Elliptic Dataset (Kaggle) |
| txId2 | ID de la transacción destino (nodo destino) | int | Enteros positivos correspondientes a IDs de transacciones | Elliptic Dataset (Kaggle) |

- **Dimensiones totales:** 234,355 filas × 2 columnas
- **Nota:** Representa un grafo dirigido donde la dirección indica el flujo de Bitcoin.

## Tabla 3: Classes (elliptic_txs_classes.csv)

Contiene las etiquetas de clasificación para cada transacción, indicando si es ilícita, legítima o desconocida.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| txId | Identificador único de la transacción | int | Enteros positivos correspondientes a IDs de transacciones | Elliptic Dataset (Kaggle) |
| class | Etiqueta de clasificación de la transacción | string/int | `"1"` (ilícita), `"2"` (legítima), `"unknown"` (sin etiqueta) | Elliptic Dataset (Kaggle) |

- **Dimensiones totales:** 203,769 filas × 2 columnas