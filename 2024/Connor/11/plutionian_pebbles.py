from functools import cache


print("Part 1:")
print("==============================")

input_filepath = "./input_11.txt"
example_filepath = "./example_11.txt"
example_filepath2 = "./example_11_2.txt"

def get_stones(filepath):
    return [int(i) for i in open(filepath).read().split()]

def apply_blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            num_str = str(stone)
            num_len = len(num_str)
            new_stones.append(int(num_str[0:int(num_len/2)]))
            new_stones.append(int(num_str[int(num_len/2):]))
        else:
            new_stones.append(stone*2024)
    return new_stones

def apply_n_blinks(filepath, n=1):
    stones = get_stones(filepath)
    for _ in range(n):
        stones = apply_blink(stones)
    return len(stones)

print("Example: ", apply_n_blinks(example_filepath, 6), "\n\n")
print("Example2 : ", apply_n_blinks(example_filepath, 25), "\n\n")
print("Input solution: ", apply_n_blinks(input_filepath, 25))
print("==============================")


print("Part 2:")
print("==============================")


# SCRAPPED
# @cache
# def recursively_blink(stone, blinks_left):
#     blinks_left -= 1
#     if blinks_left < 0 and stone == 0:
#         return 1
#     elif stone == 0:
#         return recursively_blink(1, blinks_left)
    
#     elif blinks_left < 0 and len(str(stone)) % 2 == 0:
#         return 2
#     elif len(str(stone)) % 2 == 0:
#         num_str = str(stone)
#         num_len = len(num_str)
#         return recursively_blink(int(num_str[0:int(num_len/2)]), blinks_left) + recursively_blink(int(num_str[int(num_len/2):]), blinks_left)
    
#     elif blinks_left < 0 and len(str(stone)) % 2 == 1:
#         return 1
#     else:
#         return recursively_blink(stone*2024, blinks_left)
    
@cache
def recursively_blink(stone, blinks_left):
    if blinks_left == 0:
        return 1
    if stone == 0:
        return recursively_blink(1, blinks_left-1)
    num_str = str(stone)
    num_len = len(num_str)
    if num_len % 2:
        return recursively_blink(stone*2024, blinks_left-1)
    else:
        return recursively_blink(int(num_str[0:int(num_len/2)]), blinks_left-1) + recursively_blink(int(num_str[int(num_len/2):]), blinks_left-1)


def apply_n_blinks_p2(filepath, n):
    stones = get_stones(filepath)
    running_count = 0
    for stone in stones:
        running_count += recursively_blink(stone, n)
    return running_count


print("Input solution: ", apply_n_blinks_p2(input_filepath, 75))
