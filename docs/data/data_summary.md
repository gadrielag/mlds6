# Reporte de Datos

Este documento resume la exploración inicial del dataset Elliptic, utilizado para detección de transacciones ilícitas en Bitcoin.

## Resumen general de los datos

- Fuente: Kaggle (`ellipticco/elliptic-data-set`).
- Tablas principales:
	- `elliptic_txs_features.csv`: 203,769 filas x 167 columnas.
	- `elliptic_txs_edgelist.csv`: 234,355 filas x 2 columnas.
	- `elliptic_txs_classes.csv`: 203,769 filas x 2 columnas.
- Unidad de análisis: transacción de Bitcoin (nodo en grafo dirigido).
- Estructura temporal: 49 timesteps.

## Resumen de calidad de los datos

- Valores faltantes: no se esperan faltantes estructurales en las columnas principales del dataset oficial.
- Duplicados: se verifica el conteo de aristas duplicadas en la etapa EDA (`scripts/eda/main.py`).
- Consistencia de esquema:
	- `features`: 167 columnas (id + timestep + 165 features anonimizadas).
	- `edges`: columnas `txId1`, `txId2`.
	- `classes`: columnas `txId`, `class`.

## Variable objetivo

- Variable original: `class`.
- Valores posibles:
	- `1`: transacción ilícita.
	- `2`: transacción lícita.
	- `unknown`: sin etiqueta.
- Para entrenamiento supervisado se usan solo etiquetas conocidas (`1` y `2`), mapeando:
	- ilícita -> 1
	- lícita -> 0

## Variables individuales

- Las 165 variables explicativas están anonimizadas por el proveedor.
- Se combinan características locales y agregadas del vecindario del nodo.
- Por diseño del problema, se prioriza modelamiento relacional (GNN) sobre interpretación directa de cada feature.

## Ranking de variables

- En esta fase no se define ranking definitivo por feature.
- Se utiliza el set completo de variables para preservar la señal estructural en el modelo de grafos.

## Relación entre variables explicativas y variable objetivo

- El comportamiento de fraude depende tanto de atributos del nodo como de su contexto topológico.
- Por esta razón, el pipeline utiliza snapshots temporales de grafo y no solo análisis tabular estático.
- La relación se evalúa de forma indirecta mediante desempeño del modelo GCN (accuracy, precision, recall y F1).
