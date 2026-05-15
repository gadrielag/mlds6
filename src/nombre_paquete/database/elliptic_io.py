from __future__ import annotations

import shutil
from pathlib import Path
from typing import Dict, Tuple

import pandas as pd

DATASET_ID = "ellipticco/elliptic-data-set"
CSV_FILES = {
    "features": "elliptic_txs_features.csv",
    "edges": "elliptic_txs_edgelist.csv",
    "classes": "elliptic_txs_classes.csv",
}


def resolve_dataset_dir(work_dir: Path) -> Path:
    """Resolve the directory that contains the Elliptic CSV files."""
    dataset_root = work_dir / "elliptic_bitcoin_dataset"
    if dataset_root.is_dir():
        return dataset_root
    return work_dir


def ensure_dataset_local(project_root: Path, output_dir: Path | None = None) -> Path:
    """Download and copy the Elliptic dataset into the project data folder."""
    try:
        import kagglehub
    except ImportError as exc:
        raise RuntimeError(
            "kagglehub no esta instalado. Instala dependencias con pip install -e ."
        ) from exc

    output_dir = output_dir or (project_root / "data" / "elliptic-data-set")
    output_dir.mkdir(parents=True, exist_ok=True)

    cache_dir = Path(kagglehub.dataset_download(DATASET_ID))
    shutil.copytree(cache_dir, output_dir, dirs_exist_ok=True)
    return resolve_dataset_dir(output_dir)


def dataset_paths(data_dir: Path) -> Dict[str, Path]:
    base = resolve_dataset_dir(data_dir)
    return {name: base / file_name for name, file_name in CSV_FILES.items()}


def load_raw_tables(data_dir: Path) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    paths = dataset_paths(data_dir)
    features = pd.read_csv(paths["features"], header=None)
    edges = pd.read_csv(paths["edges"])
    classes = pd.read_csv(paths["classes"])
    return features, edges, classes


def validate_raw_tables(
    features: pd.DataFrame,
    edges: pd.DataFrame,
    classes: pd.DataFrame,
) -> None:
    expected_cols = {
        "edges": {"txId1", "txId2"},
        "classes": {"txId", "class"},
    }

    if not expected_cols["edges"].issubset(edges.columns):
        raise ValueError("El archivo de aristas no tiene columnas txId1 y txId2")
    if not expected_cols["classes"].issubset(classes.columns):
        raise ValueError("El archivo de clases no tiene columnas txId y class")
    if features.shape[1] != 167:
        raise ValueError(
            f"Se esperaban 167 columnas de features y se obtuvieron {features.shape[1]}"
        )


def labeled_dataset(features: pd.DataFrame, classes: pd.DataFrame) -> pd.DataFrame:
    """Return merged features + labels only for known labels."""
    feat = features.rename(columns={0: "txId", 1: "timestep"}).copy()
    merged = feat.merge(classes, on="txId", how="inner")
    known = merged[merged["class"].isin(["1", "2", 1, 2])].copy()
    known["target_illicit"] = known["class"].astype(str).map({"1": 1, "2": 0}).astype(int)
    return known
