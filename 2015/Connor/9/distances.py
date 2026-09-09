# %%
import numpy as np
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).parent
# file = HERE / "example.txt"
file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read().splitlines()
# %%
distances = {}
for line in DATA:
    city_a = line.split()[0]
    city_b = line.split()[2]
    distance = int(line.split()[-1])
    try:
        distances[city_a][city_b] = distance
    except KeyError:
        distances[city_a] = {}
        distances[city_a][city_b] = distance
    try:
        distances[city_b][city_a] = distance
    except KeyError:
        distances[city_b] = {}
        distances[city_b][city_a] = distance

# %%
all_cities = list(distances.keys())
all_possible_routes = [p for p in permutations(all_cities) if p < p[::-1]]

# %%
def get_route_length(distances, route):
    distance = 0
    for i, current_city in enumerate(route):
        next_city = route[i+1]
        distance += distances[current_city][next_city]
        if i == len(route)-2:
            return distance

# %%
shortest_route = np.inf
for route in all_possible_routes:
    test_length = get_route_length(distances, route)
    if test_length < shortest_route:
        shortest_route = test_length

# %%
print("===Part 1===")
print(shortest_route)
# %%
longest_route = 0
for route in all_possible_routes:
    test_length = get_route_length(distances, route)
    if test_length > longest_route:
        longest_route = test_length

# %%
print("===Part 2===")
print(longest_route)
# %%
