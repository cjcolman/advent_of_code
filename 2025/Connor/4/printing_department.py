# %%
def parse_input(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
# %%
def is_box_accessible(box_coord, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # Up, Down, Left, Right, Diagonals
    x, y = box_coord
    adjacent_boxes = 0
    for direction in directions:
        dx, dy = direction
        if x + dx < 0 or x + dx >= len(grid) or y + dy < 0 or y + dy >= len(grid[0]):
            continue
        else:
            if grid[x + dx][y + dy] == '@':
                adjacent_boxes += 1
    return adjacent_boxes < 4
     
# %%
def count_accessible_boxes(grid, mode='draw'):
    grid_copy = [list(row) for row in grid]
    accessible_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@' and is_box_accessible((i, j), grid):
                accessible_count += 1
                if mode == 'draw':
                    grid_copy[i][j] = 'X'  # Mark as counted
                if mode == 'remove':
                    grid_copy[i][j] = '.'  # Mark as removed
    grid_copy = [''.join(row) for row in grid_copy]
    return accessible_count, grid_copy

# %%
def draw_grid(grid):
    for row in grid:
        print(row)

# %%
accessible_count, updated_grid = count_accessible_boxes(parse_input('example.txt'))
print("Example Test Case: ", accessible_count, " (Expected: 13)")
draw_grid(updated_grid)

accessible_count, updated_grid = count_accessible_boxes(parse_input('input.txt'))
print("Part 1: ", accessible_count)
draw_grid(updated_grid)

# %%
def run_until_no_accessible_boxes(grid):
    current_grid = grid
    total_accessible = 0
    while True:
        accessible_count, updated_grid = count_accessible_boxes(current_grid, mode='remove')
        if accessible_count == 0:
            break
        total_accessible += accessible_count
        current_grid = updated_grid
    return total_accessible, current_grid

# %%
total_accessible, final_grid = run_until_no_accessible_boxes(parse_input('input.txt'))
print("Part 2: ", total_accessible)
draw_grid(final_grid)
# %%
