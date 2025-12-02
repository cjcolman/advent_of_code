# %%
def parse_input(file_path):
    with open(file_path, 'r') as file:
        elements = file.read().strip().split(',')
    return [(int(y[0]), int(y[1])) for y in [x.split('-') for x in elements]]

# %%
print(parse_input('input.txt'))

# %%
def is_valid_id_1(id):
    str_id = str(id)
    if len(str_id) % 2 == 1:
       return True
    else:
        mid = len(str_id) // 2
        if str_id[:mid] == str_id[mid:]:
            return False
    return True

# %%
def count_valid_ids_1(id_ranges):
    valid_count = 0
    for start, end in id_ranges:
        for id in range(start, end + 1):
            if not is_valid_id_1(id):
                valid_count += id
    return valid_count

# %%
print(count_valid_ids_1(parse_input('input.txt')))



# %%
def is_valid_id_2(id):
    str_id = str(id)
    valid_flag = True
    midpoint = len(str_id) // 2
    for i in range(1, midpoint+1):
        substring = str_id[:i]
        if substring * (len(str_id) // len(substring)) == str_id:
            valid_flag = False
            break
    return valid_flag

# %%
def count_valid_ids_2(id_ranges):
    valid_count = 0
    for start, end in id_ranges:
        for id in range(start, end + 1):
            if not is_valid_id_2(id):
                valid_count += id
    return valid_count
# %%

print(count_valid_ids_2(parse_input('input.txt')))
# %%