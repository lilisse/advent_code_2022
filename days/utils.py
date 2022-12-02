from pathlib import Path
from decimal import Decimal
from typing import List, Dict
from rich.console import Console

CONSOLE = Console()

def read_file(path: Path) -> str:
    with open(Path.cwd() / path, 'r') as opened_file:
        content = opened_file.read()

    return content
