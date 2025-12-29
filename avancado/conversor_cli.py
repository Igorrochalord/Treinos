"""Conversor avançado com interface de linha de comando e histórico em JSON."""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple

HISTORY_FILE = Path(__file__).with_name("conversion_history.json")

def _ensure_history_file() -> None:
    if not HISTORY_FILE.exists():
        HISTORY_FILE.write_text("[]", encoding="utf-8")


def _load_history() -> list[dict]:
    _ensure_history_file()
    try:
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def _save_history(history: list[dict]) -> None:
    HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")


LENGTH_FACTORS: Dict[str, float] = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.34,
    "ft": 0.3048,
}

def _convert_length(value: float, from_unit: str, to_unit: str) -> float:
    base = value * LENGTH_FACTORS[from_unit]
    return base / LENGTH_FACTORS[to_unit]


def _convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    if from_unit == "c":
        if to_unit == "f":
            return (value * 9 / 5) + 32
        if to_unit == "k":
            return value + 273.15
    if from_unit == "f":
        celsius = (value - 32) * 5 / 9
        return _convert_temperature(celsius, "c", to_unit)
    if from_unit == "k":
        celsius = value - 273.15
        return _convert_temperature(celsius, "c", to_unit)
    raise ValueError("Conversão de temperatura não suportada.")


TEMP_UNITS = {"c", "f", "k"}


def convert(value: float, from_unit: str, to_unit: str) -> Tuple[float, str]:
    lower_from, lower_to = from_unit.lower(), to_unit.lower()
    if lower_from in TEMP_UNITS and lower_to in TEMP_UNITS:
        return _convert_temperature(value, lower_from, lower_to), "temperatura"
    if lower_from in LENGTH_FACTORS and lower_to in LENGTH_FACTORS:
        return _convert_length(value, lower_from, lower_to), "comprimento"
    raise ValueError("As unidades devem pertencer à mesma categoria (temperatura ou comprimento).")


def log_conversion(record: dict) -> None:
    history = _load_history()
    history.append(record)
    _save_history(history)


def show_history(limit: int | None = None) -> None:
    history = _load_history()
    if not history:
        print("Sem histórico registrado.")
        return
    to_show = history[-limit:] if limit else history
    for item in to_show:
        print(f"[{item['timestamp']}] {item['value']} {item['from']} -> {item['result']:.4f} {item['to']} ({item['category']})")


def clear_history() -> None:
    _save_history([])
    print("Histórico limpo.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Conversor com histórico e múltiplas unidades.")
    parser.add_argument("value", type=float, nargs="?", help="Valor a ser convertido")
    parser.add_argument("from_unit", nargs="?", help="Unidade de origem (ex: C, F, K, m, km)")
    parser.add_argument("to_unit", nargs="?", help="Unidade de destino")
    parser.add_argument("--history", choices=["show", "clear"], help="Exibe ou limpa o histórico de conversões")
    parser.add_argument("--limit", type=int, default=None, help="Limite ao usar --history show")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.history == "clear":
        clear_history()
        return
    if args.history == "show":
        show_history(limit=args.limit)
        return
    if args.value is None or args.from_unit is None or args.to_unit is None:
        parser.error("Informe value, from_unit e to_unit ou use --history.")
    result, category = convert(args.value, args.from_unit, args.to_unit)
    print(f"{args.value} {args.from_unit} equivalem a {result:.4f} {args.to_unit} ({category}).")
    log_conversion(
        {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "value": args.value,
            "from": args.from_unit,
            "to": args.to_unit,
            "result": result,
            "category": category,
        }
    )


if __name__ == "__main__":
    main()
