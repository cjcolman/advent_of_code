import itertools
from collections import defaultdict

print("Part 1:")
print("==============================")

input_filepath = "./input_08.txt"
example_filepath = "./example_08.txt"
example_filepath_2 = "./example_08_2.txt"

def get_frequency_dict(filepath):
    grid = open(filepath).read().split("\n")
    freq_dict = defaultdict(set)
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter != ".":
                freq_dict[letter].add((i,j))
    grid_size = (len(grid), len(grid[0]))

    return freq_dict, grid_size

def get_antinode(coord_1, coord_2):
    diff_i = coord_1[0] - coord_2[0]
    diff_j = coord_1[1] - coord_2[1]
    antinode_coord_1 = (coord_1[0] + diff_i, coord_1[1] + diff_j)
    antinode_coord_2 = (coord_2[0] - diff_i, coord_2[1] - diff_j)
    return antinode_coord_1, antinode_coord_2

def get_antinode_part_2(coord_1, coord_2, grid_size):
    diff_i = coord_1[0] - coord_2[0]
    diff_j = coord_1[1] - coord_2[1]
    antinode_set = set()
    current_antinode = coord_1
    while is_coord_in_grid(current_antinode, grid_size):
        current_antinode = (current_antinode[0] + diff_i, current_antinode[1] + diff_j)
        antinode_set.add(current_antinode)
    current_antinode = coord_1
    while is_coord_in_grid(current_antinode, grid_size):
        current_antinode = (current_antinode[0] - diff_i, current_antinode[1] - diff_j)
        antinode_set.add(current_antinode)
    return antinode_set

def is_coord_in_grid(coord, grid_size):
    return (0 <= coord[0] < grid_size[0]) and (0 <= coord[1] < grid_size[1])

def get_all_antinodes(filepath, part_2=False):
    freq_dict, grid_size = get_frequency_dict(filepath)
    antinode_set = set([])
    for letter, coords in freq_dict.items():
        coord_combos = itertools.permutations(coords, 2)
        for coord_combo in coord_combos:
            if not part_2:
                antinodes = get_antinode(coord_combo[0], coord_combo[1])
            else:
                antinodes = get_antinode_part_2(coord_combo[0], coord_combo[1], grid_size)

            for antinode in antinodes:
                if (0 <= antinode[0] < grid_size[0]) and (0 <= antinode[1] < grid_size[1]):
                    antinode_set.add(antinode)
    draw_grid(grid_size, antinode_set)
    return antinode_set

def draw_grid(grid_size, antinode_set):
    grid = [["." for j in range(grid_size[1])] for i in range(grid_size[0])]
    for antinode in antinode_set:
        grid[antinode[0]][antinode[1]] = "#"
    for row in grid:
        print(''.join(row))
            
        

print("Example: ", len(get_all_antinodes(example_filepath)), "\n\n")
print("Input solution: ", len(get_all_antinodes(input_filepath)))
print("==============================")

print("Part 2:")
print("==============================")
print("Example: ", len(get_all_antinodes(example_filepath, True)), "\n\n")
print("Input solution: ", len(get_all_antinodes(input_filepath, True)))
print("Example 2: ", len(get_all_antinodes(example_filepath_2, True)), "\n\n")