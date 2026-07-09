# %%
with open("input.txt") as f:
    lines = f.read().split("\n")
    coords = [tuple(int(j) for j in i.split(",")) for i in lines]

# with open("example.txt") as f:
#     lines = f.read().split("\n")
#     coords = [tuple(int(j) for j in i.split(",")) for i in lines]

# %%
from collections import deque

# %%
max_area = 0
for i in range(len(coords)):
    for j in range(len(coords)):
        if j > i:
            area = (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)
            if area > max_area:
                max_area = area

print(max_area)

# %%
def render_grid(grid):
    """
    Renders the grid as a string.
    """
    for row in grid:
        print("".join(row))


# %%
def reduce_coords(coords):
    """
    Reduces the coordinates to a smaller grid conserving the ordinality.
    Also returns separate x/y index maps so constructed rectangle corners
    can still be converted back to original coordinates.
    """
    x_coords = sorted(set(coord[0] for coord in coords))
    y_coords = sorted(set(coord[1] for coord in coords))

    x_old_to_new = {x: i for i, x in enumerate(x_coords)}
    y_old_to_new = {y: i for i, y in enumerate(y_coords)}

    x_new_to_old = {i: x for i, x in enumerate(x_coords)}
    y_new_to_old = {i: y for i, y in enumerate(y_coords)}

    reduced_coords_new_old = {
        (x_old_to_new[x], y_old_to_new[y]): (x, y)
        for x, y in coords
    }

    reduced_coords_old_new = {
        (x, y): (x_old_to_new[x], y_old_to_new[y])
        for x, y in coords
    }

    return reduced_coords_new_old, reduced_coords_old_new, x_new_to_old, y_new_to_old

# %%
def paint_polygon(coords):
    """
    Takes the input list of coordinates and paints the polygon perimeter as "#".
    """
    _, reduced_coords_old_new, _, _ = reduce_coords(coords)

    vertices = []
    for big_vertex in coords:
        reduced_vertex = reduced_coords_old_new[big_vertex]
        vertices.append(reduced_vertex)

    x_max = max(vertex[0] for vertex in vertices)
    y_max = max(vertex[1] for vertex in vertices)

    # Since your code uses grid[x][y], rows need to be x-sized
    grid = [["." for _ in range(y_max + 2)] for _ in range(x_max + 2)]

    start = vertices[0]

    while vertices:
        vertex = vertices.pop(0)
        x = vertex[0]
        y = vertex[1]

        grid[x][y] = "#"

        next_vertex = vertices[0] if vertices else start

        if x == next_vertex[0]:
            for i in range(min(y, next_vertex[1]), max(y, next_vertex[1]) + 1):
                grid[x][i] = "#"

        elif y == next_vertex[1]:
            for i in range(min(x, next_vertex[0]), max(x, next_vertex[0]) + 1):
                grid[i][y] = "#"

    return grid


# %%

def fill_polygon(grid):
    if not grid or not grid[0]:
        return grid

    rows = len(grid)
    cols = len(grid[0])

    # Work on a copy so we don't mutate the original grid
    result = [row[:] for row in grid]

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    q = deque()

    def add_if_outside(r, c):
        if (
            0 <= r < rows
            and 0 <= c < cols
            and result[r][c] == "."
            and not visited[r][c]
        ):
            visited[r][c] = True
            q.append((r, c))

    # Add all border "." cells as outside starting points
    for c in range(cols):
        add_if_outside(0, c)
        add_if_outside(rows - 1, c)

    for r in range(rows):
        add_if_outside(r, 0)
        add_if_outside(r, cols - 1)

    # Flood fill exterior empty space
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            add_if_outside(nr, nc)

    # Any "." not reached from outside is inside the polygon
    for r in range(rows):
        for c in range(cols):
            if result[r][c] == "." and not visited[r][c]:
                result[r][c] = "#"

    return result


# %%

