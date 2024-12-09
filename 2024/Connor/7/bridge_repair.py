import time
import itertools
from operator import add, mul

print("Part 1:")
print("==============================")

input_filepath = "./input_07.txt"
example_filepath = "./example_07.txt"
example_filepath2 = "./example_07_2.txt"

def get_input(filepath):
    return open(filepath).read().split("\n")

"""
SCRAPPED
def is_line_valid(line):
    result, inputs = line.split(": ")
    result = int(result)
    inputs = inputs.split()
    operands = ["*", "+"]
    all_possible_operands_list = list(itertools.product(operands, repeat=5))
    for operand_list in all_possible_operands_list:
        eval_string = generate_eval_string(inputs, operand_list)
        if eval(eval_string) == result:
            print(line)
            return result
    else:
        return 0

def generate_eval_string(inputs, operands):
    try:
        new_input = ["("+inputs[0]+operands[0]+inputs[1]+")"]+inputs[2:]
        return generate_eval_string(new_input, operands[1:])
    except:
        return "("+inputs[0]+operands[0]+inputs[1]+")

def get_sum_of_valid_lines(filepath):
    lines = get_input(filepath)
    valid_sum = 0
    for line in lines:
        valid_sum += is_line_valid(line)

    return valid_sum

def get_line_value(result, inputs, running_total=0):
    total_1 = running_total + int(inputs[0])
    total_2 = running_total * int(inputs[0])
    if total_1 > result and total_2 > result:
        return 0
    elif (len(inputs) == 1 and total_1 == result) or (len(inputs) == 1 and total_2 == result):
        return result
    elif (len(inputs) == 1):
        return 0
    else:
        return get_line_value(result, inputs[1:], total_1) or get_line_value(result, inputs[1:], total_2)"""


def get_sum_of_valid_lines(filepath):
    lines = get_input(filepath)
    valid_sum = 0
    for line in lines:
        result, inputs = line.split(": ")
        result = int(result)
        inputs = [int(i) for i in inputs.split()]
        if is_line_valid(result, inputs):
            valid_sum += result

    return valid_sum

def get_sum_of_valid_lines_part_2(filepath):
    lines = get_input(filepath)
    valid_sum = 0
    for line in lines:
        result, inputs = line.split(": ")
        result = int(result)
        inputs = [int(i) for i in inputs.split()]
        if is_line_valid_part_2(result, inputs):
            valid_sum += result

    return valid_sum

def is_line_valid(result, inputs):
    if len(inputs) == 1:
        return inputs[0] == result
    if is_line_valid(result, [inputs[0] + inputs[1]] + inputs[2:]):
        return True
    if is_line_valid(result, [inputs[0] * inputs[1]] + inputs[2:]):
        return True
    return False

def is_line_valid_part_2(result, inputs):
    if len(inputs) == 1:
        return inputs[0] == result
    if is_line_valid_part_2(result, [inputs[0] + inputs[1]] + inputs[2:]):
        return True
    if is_line_valid_part_2(result, [inputs[0] * inputs[1]] + inputs[2:]):
        return True
    if is_line_valid_part_2(result, [int(str(inputs[0]) + str(inputs[1]))] + inputs[2:]):
        return True
    return False


# print(get_sum_of_valid_lines(example_filepath2))
print("Example: ", get_sum_of_valid_lines(example_filepath), "\n\n")
print("Input solution: ", get_sum_of_valid_lines(input_filepath))
print("==============================")


print("Part 1:")
print("==============================")
print("Example: ", get_sum_of_valid_lines_part_2(example_filepath), "\n\n")
print("Input solution: ", get_sum_of_valid_lines_part_2(input_filepath))



