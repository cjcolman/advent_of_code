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
print(present_area)