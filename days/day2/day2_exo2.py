from ..utils import CONSOLE, read_file
from pathlib import Path
from typing import Dict, List


def parse_input(content: str) -> Dict[str, Dict[str, str]]:
    result = {}

    for idx, game in enumerate(content.split("\n"), start=1):
        game_data = game.split(" ")
        if game_data[0]:
            res = dict(opo=game_data[0], end=game_data[1])
            result[f"game_{idx}"] = res

    return result


def _get_score_for_symbol(symbol: str) -> int:
    """
    Opponent:
        - A: Rock
        - B: Paper
        - C: Scissors

    Me:
        - L: Rock
        - M: Paper
        - N: Scissors

    End:
        - X: Loose
        - Y: Draw
        - Z: Win
    """
    match symbol:
        case "X":
            return 0
        case "A" | "L":
            return 1
        case "B" | "M":
            return 2
        case "C" | "N" | "Y":
            return 3
        case "Z":
            return 6


def _get_hand(games: Dict[str, Dict[str, str]]):
    result = []

    for game in games.values():
        result.append(_get_hand_by_opo_and_end(game["end"], game["opo"]))

    return result


def _get_hand_by_opo_and_end(end: str, opo: str) -> str:
    """
    Opponent:
        - A: Rock
        - B: Paper
        - C: Scissors

    Me:
        - L: Rock
        - M: Paper
        - N: Scissors

    End:
        - X: Loose
        - Y: Draw
        - Z: Win
    """
    match opo:
        case "A":
            match end:
                case "X":
                    return "N"
                case "Y":
                    return "L"
                case "Z":
                    return "M"
        case "B":
            match end:
                case "X":
                    return "L"
                case "Y":
                    return "M"
                case "Z":
                    return "N"
        case "C":
            match end:
                case "X":
                    return "M"
                case "Y":
                    return "N"
                case "Z":
                    return "L"


def _get_hand_score(my_hands: List[str]) -> int:
    result = 0

    for hand in my_hands:
        result += _get_score_for_symbol(hand)

    return result


def _get_game_score(games: Dict[str, Dict[str, str]]) -> int:
    result = 0
    for game in games.values():
        result += _get_score_for_symbol(game["end"])

    return result


def _get_score(games: Dict[str, Dict[str, str]]) -> int:
    return _get_hand_score(_get_hand(games)) + _get_game_score(games)


def day2_exo2(path: Path) -> int:
    content = read_file(path)
    games = parse_input(content)
    score = _get_score(games)
    CONSOLE.print(f"[green underline]Day 2 Exo 2:[/green underline]\n\t{score}")
    return score
