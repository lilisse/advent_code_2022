from pathlib import Path
from typing import Dict, List, Tuple
from decimal import Decimal
from ..utils import read_file, CONSOLE
from .day1_exo1 import get_the_most, parse_input


def day1_exo2(path: Path) -> Decimal:
    content = read_file(Path(path))
    calories_by_elfs = parse_input(content)
    result = Decimal("0")

    for i in range(3):
        res = get_the_most(calories_by_elfs)
        calories_by_elfs.pop(res[0])
        result += res[1]

    CONSOLE.print(f"[green underline]Day 1 Exo 2:[/green underline]\n\t{result}")
    return result
