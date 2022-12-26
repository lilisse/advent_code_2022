from pathlib import Path
from .day3_exo1 import get_all_weight
from ..utils import read_file, CONSOLE
from typing import List, Dict


def parse_input(content: str) -> List[str]:
    result = []

    for bag in content.split("\n"):
        if bag:
            result.append(bag)

    return result


def _get_badge(group: List[str]) -> str:
    return list(set(group[0]) & set(group[1]) & set(group[2]))[0]


def _get_badges(bags: List[str]) -> List[str]:
    begin = 0
    end = 3
    result = []

    while end <= len(bags):
        result.append(_get_badge(bags[begin:end]))
        begin += 3
        end += 3

    return result


def day3_exo2(path: Path) -> int:
    bags = parse_input(read_file(path))
    badges = _get_badges(bags)
    result = get_all_weight(badges)
    CONSOLE.print(f"[green underline]Day 3 Exo 2:[/green underline]\n\t{result}")
    return result
