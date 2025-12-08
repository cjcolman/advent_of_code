# %%
import functools

def parse_input(filepath):
    grid = {}
    with open(filepath, 'r') as file:
        data = [line.strip() for line in file.readlines()]
        for i in range(len(data)):
            for j in range(len(data[0])):
                grid[i + 1j*j] = data[i][j]
                if data[i][j] == 'S':
                    start_coord = i + 1j*j
    return grid, start_coord

from frozendict import frozendict

def freezeargs(func):
    """Convert a mutable dictionary into immutable.
    Useful to be compatible with cache
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        args = (frozendict(arg) if isinstance(arg, dict) else arg for arg in args)
        kwargs = {k: frozendict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapped

# %%
def render_grid(cells: dict[complex, str], empty: str = " ") -> str:
    """
    Render a grid stored as {y + x*i: symbol} into a multiline string.
    
    - real part = y (row, top→bottom)
    - imag part = x (column, left→right)
    """
    if not cells:
        return ""

    ys = [int(z.real) for z in cells.keys()]   # rows
    xs = [int(z.imag) for z in cells.keys()]   # cols

    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)

    lines = []
    for y in range(min_y, max_y + 1):          # top → bottom
        row_chars = []
        for x in range(min_x, max_x + 1):
            z = complex(y, x)
            row_chars.append(str(cells.get(z, empty)))
        lines.append("".join(row_chars))

    return "\n".join(lines)


# %%
def propogate_tachyon_count_splits(filepath):
    number_of_splits = 0
    grid, start_coord = parse_input(filepath)
    max_row = max(z.real for z in grid.keys())
    cell_queue = [start_coord]
    while cell_queue:
        current_cell = cell_queue.pop(-1)
        next_cell = current_cell + 1
        try:
            if grid[next_cell] == ".":
                cell_queue.append(next_cell)
                grid[next_cell] = '|'
            elif grid[next_cell] == "|":
                pass
            elif grid[next_cell] == '^':
                number_of_splits += 1
                for direction in (-1j, 1j):
                    split_cell = next_cell + direction
                    if grid[split_cell] == ".":
                        cell_queue.append(split_cell)
                        grid[split_cell] = '|'
                    elif grid[split_cell] == "|":
                        pass
        except KeyError:
            pass

    return grid, number_of_splits

# %%
grid, splits = propogate_tachyon_count_splits("example.txt")
print(render_grid(grid))
print("Part 1 Example:", splits, "Expected: 21")
# %%
grid, splits = propogate_tachyon_count_splits("input.txt")
print(render_grid(grid))
print("Part 1 Input:", splits)


# %%
@freezeargs
@functools.cache
def count_paths(solved_grid, current_cell):
    max_row = max(z.real for z in solved_grid.keys())
    max_col = max(z.imag for z in solved_grid.keys())
    next_cell = current_cell + 1
    if next_cell.imag < 0 or next_cell.imag > max_col:
        return 0
    if next_cell.real == max_row:
        return 1
    if solved_grid[next_cell] == "." or solved_grid[next_cell] == "|":
        return count_paths(solved_grid, next_cell)
    elif solved_grid[next_cell] == '^':
        return count_paths(solved_grid, next_cell -1j) + count_paths(solved_grid, next_cell +1j)

# %%
_, start_coord = parse_input("example.txt")
grid, splits= propogate_tachyon_count_splits("example.txt")
num_paths = count_paths(grid, start_coord)
print(render_grid(grid))
print("Part 2 Example:", num_paths, "Expected: 40") 

# %%
_, start_coord = parse_input("input.txt")
grid, splits = propogate_tachyon_count_splits("input.txt")
num_paths = count_paths(grid, start_coord)
print(render_grid(grid))
print("Part 2 Input:", num_paths)

# %%
