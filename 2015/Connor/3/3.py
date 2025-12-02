# %%
def parse_input(file_path):
    with open(file_path) as f:
        directions = f.read()
    return directions

# %%
def get_list_of_visits(directions):
    current_x, current_y = 0, 0
    all_visits = [(current_x, current_y)]
    for direction in directions:
        current_x += {"<":-1, ">":1, "^":0, "v":0}[direction]
        current_y += {"<":0, ">":0, "^":1, "v":-1}[direction]
        all_visits.append((current_x, current_y))
    return all_visits

# %%
def get_unique_visits(all_visits):
    return len(set(all_visits))

# %%
def split_paths(directions):
    santa_path = []
    robo_path = []
    for i, direction in enumerate(directions):
        if i % 2 == 0:
            santa_path.append(direction)
        else:
            robo_path.append(direction)
    return santa_path, robo_path

# %%
print("part 1: ", get_unique_visits(get_list_of_visits(parse_input("input.txt"))))
print("part 2: ", get_unique_visits(get_list_of_visits(split_paths(parse_input("input.txt"))[0]) + get_list_of_visits(split_paths(parse_input("input.txt"))[1])))
# %%
