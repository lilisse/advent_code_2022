from pathlib import Path
from typing import Dict, List, Tuple
from decimal import Decimal
from utils import read_file, CONSOLE

def parse_input(content : str) -> Dict[str, List[str]]:
    content_by_line = content.split("\n\n")
    result = {}
    for idx, calories in enumerate(content_by_line, start=1):
        res = []
        for cal in calories.split("\n"):
            if cal:
                res.append(cal)
        result[f"elf_{idx}"] = res

    return result

def get_calories(calories):
    result = Decimal('0')
    for cal in calories:
        result += Decimal(cal)

    return result


def get_the_most(elfs: Dict[str, List[str]]) -> Tuple[str, Decimal]:
    most_calories = 0
    winner = ""

    for elf, calories in elfs.items():
        calories_for_this_elf = get_calories(calories)

        if calories_for_this_elf > most_calories:
            most_calories = calories_for_this_elf
            winner = elf

    return (winner, most_calories)

def day1_exo1(path: Path) -> Tuple[str, Decimal]:
    content = read_file(Path(path))
    calories_by_elfs = parse_input(content)
    result = get_the_most(calories_by_elfs)
    CONSOLE.print(f"Day 1 Exo 1:\n\t{result}")
