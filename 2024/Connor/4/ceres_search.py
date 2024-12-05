print("Part 1:")
print("==============================")

input_filepath = "./input_04.txt"
example_filepath = "./example_04.txt"

def get_input_as_list_of_strings(filepath):
    return open(filepath).read().split("\n")

def transpose_90(list_of_strings):
    return [''.join(i) for i in zip(*list_of_strings)]

def transpose_45(list_of_strings):
    num_of_new_strings = len(list_of_strings) + len(list_of_strings[0]) - 1
    output = ['' for _ in range(num_of_new_strings)]
    for j in range(len(list_of_strings[0])):
        for i in range(len(list_of_strings)):
            string_no = i+j
            output[string_no] += list_of_strings[i][j]
    return output

def rotate_90(list_of_strings):
    return ["".join(i) for i in zip(*reversed(list_of_strings))]

def get_all_orientations(filepath):
    list_1 = get_input_as_list_of_strings(filepath)
    list_2 = transpose_90(list_1)
    list_3 = transpose_45(list_1)
    list_4 = transpose_45(rotate_90(list_1))

    all_lists = list_1 + list_2 + list_3 + list_4
    return all_lists

def count_matches(filepath):
    all_lists = get_all_orientations(filepath)
    count = 0
    for row in all_lists:
        count += row.count("XMAS")
        count += row.count("SAMX")

    return count


print("Example: ", count_matches(example_filepath), "\n\n")
print("Input solution: ", count_matches(input_filepath))
print("==============================")

print("Part 2:")
print("==============================")

def add_border(input):
    input.insert(0,"."*len(input[0]))
    input.insert(len(input[0])+1,"."*len(input[0]))
    output = ["."+line+"." for line in input]
    return output

def is_mas_centre(input, i, j):
    corners = [(i-1,j-1),
               (i-1,j+1),
               (i+1,j-1),
               (i+1,j+1)]
    corners_string = ''
    for corner in corners:
        try:
            corners_string += input[corner[0]][corner[1]]
        except:
            return False
    if corners_string.count("M") == 2 and corners_string.count("S") == 2 and corners_string[0] != corners_string[-1]: # Final condition to stop mam / sas
        return True
    else:
        return False


def count_matches_part_2(filepath):
    input = get_input_as_list_of_strings(filepath)
    input = add_border(input)
    count = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "A":
                count += is_mas_centre(input, i, j)

    return count

print("Example: ", count_matches_part_2(example_filepath), "\n\n")
print("Input solution: ", count_matches_part_2(input_filepath))
print("==============================")
