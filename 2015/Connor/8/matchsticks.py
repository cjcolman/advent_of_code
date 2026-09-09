"""Advent of Code 2025, Day 8: Matchsticks"""
# %%
from pathlib import Path
import re

HERE = Path(__file__).parent
# file = HERE / "example.txt"
file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read().splitlines()

# %%
def get_num_mem_chars(line):
    """Return the number of characters represented in memory for a string literal."""
    newline = line.replace(r"\\", ".")
    newline = newline.replace(r"\"", ".")
    newline = re.sub(r"\\x[0-9a-fA-F]{2}", ".", newline)
    return len(newline)-2

# %%
def get_summed_differences_p1(lines):
    """Sum the difference between literal length and memory length for part 1."""
    total = 0
    for line in lines:
        total += len(line) - get_num_mem_chars(line)
    return total

# %%
def encoded_string_len(line):
    """Return the encoded length of a string literal for part 2."""
    newline = line.replace("\"", r"..")
    newline = newline.replace("\\", r"..")
    return len(newline) + 2

# %%
def get_summed_differences_p2(lines):
    """Sum the difference between encoded length and literal length for part 2."""
    total = 0
    for line in lines:
        total += encoded_string_len(line) - len(line)
    return total

# %%
print("=== Part 1 ===")
print(get_summed_differences_p1(DATA))
print("=== Part 2 ===")
print(get_summed_differences_p2(DATA))

# %%
