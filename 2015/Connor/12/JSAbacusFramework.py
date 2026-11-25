"""
Advent of Code 2015 - Day 11
"""

# %%
from pathlib import Path
import json
import re

HERE = Path(__file__).parent
file = HERE / "input.json"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read()


# %%
print("=== Part 1 ===")
print(sum(int(x) for x in re.findall(r"-?\d+", DATA)))
# %%
def parse_object(ob):
    pass
    