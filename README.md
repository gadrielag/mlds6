# Team Data Science Project Template

Repositorio del proyecto aplicado de MLDS para la Entrega 1, enfocado en entendimiento del negocio, carga de datos y diccionario de datos del dataset Elliptic.

## Estructura

- `src/nombre_paquete`: codigo fuente de adquisicion y soporte de reportes.
- `scripts`: punto de entrada de la fase actual (adquisicion de datos).
- `docs`: documentacion de entregables en formato markdown.
- `data`: almacenamiento local del dataset y reportes generados.

## Requisitos

1. Python 3.10 o superior.
2. Credenciales de Kaggle configuradas para descarga automatica con `kagglehub`.

## Instalacion

```bash
pip install -e .
```

## Ejecucion por etapas

```bash
python scripts/data_acquisition/main.py
```

## Resultado esperado

- Dataset en `data/elliptic-data-set`.
- Resumen de adquisicion en `data/reports/acquisition_summary.json`.
- Diccionario y marco de negocio diligenciados en `docs/`.

## Referencia metodologica

La implementacion de esta rama esta recortada al alcance de Entrega 1 de acuerdo con las instrucciones oficiales (carga de datos, marco de proyecto y diccionario).
