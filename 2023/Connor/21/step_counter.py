with open("21/input.txt") as f:
    maze = f.read().split("\n")

def get_next_step(current_spots_set, maze):
    new_spots_set = set()
    possible_steps = [(-1,0), (1,0), (0,-1), (0,1)]
    for current_spot in current_spots_set:
        for current_step in possible_steps:
            new_x = current_spot[0] + current_step[0]
            new_y = current_spot[1] + current_step[1]
            if (new_x < 0 ) or (new_y < 0) or (new_x >= len(maze)) or (new_y >= len(maze[0])):
                continue
            elif maze[new_x][new_y] == "#":
                continue
            else:
                new_spots_set.add((new_x,new_y))
    return new_spots_set

def get_starting_spot(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == "S":
                return (x, y)
            

spots_set = set()
spots_set.add(get_starting_spot(maze))
for i in range(64):
    spots_set = get_next_step(spots_set, maze)
print(len(spots_set))   

# %%
