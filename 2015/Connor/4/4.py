# %%
from hashlib import md5


def parse_input(file_path):
    with open(file_path) as f:
        keyword = f.read()
    return keyword

# %%
def check_hash(hash_string, leading_zeros):
    if hash_string[:leading_zeros] == leading_zeros * "0":
        return True
    else:
        return False
   
# %%
def get_lowest_hash_number(keyword, leading_zeros):
    number = 0
    while not check_hash(md5((keyword + str(number)).encode()).hexdigest(), leading_zeros):
        number += 1
    return number

# %%
print("Part 1: ", get_lowest_hash_number(parse_input("input.txt"), 5))
print("Part 2: ", get_lowest_hash_number(parse_input("input.txt"), 6))

# %%
