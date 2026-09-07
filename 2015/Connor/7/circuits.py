"""Evaluate the circuit from Advent of Code 2015, Day 7.

Reads wire instructions from ``input.txt``, computes the signal on wire ``a``
for both puzzle parts, and prints the results. Part 2 replaces wire ``b`` with
the signal found for ``a`` in part 1.
"""

# %%
from pathlib import Path
from functools import cache

HERE = Path(__file__).parent
file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read().splitlines()
# %%
circuit = {}
for instruction in DATA:
    expression, name = instruction.split(" -> ")
    if "RSHIFT" in expression:
        circuit[name] = (
            ">>", expression.split(" RSHIFT ")[0], int(expression.split(" RSHIFT ")[1])
        )
    elif "LSHIFT" in expression:
        circuit[name] = (
            "<<", expression.split(" LSHIFT ")[0], int(expression.split(" LSHIFT ")[1])
        )
    elif "AND" in expression:
        circuit[name] = (
            "&", expression.split(" AND ")[0], expression.split(" AND ")[1]
        )
    elif "OR" in expression:
        circuit[name] = ("|", expression.split(" OR ")[0], expression.split(" OR ")[1])
    elif "NOT" in expression:
        circuit[name] = ("~", expression.split("NOT ")[1])
    else:
        try:
            circuit[name] = ("=", int(expression))
        except ValueError:
            circuit[name] = ("=", expression)


@cache
def get_value(wire):
    """Return the 16-bit signal produced by a wire and its dependencies."""
    operation = circuit[wire]
    operator = operation[0]
    if operator == ">>":
        return (get_value(operation[1]) >> operation[2]) & 0xFFFF
    elif operator == "<<":
        return (get_value(operation[1]) << operation[2]) & 0xFFFF
    elif operator == "&":
        try:
            return (get_value(operation[1]) & get_value(operation[2])) & 0xFFFF
        except KeyError:
            return (int(operation[1]) & get_value(operation[2])) & 0xFFFF
    elif operator == "|":
        return (get_value(operation[1]) | get_value(operation[2])) & 0xFFFF
    elif operator == "~":
        return ~get_value(operation[1]) & 0xFFFF
    else:
        try:
            return get_value(operation[1])
        except KeyError:
            return operation[1] & 0xFFFF

# %%
print("==================")
print("Part 1:")
print(get_value("a"))
print("==================")
# %%
circuit["b"] = ("=", get_value("a"))
get_value.cache_clear()
print("==================")
print("Part 2:")
print(get_value("a"))
print("==================")
