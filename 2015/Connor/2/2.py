# %%
def parse_input(file_path):
    with open(file_path) as f:
        data = f.read().split('\n')
    return [(int(x[0]),int(x[1]),int(x[2])) for x in [line.split('x') for line in data]]

# %%
def get_wrapping_paper_needed(dimensions):
    total_paper = 0
    for l, w, h in dimensions:
        side1 = l * w
        side2 = w * h
        side3 = h * l
        smallest_side = min(side1, side2, side3)
        total_paper += 2 * (side1 + side2 + side3) + smallest_side
    return total_paper

# %%
print(get_wrapping_paper_needed(parse_input('input.txt')))

# %%
def get_ribbon_around(dimensions):
    total_ribbon = 0
    for l, w, h in dimensions:
        dim_list = [l,w,h]
        dim_list.remove(max(dim_list))
        total_ribbon += 2 * (dim_list[0] + dim_list[1])
    return total_ribbon

# %%
def get_ribbon_bow(dimensions):
    total_ribbon = 0
    for l, w, h in dimensions:
        total_ribbon += l * w * h
    return total_ribbon

# %%
print(get_ribbon_around(parse_input('input.txt')) + get_ribbon_bow(parse_input('input.txt')))

# %%