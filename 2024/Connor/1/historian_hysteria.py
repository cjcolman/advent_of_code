import time

print("Part 1:")
print("==============================")

input_filepath = "./input.txt"
example_filepath = "./example.txt"

def read_and_sort_lists(filepath):
    with open(filepath) as f:
        lines = f.read().split("\n")
        list_0 = [int(line_split[0]) for line_split in [line.split("   ") for line in lines]]
        list_1 = [int(line_split[1]) for line_split in [line.split("   ") for line in lines]]

    list_0_sorted = sorted(list_0)
    list_1_sorted = sorted(list_1)
    return list_0_sorted, list_1_sorted

def list_diffs(filepath):
    list_0_sorted, list_1_sorted = read_and_sort_lists(filepath)

    total = 0
    for i in range(len(list_0_sorted)):
        total += abs(list_1_sorted[i] - list_0_sorted[i])

    return total

print("Example: ", list_diffs(example_filepath), "\n\n")
print("Input solution: ", list_diffs(input_filepath))
print("==============================")

print("Part 2:")
print("==============================")

def zero_dict(keys):
    out_dict = {}
    for key in keys:
        out_dict[key] = 0
    return out_dict

def similarity_scores(filepath):
    similarity_score = 0
    list_0_sorted, list_1_sorted = read_and_sort_lists(filepath)
    list_1_count_map = zero_dict(set(list_1_sorted))
    for item in list_1_sorted:
        list_1_count_map[item] += 1
    
    for item in list_0_sorted:
        try:
            similarity_score += item * list_1_count_map[item]
        except KeyError:
            continue

    return similarity_score

print("Example: ", similarity_scores(example_filepath), "\n\n")
print("Input solution: ", similarity_scores(input_filepath))
print("==============================")