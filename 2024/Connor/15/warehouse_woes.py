from collections import defaultdict


print("Part 1:")
print("==============================")

input_filepath = "./input_15.txt"
example_filepath1 = "./example_15_1.txt"
example_filepath2 = "./example_15_2.txt"
example_filepath3 = "./example_15_3.txt"
example_filepath4 = "./example_15_4.txt"

def parse_input(filepath):
    grid = [[el for el in row] for row in open(filepath).read().split("\n\n")[0].split("\n")]
    instructions = open(filepath).read().split("\n\n")[1].replace("\n","")
    return grid, instructions

def push(grid, coord, direction):
    next_coord = coord+direction
    if grid[int(next_coord.real)][int(next_coord.imag)] == ".":
        grid[int(next_coord.real)][int(next_coord.imag)] = grid[int(coord.real)][int(coord.imag)]
        grid[int(coord.real)][int(coord.imag)] = "."
        return grid
    elif grid[int(next_coord.real)][int(next_coord.imag)] == "#":
        return grid
    else:
        grid[int(next_coord.real)][int(next_coord.imag)] = grid[int(coord.real)][int(coord.imag)]
        return push(grid, next_coord, direction)
    

def push(grid, coord, direction):
    next_coord = coord + direction
    next_element = grid[int(next_coord.real)][int(next_coord.imag)]
    if next_element == "O":
        return push(grid, next_coord, direction)
    elif next_element == "#":
        return grid
    elif next_element == ".":
        current_check = next_coord
        while grid[int(current_check.real)][int(current_check.imag)] != "@":
            grid[int(current_check.real)][int(current_check.imag)] = "O"
            current_check -= direction
        grid[int((current_check+direction).real)][int((current_check+direction).imag)] = "@"
        grid[int(current_check.real)][int(current_check.imag)] = "."
        return grid

def find_boy(grid):
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "@":
                return i + 1j*j 
            
def run_instructions(filepath):
    grid, instructions = parse_input(filepath)
    instruction_map = {
        "<": -1j,
        "^": -1,
        ">": 1j,
        "v": 1
    }
    instructions = [instruction_map[el] for el in instructions]
    for instruction in instructions:
        grid = push(grid, find_boy(grid), instruction)
    return calc_gps(grid)

def calc_gps(grid):
    sum = 0
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "O":
                sum += 100*i + j
    return sum

print("Example1: ", run_instructions(example_filepath1), "\n\n")
print("Example2: ", run_instructions(example_filepath2), "\n\n")
print("Input solution: ", run_instructions(input_filepath))
print("==============================")

print("Part 2:")
print("==============================")

