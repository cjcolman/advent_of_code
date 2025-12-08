# %%
def parse_input(filepath):#
    with open(filepath) as f:
        lines = f.readlines()
        data = [line.split() for line in lines]
    output = [[] for _ in range(len(data[0]))]
    for i in range(len(data[0])):
        for j in range(len(data)):
            output[i].append(data[j][i])
    return output

# %%
def perform_operation(data):
    local_vars = {}
    op_str = "output = " + data[-1].join(data[:-1])
    exec(op_str, {}, local_vars)
    return local_vars['output']

# %%
def sum_all_operations(file_path):
    list_of_operations = parse_input(file_path)
    total = 0
    for operation in list_of_operations:
        total += perform_operation(operation)
    return total

# %%
print("Example: ", sum_all_operations("example.txt"), " Expected: 4277556")

print("Part 1: ", sum_all_operations("input.txt"))

# %%
def parse_input_p2(filepath):
    with open(filepath) as f:
        data = [list(x) for x in f.read().split("\n")]
    max_len = max([len(x) for x in data])
    for i, l in enumerate(data):
        extra = max_len - len(l)
        for _ in range(extra):
            data[i].append('')

    output = [[] for i in range(len(data))]
    n = 0
    while data[0]:
        try:
            for i in range(len(data)):
                output[n].append(data[i].pop(-1))
            n += 1
        except IndexError:
            break
    return output


# %%
print(parse_input_p2("example.txt"))

# %%
