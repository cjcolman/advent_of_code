from collections import defaultdict

print("Part 1:")
print("==============================")

input_filepath = "./input_12.txt"
example_filepath1 = "./example_12_1.txt"
example_filepath2 = "./example_12_2.txt"
example_filepath3 = "./example_12_3.txt"

def get_grid(filepath):
    return [[plot for plot in row] for row in open(filepath).read().split("\n")]

def get_fencing_price(filepath):
    region_dict = defaultdict(lambda: 0)
    grid = get_grid(filepath)
    # first pass
    region_dict = horizontal_pass(grid, region_dict)
    # second pass
    region_dict = horizontal_pass([i for i in zip(*grid)], region_dict, first_pass=False)

    region_dict[None] = 0
    price = 0
    for val in region_dict.values():
        price += val.real * val.imag
    
    return price

def horizontal_pass(grid, region_dict, first_pass=True):
    for i, row in enumerate(grid):
        previous_plot = None
        for j, plot in enumerate(row):
            if first_pass:
                region_dict[plot] += 1
            if plot != previous_plot:
                region_dict[previous_plot] += 1j
                region_dict[plot] += 1j
            previous_plot = plot
            if j == len(grid[0])-1:
                region_dict[plot] += 1j
    return region_dict

def get_region_area_and_perimeter(grid, starting_point, visited):
    region_name = grid[int(starting_point.real)][int(starting_point.imag)]
    current_stack = [starting_point]
    directions = [1, -1, 1j, -1j]
    area = 0
    perimeter = 0
    while current_stack:
        area += 1
        current_point = current_stack.pop(-1)
        visited.add(current_point)
        for direction in directions:
            next_point = current_point + direction
            if next_point.real < 0 or next_point.real >= len(grid) or next_point.imag < 0 or next_point.imag >= len(grid[0]) or grid[int(next_point.real)][int(next_point.imag)] != region_name:
                perimeter += 1
            elif next_point not in visited and next_point not in current_stack:
                current_stack.append(next_point)         
    return area, perimeter, visited

def get_total_price(filepath, p2=False):
    grid = get_grid(filepath)
    price = 0
    visited = set([])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i + j*1j not in visited:
                if not p2:
                    area, perimeter, visited = get_region_area_and_perimeter(grid, i + j*1j, visited)
                elif p2:
                    area, perimeter, visited = get_region_area_and_perimeter_part2(grid, i + j*1j, visited)
                price += area * perimeter
    return price

print("Example 1: ", get_total_price(example_filepath1), "\n\n")
print("Example 2: ", get_total_price(example_filepath2), "\n\n")
print("Example 3: ", get_total_price(example_filepath3), "\n\n")
print("Input solution: ", get_total_price(input_filepath))
print("==============================")


print("Part 2:")
print("==============================")

def get_region_area_and_perimeter_part2(grid, starting_point, visited):
    region_name = grid[int(starting_point.real)][int(starting_point.imag)]
    current_stack = [starting_point]
    directions = [1, -1, 1j, -1j]
    area = 0
    perimeter = 0
    fence_boundaries = []
    while current_stack:
        area += 1
        current_point = current_stack.pop(-1)
        visited.add(current_point)
        for direction in directions:
            next_point = current_point + direction
            if next_point.real < 0 or next_point.real >= len(grid) or next_point.imag < 0 or next_point.imag >= len(grid[0]) or grid[int(next_point.real)][int(next_point.imag)] != region_name:
                fence_boundaries.append((current_point, next_point))
            elif next_point not in visited and next_point not in current_stack:
                current_stack.append(next_point)

    # Calculate fence parts
    while fence_boundaries:
        current_fence = fence_boundaries[-1]
        if abs(current_fence[1].imag-current_fence[0].imag) == 1: # Vertical Fence
            check = list(current_fence)
            while tuple(check) in fence_boundaries:
                check[0], check[1] = check[0] - 1, check[1] - 1
            check = [check[0] + 1, check[1] + 1] # Starting point            
            while tuple(check) in fence_boundaries:
                fence_boundaries.remove(tuple(check))
                check[0], check[1] = check[0] + 1, check[1] + 1
            perimeter += 1
        elif abs(current_fence[1].real-current_fence[0].real) == 1: # Horizontal Fence
            check = list(current_fence)
            while tuple(check) in fence_boundaries:
                check[0], check[1] = check[0] - 1j, check[1] - 1j
            check = [check[0] + 1j, check[1] + 1j] # Starting point            
            while tuple(check) in fence_boundaries:
                fence_boundaries.remove(tuple(check))
                check[0], check[1] = check[0] + 1j, check[1] + 1j
            perimeter += 1

    return area, perimeter, visited

print("Example 1: ", get_total_price(example_filepath1, p2=True), "\n\n")
print("Example 2: ", get_total_price(example_filepath2, p2=True), "\n\n")
print("Example 3: ", get_total_price(example_filepath3, p2=True), "\n\n")
print("Input solution: ", get_total_price(input_filepath, p2=True))
print("==============================")