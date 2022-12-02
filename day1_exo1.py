from pathlib import Path
from typing import Dict, List, Tuple
from decimal import Decimal
from utils import read_file, parse_input_day1, get_calories, CONSOLE

def get_the_most(elfs: Dict[str, List[str]]) -> Tuple[str, Decimal]:
    most_calories = 0
    winner = ""


    for elf, calories in elfs.items():
        calories_for_this_elf = get_calories(calories)

        if calories_for_this_elf > most_calories:
            most_calories = calories_for_this_elf
            winner = elf

    return (winner, most_calories)

def day1_exo1(path: Path):
    content = read_file(Path(path))
    calories_by_elfs = parse_input_day1(content)
    result = get_the_most(calories_by_elfs)
    CONSOLE.print(f"Day 1 Exo 1:\n\t{result}")
