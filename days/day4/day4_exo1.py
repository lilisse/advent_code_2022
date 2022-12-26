from ..utils import CONSOLE, read_file
from pathlib import Path


def parse_input(content: str) -> list[dict[str, tuple[str, str]]]:
    result = []
    couples = content.split("\n")

    for couple in couples:
        if couple:
            res = {}
            tmp_cou = couple.split(",")
            tmp_part_one = tmp_cou[0].split("-")
            tmp_part_two = tmp_cou[1].split("-")
            res["one"] = (tmp_part_one[0], tmp_part_one[1])
            res["two"] = (tmp_part_two[0], tmp_part_two[1])
            result.append(res)

    return result


def is_full_range(couple: dict[str, tuple[str, str]]) -> bool:
    """
    {one: ('2', '4'), two: ('6', '8')}

    {one: ('6', '6'), two: ('4', '6')}

    {one: ('2', '8'), two: ('3', '7')}
    """
    one_min = int(couple["one"][0])
    one_max = int(couple["one"][1])
    two_min = int(couple["two"][0])
    two_max = int(couple["two"][1])

    one = list(range(one_min, one_max + 1))
    two = list(range(two_min, two_max + 1))

    if set(one).issuperset(two) or set(two).issuperset(one):
        return True

    return False


def how_many_is_full_range(couples: list[dict[str, tuple[str, str]]]) -> int:
    res = 0
    for couple in couples:
        if is_full_range(couple):
            res += 1

    return res


def day4_exo1(path: Path) -> int:
    content = read_file(path)
    couples = parse_input(content)
    result = how_many_is_full_range(couples)
    CONSOLE.print(f"[green underline]Day 4 Exo 1:[/green underline]\n\t{result}")
    return result
