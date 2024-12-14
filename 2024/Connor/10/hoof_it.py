print("==============================")
print("Part 1")

input_filepath = "./input_10.txt"
example_filepath = "./example_10.txt"

class Maze:
    def __init__(self, filepath):
        self.maze = [row for row in open(filepath).read().split('\n')]
        self.get_starting_points()

    def get_starting_points(self):
        self.list_of_starts = []
        for i, row in enumerate(self.maze):
            for j, height in enumerate(row):
                if height == "0":
                    self.list_of_starts.append(i + j*1j)

    def get_trailhead_score_part1(self, trailhead_start):
        directions = [-1,1,-1j,1j]
        current_stack = [trailhead_start]
        visited = []
        score = 0
        while current_stack:
            current_spot = current_stack.pop(-1)
            visited.append(current_spot)
            if self.maze[int(current_spot.real)][int(current_spot.imag)] == "9":
                score += 1
            for direction in directions:
                new_spot = current_spot + direction
                if 0 <= new_spot.real < len(self.maze) and 0 <= new_spot.imag < len(self.maze[0]):
                    if (int(self.maze[int(new_spot.real)][int(new_spot.imag)]) - int(self.maze[int(current_spot.real)][int(current_spot.imag)]) == 1) and new_spot not in visited:
                        current_stack.append(new_spot)
                else:
                    continue
        return score
    
    def get_trailhead_score_part2(self, trailhead_start):
        directions = [-1,1,-1j,1j]
        current_stack = [trailhead_start]
        score = 0
        while current_stack:
            current_spot = current_stack.pop(-1)
            if self.maze[int(current_spot.real)][int(current_spot.imag)] == "9":
                score += 1
            for direction in directions:
                new_spot = current_spot + direction
                if 0 <= new_spot.real < len(self.maze) and 0 <= new_spot.imag < len(self.maze[0]):
                    if (int(self.maze[int(new_spot.real)][int(new_spot.imag)]) - int(self.maze[int(current_spot.real)][int(current_spot.imag)]) == 1):
                        current_stack.append(new_spot)
                else:
                    continue
        return score
    
    def get_total_maze_score(self, p2=False):
        score_sum = 0
        if not p2:
            for starting_point in self.list_of_starts:
                score_sum += self.get_trailhead_score_part1(starting_point)
        elif p2:
            for starting_point in self.list_of_starts:
                score_sum += self.get_trailhead_score_part2(starting_point)

        return score_sum
    
example_maze = Maze(example_filepath)
input_maze = Maze(input_filepath)
print("Example: ", example_maze.get_total_maze_score(), "\n\n")
print("Input: ", input_maze.get_total_maze_score())

print("==============================")
print("Part 2")

print("Example: ", example_maze.get_total_maze_score(p2=True), "\n\n")
print("Input: ", input_maze.get_total_maze_score(p2=True))