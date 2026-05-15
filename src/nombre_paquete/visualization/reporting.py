from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


def summarize_tables(
    features: pd.DataFrame,
    edges: pd.DataFrame,
    classes: pd.DataFrame,
) -> dict[str, Any]:
    known_classes = classes[classes["class"] != "unknown"]
    class_distribution = known_classes["class"].astype(str).value_counts().to_dict()

    summary = {
        "features_shape": list(features.shape),
        "edges_shape": list(edges.shape),
        "classes_shape": list(classes.shape),
        "known_labels": int((classes["class"] != "unknown").sum()),
        "unknown_labels": int((classes["class"] == "unknown").sum()),
        "class_distribution_known": class_distribution,
        "n_duplicate_edges": int(edges.duplicated().sum()),
        "n_missing_classes": int(classes.isna().sum().sum()),
        "n_missing_edges": int(edges.isna().sum().sum()),
        "n_missing_features": int(features.isna().sum().sum()),
    }
    return summary


def summary_to_markdown(summary: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Reporte de Datos",
            "",
            "## Resumen general de los datos",
            f"- Features: {summary['features_shape'][0]} filas x {summary['features_shape'][1]} columnas.",
            f"- Edges: {summary['edges_shape'][0]} filas x {summary['edges_shape'][1]} columnas.",
            f"- Classes: {summary['classes_shape'][0]} filas x {summary['classes_shape'][1]} columnas.",
            "",
            "## Resumen de calidad de los datos",
            f"- Valores faltantes en features: {summary['n_missing_features']}.",
            f"- Valores faltantes en edges: {summary['n_missing_edges']}.",
            f"- Valores faltantes en classes: {summary['n_missing_classes']}.",
            f"- Aristas duplicadas: {summary['n_duplicate_edges']}.",
            "",
            "## Variable objetivo",
            f"- Etiquetas conocidas: {summary['known_labels']}.",
            f"- Etiquetas unknown: {summary['unknown_labels']}.",
            f"- Distribucion etiquetas conocidas: {summary['class_distribution_known']}.",
            "",
            "## Ranking de variables",
            "- En este entregable no se calcula un ranking supervisado definitivo.",
            "- Se mantiene el conjunto completo de 165 variables anonimizadas para modelamiento con GNN.",
        ]
    )


def write_json(data: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
