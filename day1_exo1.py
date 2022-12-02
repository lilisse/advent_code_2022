from pathlib import Path
from typing import Dict, List, Tuple
from decimal import Decimal

def read_file(path: Path) -> str:
    with open(Path.cwd() / path, 'r') as opened_file:
        content = opened_file.read()

    return content

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

content = read_file(Path("input/day1_exo1.txt"))
calories_by_elfs = parse_input(content)
result = get_the_most(calories_by_elfs)
print(result)
