from ..utils import CONSOLE, read_file
from typing import Dict, List
from pathlib import Path

MINUS_LOWER = 96
MINUS_UPPER = 38

def parse_input(content: str) -> Dict[str, Dict[str, str]]:
    result = {}

    for idx, bag in enumerate(content.split("\n"), start=1):
        res = {}
        if bag:
            bag_len = len(bag)
            res["one"] = bag[:bag_len//2]
            res["two"] = bag[bag_len//2:]
            result[f"bag_{idx}"] = res

    return result

def _get_weight(char: str):
    if char.isupper():
        return ord(char) - MINUS_UPPER
    else:
        return ord(char) - MINUS_LOWER

def _get_anomalies(bags: Dict[str, Dict[str, str]]):
    result = []

    for bag in bags.values():
        result.append(list(set(bag["one"])&set(bag["two"]))[0])

    return result

def get_all_weight(anomalies: List[str]) -> int:
    result = 0

    for ano in anomalies:
        result += _get_weight(ano)

    return result

def day3_exo1(path: Path) -> int:
    bags = parse_input(read_file(path))
    anomalies = _get_anomalies(bags)
    result = get_all_weight(anomalies)
    CONSOLE.print(f"[green underline]Day 3 Exo 1:[/green underline]\n\t{result}")
    return result
