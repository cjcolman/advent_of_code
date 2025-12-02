# %%
def parse_input(file_path):
    with open(file_path) as f:
        data = f.read()
    return data.strip()

# %%
def find_floor(data):
    return data.count('(') - data.count(')')

# %%
print(find_floor(parse_input('input.txt')))

# %%
def find_basement_position(data):
    current_floor = 0
    instruction_number = 1
    for instruction in data:
        current_floor += {'(': 1, ')': -1}[instruction]
        if current_floor == -1:
            return instruction_number
        instruction_number += 1

# %%
print(find_basement_position(parse_input('input.txt')))
# %%