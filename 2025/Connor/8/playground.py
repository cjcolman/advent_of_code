# %%
import numpy as np
from itertools import combinations

# %%
def parse_input(filepath):
    with open(filepath) as f:
        lines = [tuple(int(j) for j in i.split(",")) for i in f.read().split("\n")]
        return lines

# %%
def get_euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** 0.5

# %%
class LowArray:
    def __init__(self, n):
        self.array = [(np.inf, [], []) for i in range(n)]

    def insert(self, element):
        if element[0] <= self.array[-1][0]:
            self.array.pop(-1)
            self.array.append(element)
            self.array = sorted(self.array, key=lambda x: x[0])

# %%
def get_n_nearest_pairs(lines, n):
    nearest_n = LowArray(n)
    for point1, point2 in combinations(lines, 2):
        nearest_n.insert((get_euclidean_distance(point1, point2), point1, point2))
    return nearest_n.array

# %%
def get_all_nearest_pairs(lines):
    nearest_pairs = []
    for point1, point2 in combinations(lines, 2):
        nearest_pairs.append((get_euclidean_distance(point1, point2), point1, point2))
    nearest_pairs = sorted(nearest_pairs, key=lambda x: x[0])
    return nearest_pairs

# %%
def get_circuits(array):
    circuits = []
    for element in array:
        point1, point2 = element[1], element[2]
        for circuit in circuits:
            if point1 in circuit or point2 in circuit:
                circuit.add(point1)
                circuit.add(point2)
                break
        else:
            new_circuit = set([point1, point2])
            circuits.append(new_circuit)
    return circuits

# %%
def combine_circuits(circuits):
    merged = True
    while merged:
        merged = False
        for i in range(len(circuits)):
            for j in range(i + 1, len(circuits)):
                if circuits[i].intersection(circuits[j]):
                    circuits[i] = circuits[i].union(circuits[j])
                    del circuits[j]
                    merged = True
                    break
            if merged:
                break
    return circuits

# %%
def get_answer(circuits):
    lengths = sorted([len(circuit) for circuit in circuits],reverse=True)
    return lengths[0] * lengths[1] * lengths[2]

# %%
lines = parse_input("example.txt")
nearest_pairs = get_n_nearest_pairs(lines, 10)
circuits = get_circuits(nearest_pairs)
combined_circuits = combine_circuits(circuits)
print("Part 1 Example:" , get_answer(combined_circuits), "Expected 40")
# %%
lines = parse_input("input.txt")
nearest_pairs = get_n_nearest_pairs(lines, 1000)
circuits = get_circuits(nearest_pairs)
combined_circuits = combine_circuits(circuits)
print("Part 1:" , get_answer(combined_circuits))
# %%
lines = parse_input("input.txt")
nearest_pairs = get_n_nearest_pairs(lines, 7000)
circuits = get_circuits(nearest_pairs)
combined_circuits = combine_circuits(circuits)
print(len(combined_circuits))
print(len(combined_circuits[0]))

# %%
last_one_in = set(lines).difference(combined_circuits[0]).pop()

# %%
def get_answer_part_2(lines, last_one_in):
    min = np.inf
    for point in lines:
        if point != last_one_in:
            distance  = get_euclidean_distance(point, last_one_in)
            if distance < min:
                min = distance
                closest_point = point
    return last_one_in[0] * closest_point[0]
# %%
print("Part 2:", get_answer_part_2(lines, last_one_in))
# %%
