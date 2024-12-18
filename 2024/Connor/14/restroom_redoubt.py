import re
from collections import defaultdict
import matplotlib.pyplot as plt

print("Part 1:")
print("==============================")

input_filepath = "./input_14.txt"
example_filepath = "./example_14.txt"

def parse_input(filepath):
    return [[int(j) for j in re.findall(r"-*\d+", i)] for i in open(filepath).read().split("\n")]

def get_final_quadrant(inputs, width, height, t=100):
    final_x, final_y = (inputs[0]+(inputs[2]*t))%width, (inputs[1]+(inputs[3]*t))%height
    if final_x < (width-1)/2 and final_y < (height-1)/2:
        return "tl"
    elif final_x > (width-1)/2 and final_y < (height-1)/2:
        return "tr"
    elif final_x < (width-1)/2 and final_y > (height-1)/2:
        return "bl"
    elif final_x > (width-1)/2 and final_y > (height-1)/2:
        return "br"
    else:
        return None
    
def get_safety_score(filepath, width, height, t=100):
    inputs = parse_input(filepath)
    quadrants = defaultdict(lambda: 0)
    for input in inputs:
        quad = get_final_quadrant(input, width, height, t)
        if quad:
            quadrants[quad] += 1
        
    safety_score = 1
    for val in quadrants.values():
        safety_score *= val
    return safety_score

print("Example: ", get_safety_score(example_filepath, 11, 7, 100), "\n\n")
print("Input solution: ", get_safety_score(input_filepath, 101, 103, t=100))
print("==============================")

print("Part 2:")
print("==============================")

def elapse_one_second_one_robot(inputs, width, height):
    return [(inputs[0]+(inputs[2]))%width, (inputs[1]+(inputs[3]))%height, inputs[2], inputs[3]]

def elapse_one_second_all_robots(list_of_inputs, width, height):
    return [i for i in map(elapse_one_second_one_robot, list_of_inputs, [width]*len(list_of_inputs), [height]*len(list_of_inputs))]

def check_if_vertically_symmetrical(list_of_inputs, width, height):
    quadrants = defaultdict(lambda: 0)
    for inputs in list_of_inputs:
        if inputs[0] < (width-1)/2 and inputs[1] < (height-1)/2:
            quadrants["tl"] += 1
        elif inputs[0] > (width-1)/2 and inputs[1] < (height-1)/2:
            quadrants["tr"] += 1
        elif inputs[0] < (width-1)/2 and inputs[1] > (height-1)/2:
            quadrants["bl"] += 1
        elif inputs[0] > (width-1)/2 and inputs[1] > (height-1)/2:
            quadrants["br"] += 1
    if 0.99 < quadrants["tr"]/quadrants["tl"] < 1.01 and 0.99 < quadrants["br"]/quadrants["bl"] < 1.01:
        return True
    else:
        return False

def check_if_close_to_centre(list_of_inputs, width, height, threshold=0.5):
    centre = (width-1)/2
    total_dist_from_centre = 0
    for inputs in list_of_inputs:
        total_dist_from_centre += abs(inputs[0]-centre)/centre
    avg = total_dist_from_centre/len(list_of_inputs)
    return avg < threshold

def check_if_unique_positions(list_of_inputs):
    set_of_positions = set([])
    for inputs in list_of_inputs:
        set_of_positions.add((inputs[0], inputs[1]))
    return len(set_of_positions) == len(list_of_inputs)

def run_until_vertically_symmetrical(filepath, width, height):
    list_of_inputs = parse_input(filepath)
    t = 0
    # while not check_if_vertically_symmetrical(list_of_inputs, width, height) or t in [11,19,718,1324,1745,2031,2233,2342,2412,2536,2940,2969,2994,3371,3668,4406,4455,5065,5113,6180,6273,6277,6479,7032,7053,7058,7081,7413,7792,8019,9421,9938,10365,11121,11727,12148,12434,12636,12745,12815,12939,13343,13372,13397,13774,14071,14809,14858,15468,15516,16583,16676,16680,16882,17435,17456,17461,17484,17816,18195,18422,19824,20341,20768,21524,22130,22551,22837,23039,23148,23218,23746,23342,23775,23800,24177,24474,25212,25261,25871,25919]:
    # while not check_if_close_to_centre(list_of_inputs, width, height, threshold=0.3) or t<8000 or t in [8056,8157]:
    while not check_if_unique_positions(list_of_inputs):
        t += 1
        list_of_inputs = elapse_one_second_all_robots(list_of_inputs, width, height)
    zipped = [i for i in zip(*list_of_inputs)]
    x, y = zipped[0], zipped[1]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.ylim(110, -10)
    plt.show()
    return t


# print("Example: ", run_until_vertically_symmetrical(example_filepath, 11, 7), "\n\n")
print("Input solution: ", run_until_vertically_symmetrical(input_filepath, 101, 103))
print("==============================")

