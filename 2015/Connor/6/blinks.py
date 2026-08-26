# %%
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read().splitlines()

# %%
lights = np.zeros((1000,1000), dtype=bool)

def turn_on(x1, y1, x2, y2):
    lights[x1:x2+1, y1:y2+1] = True

def turn_off(x1, y1, x2, y2):
    lights[x1:x2+1, y1:y2+1] = False

def toggle(x1, y1, x2, y2):
    lights[x1:x2+1, y1:y2+1] = ~lights[x1:x2+1, y1:y2+1]

# %%
for line in DATA:
    if line.startswith("turn on"):
        _, _, start, _, end = line.split()
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        turn_on(x1, y1, x2, y2)
    elif line.startswith("turn off"):
        _, _, start, _, end = line.split()
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        turn_off(x1, y1, x2, y2)
    elif line.startswith("toggle"):
        _, start, _, end = line.split()
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        toggle(x1, y1, x2, y2)

print(np.sum(lights))

# %%
lights_p2 = np.zeros((1000,1000), dtype=int)

def turn_on_p2(x1, y1, x2, y2):
    lights_p2[x1:x2+1, y1:y2+1] += 1

def turn_off_p2(x1, y1, x2, y2):
    lights_p2[x1:x2+1, y1:y2+1] -= 1
    lights_p2[lights_p2 < 0] = 0

def toggle_p2(x1, y1, x2, y2):
    lights_p2[x1:x2+1, y1:y2+1] += 2
    lights_p2[lights_p2 < 0] = 0

for line in DATA:
    if line.startswith("turn on"):
        _, _, start, _, end = line.split()
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        turn_on_p2(x1, y1, x2, y2)
    elif line.startswith("turn off"):
        _, _, start, _, end = line.split()
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        turn_off_p2(x1, y1, x2, y2)
    elif line.startswith("toggle"):
        _, start, _, end = line.split()
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        toggle_p2(x1, y1, x2, y2)

print(np.sum(lights_p2))