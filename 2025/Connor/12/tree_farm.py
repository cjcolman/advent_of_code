# %%
from pathlib import Path

HERE = Path(__file__).parent
MODE = "input"
if MODE == "example":
    file = HERE / "example.txt"
else:
    file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read()

# %%
present_area = {int(present.split(":")[0]): present.split(":")[1].count('#') for 
                present in DATA.split("\n\n")[:-1]}
# %%
tree_area = [
    [int(tree[0:2])*int(tree[3:5])] + [int(i) for i in tree.split(": ")[1].split(" ")] for tree in DATA.split("\n\n")[-1].split("\n")
]
# %%
running_total = 0
for ctree in tree_area:
    area = ctree.pop(0)
    total_present_area = 0
    for present_index, present_count in enumerate(ctree):
        total_present_area += present_count * present_area[present_index]
    if total_present_area > area:
        continue
    else:
        running_total += 1
        continue

print(running_total)