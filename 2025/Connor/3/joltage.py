# %%
def parse_input(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

# %%
print(parse_input('input.txt'))

# %% - SUPERCEDED BY NEXT FUNCTION
# def get_largest_joltage(bank_string):
#     if bank_string.index(max(bank_string)) + 1 != len(bank_string):
#         idx, val = bank_string.index(max(bank_string)), max(bank_string)
#     else:
#         return int(max(bank_string[:-1]) + bank_string[-1])
#     return int(val + max(bank_string[idx+1:]))
# %%
def get_largest_joltage(bank_string, l=12):
    current_output = []
    remaining_string = bank_string
    t = l-1
    while len(current_output) < l:
        search_string = remaining_string[:-t]
        if search_string == "":
            search_string = remaining_string
        idx, val = search_string.index(max(search_string)), max(search_string)
        current_output.append(val)
        remaining_string = remaining_string[idx+1:]
        t -= 1
    return int(''.join(current_output))
# %%
def total_output_joltage(list_of_banks):
    total = 0
    for bank in list_of_banks:
        total += get_largest_joltage(bank)
    return total

# %%
def test():
    print("Test 1: ", get_largest_joltage("987654321111111", 2), "\nExpected: 98")
    print("Test 2: ", get_largest_joltage("811111111111119", 2), "\nExpected: 89")
    print("Test 3: ", get_largest_joltage("234234234234278", 2), "\nExpected: 78")
    print("Test 4: ", get_largest_joltage("818181911112111", 2), "\nExpected: 92")

test()
# %%
print("Part 1:", total_output_joltage(parse_input('input.txt')))

# %%
def test_2():
    print("Test 1: ", get_largest_joltage("987654321111111", 12), "\nExpected: 987654321111")
    print("Test 2: ", get_largest_joltage("811111111111119", 12), "\nExpected: 811111111119")
    print("Test 3: ", get_largest_joltage("234234234234278", 12), "\nExpected: 434234234278")
    print("Test 4: ", get_largest_joltage("818181911112111", 12), "\nExpected: 888911112111")

test_2()
# %%
def total_output_joltage_2(list_of_banks):
    total = 0
    for bank in list_of_banks:
        total += get_largest_joltage(bank, 12)
    return total

# %%
print("Part 2:", total_output_joltage_2(parse_input('input.txt')))

# %%
