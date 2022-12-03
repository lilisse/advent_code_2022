from ..utils import CONSOLE, read_file
from pathlib import Path
from typing import Dict

def parse_input(content: str) -> Dict[str, Dict[str, str]]:
    result = {}

    for idx, game in enumerate(content.split("\n"), start=1):
        game_data = game.split(" ")
        if game_data[0]:
            res = dict(opo=game_data[0], me=game_data[1])
            result[f"game_{idx}"] = res

    return result

def _get_score_for_symbol(symbol: str) -> int:
    """
    Opponent:
        - A: Rock
        - B: Paper
        - C: Scissors

    Me:
        - X: Rock
        - Y: Paper
        - Z: Scissors
    """
    match symbol:
        case "X" | "A":
            return 1
        case "Y" | "B":
            return 2
        case "Z" | "C":
            return 3

def _get_hand_score(games: Dict[str, Dict[str, str]]) -> int:
    result = 0

    for game in games.values():
        result += _get_score_for_symbol(game["me"])

    return result

def _get_game_score(games: Dict[str, Dict[str, str]]) -> int:
    result = 0


    for game in games.values():
        opo_hand = _get_score_for_symbol(game["opo"])
        me_hand = _get_score_for_symbol(game["me"])

        if opo_hand == 1 and me_hand == 3:
            pass

        elif (me_hand > opo_hand) or (me_hand == 1 and opo_hand == 3):
            result += 6

        elif opo_hand == me_hand:
            result += 3

    return result


def _get_score(games: Dict[str, Dict[str, str]]):
    return _get_hand_score(games) + _get_game_score(games)

def day2_exo1(path: Path) -> int:
    content = read_file(path)
    games = parse_input(content)
    score = _get_score(games)
    CONSOLE.print(f"[green underline]Day 2 Exo 1:[/green underline]\n\t{score}")
    return score
