import re

print("Part 1:")
print("==============================")

input_filepath = "./input_03.txt"
example_filepath = "./example_03.txt"

def get_input(filepath):
    return open(filepath).read()

def get_mult(mult_string):
    numbers = [int(i) for i in mult_string[4:-1].split(",")]
    return numbers[0] * numbers[1]


def get_all_matches(filepath):
    input = get_input(filepath)
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", input)
    running_sum = 0
    for match in matches:
        running_sum += get_mult(match)
    return running_sum

print("Example: ", get_all_matches(example_filepath), "\n\n")
print("Input solution: ", get_all_matches(input_filepath))
print("==============================")

print("Part 2:")
print("==============================")

example_filepath_2 = "./example_03_2.txt"

def get_all_matches_part_2(filepath):
    input = get_input(filepath)
    matches = re.findall("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", input)
    do = True
    running_sum = 0
    for match in matches:
        for i in match:
            if i != '':
                text = i
                break
        if text == "do()":
            do = True
        elif text == "don't()":
            do = False
        elif do:
            running_sum += get_mult(text)
        else:
            continue
    return running_sum

print("Example: ", get_all_matches_part_2(example_filepath_2), "\n\n")
print("Input solution: ", get_all_matches_part_2(input_filepath))
print("==============================")



