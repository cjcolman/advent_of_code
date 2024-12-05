print("Part 1:")
print("==============================")

input_filepath = "./input_05.txt"
example_filepath = "./example_05.txt"

def parse_input(filepath):
    text = open(filepath).read().split("\n\n")
    rules = [i.split("|") for i in text[0].split("\n")]
    pages = [j.split(",") for j in text[1].split("\n")]
    return rules, pages

def get_relevant_rules(rules, page):
    page_set = set(page)
    valid_rules = []
    for rule in rules:
        if set(rule) <= page_set:
            valid_rules.append(rule)

    return valid_rules

def is_valid_page(valid_rules, page):
    page_str = '.'.join(page)
    for rule in valid_rules:
        x = [page_str.find(i) for i in rule]
        if x[1] < x[0]:
            return False
    else:
        return True
    
def get_middle_value(page):
    return int(page[int((len(page)-1)/2)])

def get_all_middle_values(filepath):
    rules, pages = parse_input(filepath)
    cum_sum = 0
    for page in pages:
        valid_rules = get_relevant_rules(rules,page)
        if is_valid_page(valid_rules, page):
            cum_sum += get_middle_value(page)
    return cum_sum

print("Example: ", get_all_middle_values(example_filepath), "\n\n")
print("Input solution: ", get_all_middle_values(input_filepath))
print("==============================")

print("Part 2:")
print("==============================")

def reorder(valid_rules, page):
    page_str = '.'.join(page)
    for rule in valid_rules:
        x = [page_str.find(i) for i in rule]
        if x[1] < x[0]:
            for i in range(len(page)):
                if page[i] == rule[0]:
                    a = i
                if page[i] == rule[1]:
                    b = i
            new_page = ['' for _ in range(len(page))]

            for i in range(len(page)):
                if i == a:
                    new_page[i] = rule[1]
                elif i == b:
                    new_page[i] = rule[0]
                else:
                    new_page[i] = page[i]

    if is_valid_page(valid_rules, new_page):
        return new_page
    
    else:
        return reorder(valid_rules, new_page)

def get_all_middle_values_part_2(filepath):
    rules, pages = parse_input(filepath)
    cum_sum = 0
    for page in pages:
        valid_rules = get_relevant_rules(rules,page)
        if is_valid_page(valid_rules, page):
            continue
        else:
            reordered_page = reorder(valid_rules, page)
            cum_sum += get_middle_value(reordered_page)

    return cum_sum

print("Example: ", get_all_middle_values_part_2(example_filepath), "\n\n")
print("Input solution: ", get_all_middle_values_part_2(input_filepath))
print("==============================")



