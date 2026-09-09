# %%
from pathlib import Path

HERE = Path(__file__).parent
# file = HERE / "example.txt"
file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read().splitlines()[0]

# %%
def look_and_say(s: str) -> str:
    output = ""
    current_digit = None
    for i, digit in enumerate(s):
        if current_digit is None:
            current_digit = digit
            count = 1
        elif current_digit == digit:
            count += 1
        else:
            output += str(count) + current_digit
            current_digit = digit
            count = 1

        if i == len(s) - 1:
            output += str(count) + current_digit

    return output

# %%
part1 = DATA
print("=== Part 1 ===")
for _ in range(40):
    part1 = look_and_say(part1)
print(len(part1))
# %%
print("=== Part 2 ===")
part2 = DATA
for _ in range(50):
    part2 = look_and_say(part2)
print(len(part2))