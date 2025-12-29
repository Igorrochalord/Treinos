"""Relatório parecido com o "GitHub lines" mostrando contagem de linhas por arquivo."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable


def iter_python_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.py"):
        if path.is_file():
            yield path


def contar_linhas(arquivo: Path) -> int:
    with arquivo.open(encoding="utf-8") as handler:
        return sum(1 for _ in handler)


def gerar_relatorio(root: Path) -> None:
    total = 0
    print("Arquivo | Linhas")
    print("-" * 40)
    for arquivo in sorted(iter_python_files(root)):
        linhas = contar_linhas(arquivo)
        total += linhas
        rel = arquivo.relative_to(root)
        print(f"{rel} -> {linhas}")
    print("-" * 40)
    print(f"Total de linhas Python: {total}")


if __name__ == "__main__":
    BASE = Path(__file__).resolve().parents[1]
    gerar_relatorio(BASE)
