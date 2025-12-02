# %%
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    return data

# %%
def get_rotations(instructions_list):
    rotations = []
    for instruction in instructions_list:
        if instruction[0] == 'L':
            rotations.append(-int(instruction[1:]))
        elif instruction[0] == 'R':
            rotations.append(int(instruction[1:]))
    return rotations

# %%
def get_password_1(instructions_list):
    current_position = 50
    current_password = 0
    for instruction in instructions_list:
        current_position = (current_position + instruction) % 100
        if current_position == 0:
            current_password += 1
    return current_password

# %%
print(get_password_1(get_rotations(read_input('input.txt'))))
# %%
def get_password_2(instructions_list):
    current_position = 50
    current_password = 0
    for instruction in instructions_list:
        rotation_remaining = instruction
        while rotation_remaining != 0:
            step = 1 if rotation_remaining > 0 else -1
            current_position = (current_position + step) % 100
            rotation_remaining -= step
            if current_position == 0:
                current_password += 1
    return current_password

# %%
print(get_password_2(get_rotations(read_input('input.txt'))))
# %%