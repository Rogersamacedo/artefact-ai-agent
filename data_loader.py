"""Carregamento centralizado dos dados do desafio."""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

ARQUIVOS = {
    "products": "products.csv",
    "promotions": "promotions.csv",
    "customers": "customers.csv",
    "categories": "categories.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
}


def load_csv(dataset: str) -> list[dict[str, str]]:
    """Carrega um conjunto de dados autorizado a partir da pasta data."""
    if dataset not in ARQUIVOS:
        raise ValueError(f"Conjunto de dados não autorizado: {dataset}")

    nome_arquivo = ARQUIVOS[dataset]
    arquivos = list(DATA_DIR.glob(f"*{nome_arquivo}"))

    if len(arquivos) != 1:
        raise FileNotFoundError(
            f"Esperado exatamente um arquivo para {dataset}; "
            f"encontrados: {len(arquivos)}"
        )

    with arquivos[0].open(
        mode="r", encoding="utf-8-sig", newline=""
    ) as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def available_datasets() -> tuple[str, ...]:
    """Retorna os nomes dos conjuntos de dados permitidos."""
    return tuple(ARQUIVOS.keys())
