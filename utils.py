from pathlib import Path
from decimal import Decimal
from typing import List, Dict
from rich.console import Console

CONSOLE = Console()

def read_file(path: Path) -> str:
    with open(Path.cwd() / path, 'r') as opened_file:
        content = opened_file.read()

    return content

def parse_input_day1(content : str) -> Dict[str, List[str]]:
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
