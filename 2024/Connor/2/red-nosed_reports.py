print("Part 1:")
print("==============================")

input_filepath = "./input_02.txt"
example_filepath = "./example_02.txt"

def get_reports(filepath):
    with open(filepath) as f:
        lines = f.read().split("\n")
    output = []
    for i, line in enumerate(lines):
        output.append([])
        for element in line.split():
            output[i].append(int(element))
    return output

def get_difference_array(list_of_levels):
    difference_array = []
    for i in range(0, len(list_of_levels)-1):
        difference_array.append(list_of_levels[i+1]-list_of_levels[i])
    return difference_array

def check_report(report):
    difference_array = get_difference_array(report)
    allowed_positive_range = (1,3)
    allowed_negative_range = (-3,-1)
    in_pos_range, in_neg_range = True, True
    for k in difference_array:
        if k < allowed_positive_range[0] or k > allowed_positive_range[1]:
            in_pos_range = False
        if k < allowed_negative_range[0] or k > allowed_negative_range[1]:
            in_neg_range = False
    if in_pos_range or in_neg_range:
        return True
    else:
        return False
    
def check_all_reports(filepath):
    list_of_reports = get_reports(filepath)
    num_of_safe_reports = 0
    for report in list_of_reports:
        if check_report(report):
            num_of_safe_reports += 1
        else:
            continue
    return num_of_safe_reports

print("Example: ", check_all_reports(example_filepath), "\n\n")
print("Input solution: ", check_all_reports(input_filepath))
print("==============================")

print("Part 2:")
print("==============================")

def generate_all_perms_missing_one(report):
    perms = []
    for i in range(len(report)):
        perms.append([])
        for j in range(len(report)):
            if j == i:
                continue
            else:
                perms[i].append(report[j])
    return perms

def check_all_reports_part_2(filepath):
    list_of_reports = get_reports(filepath)
    num_of_safe_reports = 0
    for report in list_of_reports:
        report_perms = generate_all_perms_missing_one(report)
        for report_perm in report_perms:
            if check_report(report_perm):
                num_of_safe_reports += 1
                break
    return num_of_safe_reports

print("Example: ", check_all_reports_part_2(example_filepath), "\n\n")
print("Input solution: ", check_all_reports_part_2(input_filepath))
print("==============================")
