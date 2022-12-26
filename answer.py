from days import (
    day1_exo1,
    day1_exo2,
    day2_exo1,
    day2_exo2,
    day3_exo1,
    day3_exo2,
    day4_exo1,
    day4_exo2,
)
from pathlib import Path
from art import text2art, art

print(text2art("Advent  of  Code  2022"))
day1_exo1(Path("input/day1.txt"))
day1_exo2(Path("input/day1.txt"))
day2_exo1(Path("input/day2.txt"))
day2_exo2(Path("input/day2.txt"))
day3_exo1(Path("input/day3.txt"))
day3_exo2(Path("input/day3.txt"))
day4_exo1(Path("input/day4.txt"))
day4_exo2(Path("input/day4.txt"))
