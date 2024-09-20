# %% Inputs

with open(r"19\input.txt") as f:
    lines = f.read()

# with open(r"19\example.txt") as f:
#     lines = f.read()

workflows = lines.split("\n\n")[0]
parts = lines.split("\n\n")[1]

# %% Part 1
class Workflow:
    def __init__(self, params: str):
        self.steps = params.split(",")
        
class Part:
    def __init__(self, categories: str):
        categories_list = categories.split(",")
        self.categories = {}
        self.categories["x"] = int(categories.split(",")[0].split("=")[1])
        self.categories["m"] = int(categories.split(",")[1].split("=")[1])
        self.categories["a"] = int(categories.split(",")[2].split("=")[1])
        self.categories["s"] = int(categories.split(",")[3].split("=")[1])

def is_part_accepted(part, workflows_map):
    action = "in"
    while True:
        workflow = workflows_map[action]
        for step in workflow.steps:
            if ":" in step:
                action = step.split(":")[1]
                category = step[0] # x, m, a, s
                if "<" in step:
                    expr = step.split(":")[0]
                    condition = part.categories[category] < int(expr.split("<")[1])
                elif ">" in step:
                    expr = step.split(":")[0]
                    condition = part.categories[category] > int(expr.split(">")[1])
                else:
                    raise Exception("sumthin wrongo")
            else:
                action = step
                condition = True

            if condition:
                if action == "A":
                    return True
                elif action == "R":
                    # rejected
                    return False
                else:
                    workflow = workflows_map[action]
                    break


def total_parts_value(accepted_parts_list):
    total = 0
    for part in accepted_parts_list:
        for category_score in part.categories.values():
            total += category_score
    return total

workflows = workflows.split("\n")
workflows_map = {workflow.split("{")[0]: Workflow(workflow.split("{")[1][:-1]) for workflow in workflows}
workflows_map_2 = {workflow.split("{")[0]: workflow.split("{")[1][:-1] for workflow in workflows}

parts_list = [Part(part.replace("{", "").replace("}", "")) for part in parts.split("\n")]

accepted_parts_list = []
for part in parts_list:
    if is_part_accepted(part, workflows_map):
        accepted_parts_list.append(part)
    else:
        continue

print(total_parts_value(accepted_parts_list))

# %%
def get_new_ranges(x_range, m_range, a_range, s_range, condition):
    if "<" in condition:
        number = int(condition.split("<")[1])
        if "x" in condition:
            x_range_1 = range(min(x_range), number)
            x_range_2 = range(number, max(x_range)+1)
            m_range_1 = m_range
            m_range_2 = m_range
            a_range_1 = a_range
            a_range_2 = a_range
            s_range_1 = s_range
            s_range_2 = s_range
        elif "m" in condition:
            x_range_1 = x_range
            x_range_2 = x_range
            m_range_1 = range(min(m_range), number)
            m_range_2 = range(number, max(m_range)+1)
            a_range_1 = a_range
            a_range_2 = a_range
            s_range_1 = s_range
            s_range_2 = s_range
        elif "a" in condition:
            x_range_1 = x_range
            x_range_2 = x_range
            m_range_1 = m_range
            m_range_2 = m_range
            a_range_1 = range(min(a_range), number)
            a_range_2 = range(number, max(a_range)+1)
            s_range_1 = s_range
            s_range_2 = s_range
        elif "s" in condition:
            x_range_1 = x_range
            x_range_2 = x_range
            m_range_1 = m_range
            m_range_2 = m_range
            a_range_1 = a_range
            a_range_2 = a_range
            s_range_1 = range(min(s_range), number)
            s_range_2 = range(number, max(s_range)+1)
        else:
            raise Exception("Sumting wronggo")
    elif ">" in condition:
        number = int(condition.split(">")[1])
        if "x" in condition:
            x_range_1 = range(number+1, max(x_range)+1)
            x_range_2 = range(min(x_range), number+1)
            m_range_1 = m_range
            m_range_2 = m_range
            a_range_1 = a_range
            a_range_2 = a_range
            s_range_1 = s_range
            s_range_2 = s_range
        elif "m" in condition:
            x_range_1 = x_range
            x_range_2 = x_range
            m_range_1 = range(number+1, max(m_range)+1)
            m_range_2 = range(min(m_range), number+1)
            a_range_1 = a_range
            a_range_2 = a_range
            s_range_1 = s_range
            s_range_2 = s_range
        elif "a" in condition:
            x_range_1 = x_range
            x_range_2 = x_range
            m_range_1 = m_range
            m_range_2 = m_range
            a_range_1 = range(number+1, max(a_range)+1)
            a_range_2 = range(min(a_range), number+1)
            s_range_1 = s_range
            s_range_2 = s_range
        elif "s" in condition:
            x_range_1 = x_range
            x_range_2 = x_range
            m_range_1 = m_range
            m_range_2 = m_range
            a_range_1 = a_range
            a_range_2 = a_range
            s_range_1 = range(number+1, max(s_range)+1)
            s_range_2 = range(min(s_range), number+1)
        else:
            raise Exception("Sumting else wronggo")
    return x_range_1, m_range_1, a_range_1, s_range_1, x_range_2, m_range_2, a_range_2, s_range_2


def find_combo_number(x_range, m_range, a_range, s_range, workflows_map, actions):
    steps = actions.split(",")
    if len(steps) == 1:
        if steps[0] == "A":
            return (max(x_range)-min(x_range)+1)*(max(m_range)-min(m_range)+1)*(max(a_range)-min(a_range)+1)*(max(s_range)-min(s_range)+1)
        if steps[0] == "R":
            return 0
        else:
            actions = workflows_map[steps[0]]
            return find_combo_number(x_range, m_range, a_range, s_range, workflows_map, actions)
    else:
        condition = steps[0].split(":")[0]
        action = steps[0].split(":")[1]
        next_actions = ",".join(steps[1:])
        x_range_1, m_range_1, a_range_1, s_range_1, x_range_2, m_range_2, a_range_2, s_range_2 = get_new_ranges(x_range, m_range, a_range, s_range, condition)
        return find_combo_number(x_range_1, m_range_1, a_range_1, s_range_1, workflows_map, action) + find_combo_number(x_range_2, m_range_2, a_range_2, s_range_2, workflows_map, next_actions)

# %%
x_range = range(1,4001)
m_range = range(1,4001)
a_range = range(1,4001)
s_range = range(1,4001)

print(find_combo_number(x_range, m_range, a_range, s_range, workflows_map_2, "in"))
