# %%
from pathlib import Path
from functools import cache

HERE = Path(__file__).parent
MODE = "input"
if MODE == "example":
    file = HERE / "example.txt"
else:
    file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read().strip().splitlines()

# %%
print(DATA)
# %%
schematic = {s.split(":")[0]: s.split(":")[1].strip().split(" ") for s in DATA}
# %%
print(schematic)
# %%
@cache
def get_num_of_paths(name):
    if name == "out":
        return 1
    total_paths = 0
    for next_name in schematic[name]:
        total_paths += get_num_of_paths(next_name)
    return total_paths
# %%
print(get_num_of_paths("you"))

# %%
@cache
def get_num_of_allowed_paths(name, dac_flag=False, fft_flag=False):
    if name == "out" and dac_flag and fft_flag:
        return 1
    elif name == "out":
        return 0
    total_paths = 0
    for next_name in schematic[name]:
        new_dac_flag = dac_flag or name == "dac"
        new_fft_flag = fft_flag or name == "fft"
        total_paths += get_num_of_allowed_paths(next_name, new_dac_flag, new_fft_flag)
    return total_paths
# %%
print(get_num_of_allowed_paths("svr"))
# %%