class Grid:
    def __init__(self, filepath):
        self.grid, self.instructions = self.parse_input(filepath)
        self.bot_location = self.find_boy()
    
    def parse_input(self, filepath):
        grid = [[el for el in row] for row in open(filepath).read().split("\n\n")[0].split("\n")]
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el == "#":
                    grid[i][j] = "##"
                elif el == "O":
                    grid[i][j] = "[]"
                elif el == ".":
                    grid[i][j] = ".."
                elif el == "@":
                    grid[i][j] = "@."
            grid[i] = ''.join(grid[i])
        instructions = open(filepath).read().split("\n\n")[1].replace("\n","")
        return grid, instructions
    
    def find_boy(self):
        for i, row in enumerate(self.grid):
            for j, el in enumerate(row):
                if el == "@":
                    return i + 1j*j

    def get_box_locations(self):
        list_of_boxes = []
        for i, row in enumerate(self.grid):
            for j, el in enumerate(row):
                if el == "[":
                    list_of_boxes.append(Box(i+1j*j))
        return list_of_boxes
                
    def plot_grid(self, list_of_boxes):
        grid_plot = []
        for i, row in enumerate(self.grid):
            grid_plot.append([])
            for j, element in enumerate(row):
                if element in ["[", "]", "@"]:
                    grid_plot[i].append(".")
                else:
                    grid_plot[i].append(element)

        for box in list_of_boxes:
            grid_plot[int(box.left_coord.real)][int(box.left_coord.imag)] = "["
            grid_plot[int(box.right_coord.real)][int(box.right_coord.imag)] = "]"

        grid_plot[int(self.bot_location.real)][int(self.bot_location.imag)] = "@"

        return grid_plot

    """def step(self, direction, list_of_boxes):
        direction_map = {
            "<": -1j,
            "^": -1,
            ">": 1j,
            "v": 1
        }
        direc = direction_map[direction]
        next_location = self.bot_location + direc
        pushed_boxes = []
        if self.grid[int(next_location.real)][int(next_location.imag)] == "#":
            pushed=False
        else:
            pushed=True
            for box in list_of_boxes:
                if next_location == box.left_coord or next_location == box.right_coord:
                    box_pushed = box.push(direc, list_of_boxes, self.grid)
                    pushed = pushed * box_pushed
                    if box_pushed:
                        pushed_boxes.append(box)
        if not pushed:
            for box in pushed_boxes:
                box.left_coord = box.left_coord - direc
                box.right_coord = box.right_coord - direc
        elif pushed:
            self.bot_location = next_location
        #return self.plot_grid(list_of_boxes)"""

    def step(self, direction, list_of_boxes):
        direction_map = {
            "<": -1j,
            "^": -1,
            ">": 1j,
            "v": 1
        }
        direc = direction_map[direction]
        next_location = self.bot_location + direc
        if self.grid[int(next_location.real)][int(next_location.imag)] == "#":
            return
        elif self.grid[int(next_location.real)][int(next_location.imag)] == ".":
            self.bot_location = next_location
            return
        else:
            boxes_to_check = set([])
            boxes_to_move = set([])
            for box in list_of_boxes:
                if next_location == box.left_coord or next_location == box.right_coord:
                    boxes_to_check.add(box)
                    boxes_to_move.add(box)
                    break
            
            valid = True
            while valid and boxes_to_check:
                current_box = boxes_to_check.pop()
                next_left = current_box.left_coord + direc
                next_right = current_box.right_coord + direc
                if self.grid[int(next_left.real)][int(next_left.imag)] == "#" or self.grid[int(next_left.real)][int(next_left.imag)] == "#":
                    valid = False
                elif self.grid[int(next_left.real)][int(next_left.imag)] == "." and self.grid[int(next_left.real)][int(next_left.imag)] == ".":
                    continue
                else:
                    for box in list_of_boxes:
                        if box.left_coord+direc == next_left and box.right_coord+direc == next_right:
                            continue
                        if current_box.left_coord + direc + box.left_coord or\
                           current_box.left_coord + direc + box.right_coord or\
                           current_box.right_coord + direc + box.left_coord or\
                           current_box.right_coord + direc + box.right_coord:
                            boxes_to_check.add(box)
                            boxes_to_move.add(box)
            
            if not valid:
                return
            else:
                for box in boxes_to_move:
                    box.left_coord += direc
                    box.right_coord += direc
                return



class Box:
    def __init__(self, left_coord):
        self.left_coord = left_coord
        self.right_coord = left_coord + 1j

    def push(self, direction, list_of_boxes, grid):
        next_left_coord = self.left_coord + direction
        next_right_coord = self.right_coord + direction
        if grid[int(next_left_coord.real)][int(next_left_coord.imag)] == "#" or grid[int(next_right_coord.real)][int(next_right_coord.imag)] == "#":
            return False
        else:
            pushed = True
            pushed_boxes = []
            for box in list_of_boxes:
                if box.left_coord+direction == next_left_coord and box.right_coord+direction == next_right_coord:
                    continue
                if next_left_coord == box.left_coord or\
                   next_left_coord == box.right_coord or\
                   next_right_coord == box.left_coord or\
                   next_right_coord == box.right_coord:
                    box_pushed = box.push(direction, list_of_boxes, grid)
                    pushed = pushed * box_pushed
                    if box_pushed:
                        pushed_boxes.append(box)
            if not pushed:
                for box in pushed_boxes:
                    box.left_coord = box.left_coord - direction
                    box.right_coord = box.right_coord - direction
                return False
            elif pushed:
                self.left_coord = next_left_coord
                self.right_coord = next_right_coord
                return True
            else:
                return False
                    

ex_grid = Grid(example_filepath4)
list_of_boxes = ex_grid.get_box_locations()
grid_plot = ex_grid.plot_grid(list_of_boxes)
for row in grid_plot:
    print(''.join(row))
print("\n")
for direction in ex_grid.instructions:
    ex_grid.step(direction, list_of_boxes)
    grid_plot = ex_grid.plot_grid(list_of_boxes)
    for row in grid_plot:
        print(''.join(row))
    print("\n")

gps = 0
for box in list_of_boxes:
    gps += 100*int(box.left_coord.real) + int(box.left_coord.imag)

print(gps)
grid_plot = ex_grid.plot_grid(list_of_boxes)
for row in grid_plot:
    print(''.join(row))

