"""
Advent of Code 2015 - Day 11
"""

# %%
from pathlib import Path
import json
import re

HERE = Path(__file__).parent
# file = HERE / "example.json"
file = HERE / "input.json"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read()


# %%
print("=== Part 1 ===")
print(sum(int(x) for x in re.findall(r"-?\d+", DATA)))
# %%
def parse_object(ob):
    if isinstance(ob, dict):
        running_sum = 0
        for k, v in ob.items():
            running_sum += parse_object(v)
            if v == "red":
                return 0
        else:
            return running_sum
    elif isinstance(ob, list):
        running_sum = 0
        for el in ob:
            running_sum += parse_object(el)
        return running_sum
    elif isinstance(ob, str):
        return 0
    elif isinstance(ob, int):
        return ob
    else:
        raise(ValueError)


data = json.loads(DATA)
print("=== Part 2 ===")
print(parse_object(data))
# %%
