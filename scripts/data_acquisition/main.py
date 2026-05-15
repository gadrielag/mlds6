from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
	sys.path.insert(0, str(SRC_PATH))

from nombre_paquete.database import ensure_dataset_local, load_raw_tables, validate_raw_tables
from nombre_paquete.visualization import summarize_tables, write_json


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Descarga y valida el dataset Elliptic.")
	parser.add_argument(
		"--project-root",
		type=Path,
		default=Path.cwd(),
		help="Ruta raiz del proyecto.",
	)
	parser.add_argument(
		"--output-dir",
		type=Path,
		default=None,
		help="Ruta de salida para guardar una copia local del dataset.",
	)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	project_root = args.project_root.resolve()

	output_dir = args.output_dir
	if output_dir is not None:
		output_dir = output_dir.resolve()

	data_dir = ensure_dataset_local(project_root=project_root, output_dir=output_dir)
	features, edges, classes = load_raw_tables(data_dir)
	validate_raw_tables(features, edges, classes)

	summary = summarize_tables(features, edges, classes)
	report_path = project_root / "data" / "reports" / "acquisition_summary.json"
	write_json(summary, report_path)

	print(f"Dataset local en: {data_dir}")
	print(f"Reporte de adquisicion en: {report_path}")


if __name__ == "__main__":
	main()
