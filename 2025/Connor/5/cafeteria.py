# %%
def parse_input(filepath):
    """Input comes in two parts, first half is the ranges of fresh ids, e.g. "2390-2602". One per line.
       Second half is a list of ids, one per line.
       Two halves separeted by a blank line.
       Returns a list of tuples representing the ranges and a list of ids to check."""
    with open(filepath, 'r') as file:
        sections = file.read().strip().split('\n\n')
        ranges = []
        for line in sections[0].strip().split('\n'):
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        ids = [int(line) for line in sections[1].strip().split('\n')]
    return ranges, ids

# %%
def is_id_fresh(id_num, ranges):
    """Checks if the given id_num falls within any of the provided ranges."""
    for start, end in ranges:
        if start <= id_num <= end:
            return True
    return False

# %%
def count_fresh_ids(ranges, ids):
    """Counts how many ids in the list are considered fresh based on the provided ranges."""
    fresh_count = 0
    for id_num in ids:
        if is_id_fresh(id_num, ranges):
            fresh_count += 1
    return fresh_count

# %%
ranges, ids = parse_input('input.txt')
print(count_fresh_ids(ranges, ids))

# %%
def combine_two_ranges(list_of_ranges):
    ranges = sorted(list_of_ranges, key=lambda x: x[0])
    start_1 = ranges[0][0]
    end_1 = ranges[0][1]
    start_2 = ranges[1][0]
    end_2 = ranges[1][1]
    if start_2 <= end_1:
        return (min(start_1, start_2), max(end_1, end_2))
    else: return None

# %% - DOESN'T WORK YET
# def combine_all_ranges(list_of_ranges):
#     output = []
#     while list_of_ranges:
#         current_range = list_of_ranges.pop(0)
#         for check_range in list_of_ranges:
#             combined = combine_two_ranges([current_range, check_range])
#             if combined:
#                 if list_of_ranges:
#                     list_of_ranges.append(combined)
#                     try:
#                         if current_range == previous_range:
#                             output.append(combined)
#                             return sorted(output, key=lambda x: x[0])
#                     except NameError:
#                         pass
#                     previous_range = current_range
#                     break
#                 else:
#                     output.append(combined)
#                     return sorted(output, key=lambda x: x[0]) 
#         else:
#             output.append(current_range)
#     return sorted(output, key=lambda x: x[0])

# %%
def combine_all_ranges(list_of_ranges):
    starts = [(r[0], 1) for r in list_of_ranges]
    ends = [(r[1], -1) for r in list_of_ranges]
    endpoints = sorted(starts + ends, key=lambda x: x[0])

    out_ranges = []
    running_total = 0
    for endpoint in endpoints:
        running_total += endpoint[1]
        if running_total == 1 and endpoint[1] == 1:
            current_start = endpoint[0]
        elif running_total == 0 and endpoint[1] == -1:
            out_ranges.append((current_start, endpoint[0]))
    return out_ranges

# %%
example_ranges, _ = parse_input("example.txt")
print(combine_all_ranges(example_ranges))

ranges, _ = parse_input("input.txt")
print(combine_all_ranges(ranges))

# %%
def count_all_fresh_possibilities(ranges):
    total_fresh = 0
    for start, end in ranges:
        total_fresh += (end - start + 1)
    return total_fresh
# %%

example_ranges, _ = parse_input("example.txt")
combined_ranges = combine_all_ranges(example_ranges)
print(combined_ranges)
print(count_all_fresh_possibilities(combined_ranges))

# %%
ranges, _ = parse_input("input.txt")
combined_ranges = combine_all_ranges(ranges)
print(count_all_fresh_possibilities(combined_ranges))

# %%
