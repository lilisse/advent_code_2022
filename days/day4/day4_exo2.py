from pathlib import Path
from ..utils import CONSOLE, read_file
from .day4_exo1 import parse_input


def is_overlap(couple: dict[str, tuple[str, str]]) -> bool:
    one_min = int(couple["one"][0])
    one_max = int(couple["one"][1])
    two_min = int(couple["two"][0])
    two_max = int(couple["two"][1])

    one = list(range(one_min, one_max + 1))
    two = list(range(two_min, two_max + 1))

    toto = set(one) & set(two)

    if toto:
        return True

    return False


def how_many_overlapping(couples: list[dict[str, tuple[str, str]]]) -> int:
    res = 0
    for couple in couples:
        if is_overlap(couple):
            res +=1

    return res


def day4_exo2(path: Path) -> int:
    content = read_file(path)
    couples = parse_input(content)
    result = how_many_overlapping(couples)
    CONSOLE.print(f"[green underline]Day 4 Exo 2:[/green underline]\n\t{result}")
    return result