def get_all_rectangles(grid, coords):
    """
    Given a list of coordnates, returns a list of all rectangles defined by the coordinates. Each rectangle is represented as a tuple of two tuples: ((top_left_row, top_left_col), (bottom_right_row, bottom_right_col)). The returned list is sorted by area in descending order.    
    """
    rectangles = []
    for i in range(len(coords)):
        for j in range(len(coords)):
            if j > i:
                top_left = (min(coords[i][0], coords[j][0]), min(coords[i][1], coords[j][1]))
                bottom_right = (max(coords[i][0], coords[j][0]), max(coords[i][1], coords[j][1]))
                rectangles.append((top_left, bottom_right))

    # Sort rectangles by area in descending order
    rectangles.sort(key=lambda rect: (rect[1][0] - rect[0][0] + 1) * (rect[1][1] - rect[0][1] + 1), reverse=True)
    return rectangles

# %%

def is_rectangle_filled(grid, top_left, bottom_right):
    """
    Checks if the rectangle defined by top_left and bottom_right is filled with "#".
    """
    for r in range(top_left[0], bottom_right[0] + 1):
        for c in range(top_left[1], bottom_right[1] + 1):
            if grid[r][c] != "#":
                return False
    return True


# %%
def find_largest_filled_rectangle(grid, list_of_rectangles):
    """
    Given a grid and a list of rectangles, finds the largest rectangle that is completely filled with "#".
    """
    for rect in list_of_rectangles:
        if is_rectangle_filled(grid, rect[0], rect[1]):
            return rect
    return None

# %%
def get_area_of_rectangle(rect, x_new_to_old, y_new_to_old):
    """
    Converts reduced rectangle coordinates back to original coordinates
    using independent x/y mappings.
    """
    top_left, bottom_right = rect

    x1 = x_new_to_old[top_left[0]]
    y1 = y_new_to_old[top_left[1]]

    x2 = x_new_to_old[bottom_right[0]]
    y2 = y_new_to_old[bottom_right[1]]

    return (x2 - x1 + 1) * (y2 - y1 + 1)

# %%
if __name__ == "__main__":
    (
        reduced_coords_new_old,
        reduced_coords_old_new,
        x_new_to_old,
        y_new_to_old
    ) = reduce_coords(coords)

    vertices = []
    for big_vertex in coords:
        reduced_vertex = reduced_coords_old_new[big_vertex]
        vertices.append(reduced_vertex)

    grid_edges = paint_polygon(coords)
    all_rectangles = get_all_rectangles(grid_edges, vertices)

    grid = fill_polygon(grid_edges)

    largest_filled_rectangle = find_largest_filled_rectangle(grid, all_rectangles)

    area_of_rectangle = get_area_of_rectangle(
        largest_filled_rectangle,
        x_new_to_old,
        y_new_to_old
    )

    print(area_of_rectangle)

# %%
from IPython.display import HTML, display

def render_grid_html(edge_grid, filled_grid=None, rectangle=None, cell_size=8):
    """
    Renders the grid as HTML.

    Colours:
    - blue: polygon boundary
    - light grey: polygon interior
    - green: largest rectangle
    - white: outside area
    """

    if filled_grid is None:
        filled_grid = edge_grid

    rect_cells = set()

    if rectangle is not None:
        (r1, c1), (r2, c2) = rectangle

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                rect_cells.add((r, c))

    html = f"""
    <div style="
        display: inline-grid;
        grid-template-columns: repeat({len(filled_grid[0])}, {cell_size}px);
        font-size: 0;
        border: 1px solid #ddd;
    ">
    """

    for r in range(len(filled_grid)):
        for c in range(len(filled_grid[0])):

            if (r, c) in rect_cells:
                colour = "#2ecc71"   # green
            elif edge_grid[r][c] == "#":
                colour = "#3498db"   # blue
            elif filled_grid[r][c] == "#":
                colour = "#bdc3c7"   # grey
            else:
                colour = "#ffffff"   # white

            html += f"""
            <div style="
                width: {cell_size}px;
                height: {cell_size}px;
                background-color: {colour};
            "></div>
            """

    html += "</div>"

    display(HTML(html))
# %%
edge_grid = paint_polygon(coords)
filled_grid = fill_polygon(edge_grid)

largest_filled_rectangle = find_largest_filled_rectangle(
    filled_grid,
    all_rectangles
)

render_grid_html(
    edge_grid=edge_grid,
    filled_grid=filled_grid,
    rectangle=largest_filled_rectangle,
    cell_size=6
)
# %%
