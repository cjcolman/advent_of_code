import time

print("Part 1:")
print("==============================")

input_filepath = "./input_06.txt"
example_filepath = "./example_06.txt"

class Play():
    def __init__(self, filepath):
        self.filepath = filepath
        self.maze = self.get_maze()
        self.current_i, self.current_j, self.current_direction = self.get_starting_point_and_direction()
        self.visited_squares = set([])
        self.finished = False
        self.in_loop = False
        self.direction_map = {"N":(-1,0),
                              "E":(0,1),
                              "S":(1,0),
                              "W":(0,-1)}

    def get_maze(self):
        maze = open(self.filepath).read().split("\n")
        return maze
    
    def get_starting_point_and_direction(self):
        for i, row in enumerate(self.maze):
            j = row.find("^")
            if j != -1:
                return i, j, "N"
            
    def go(self):
        self.next_direction = "E"
        while not self.finished:
            self.visited_squares.add((self.current_i, self.current_j, self.current_direction))
            self.next_i = self.current_i + self.direction_map[self.current_direction][0]
            self.next_j = self.current_j + self.direction_map[self.current_direction][1]
            if self.next_i < 0 or self.next_i == len(self.maze) or self.next_j < 0 or self.next_j >= len(self.maze[0]):
                self.finished = True
                break
            elif self.maze[self.next_i][self.next_j] == "#":
                self.rotate()
            else:
                self.take_step()

            if (self.current_i, self.current_j, self.current_direction) in self.visited_squares:
                self.finished = True
                self.in_loop = True
        return self.exit()


    def take_step(self):
        self.current_i = self.current_i + self.direction_map[self.current_direction][0]
        self.current_j = self.current_j + self.direction_map[self.current_direction][1]
        """potential_obst_i = self.current_i + self.direction_map[self.current_direction][0]
        potential_obst_j = self.current_j + self.direction_map[self.current_direction][1]
        if not (potential_obst_i < 0 or potential_obst_i == len(self.maze) or potential_obst_j < 0 or potential_obst_j >= len(self.maze[0])):
            terminate = False
            check_i = self.current_i
            check_j = self.current_j
            while not terminate:
                if check_i < 0 or check_i == len(self.maze) or check_j < 0 or check_j >= len(self.maze[0]) or self.maze[check_i][check_j] == "#":
                    terminate = True
                elif (check_i, check_j, self.next_direction) in self.visited_squares:
                    terminate = True
                    self.new_obstacles.add((potential_obst_i, potential_obst_j))
                else:
                    check_i = check_i + self.direction_map[self.next_direction][0]
                    check_j = check_j + self.direction_map[self.next_direction][1]"""


    def rotate(self):
        if self.current_direction == "N":
            self.current_direction = "E"
            # self.next_direction = "S"
        elif self.current_direction == "E":
            self.current_direction = "S"
            # self.next_direction = "W"
        elif self.current_direction == "S":
            self.current_direction = "W"
            # self.next_direction = "N"
        elif self.current_direction == "W":
            self.current_direction = "N"
            # self.next_direction = "E"

    def exit(self):
        return len(self.visited_squares), self.in_loop
    

print("Example: ", Play(example_filepath).go(), "\n\n")
print("Input solution: ", Play(input_filepath).go())
print("==============================")


print("Part 2:")
print("==============================")

def find_all_potential_loop_obstacles(filepath):
    start = time.time()
    temp = Play(filepath)
    starting_i, starting_j, _ = temp.get_starting_point_and_direction()
    loop_count = 0
    for i in range(len(temp.maze)):
        for j in range(len(temp.maze[0])):
            if (i == starting_i and j == starting_j) or temp.maze[i][j] == "#":
                continue
            else:
                checker = Play(filepath)
                checker.maze = [[square for square in row] for row in checker.maze]
                checker.maze[i][j] = "#"
                ___, enters_loop = checker.go()
                loop_count += enters_loop
    return loop_count, time.time() - start
            
print(find_all_potential_loop_obstacles(example_filepath)) # Takes about 0.6s
print(find_all_potential_loop_obstacles(input_filepath)) # Takes about 50s