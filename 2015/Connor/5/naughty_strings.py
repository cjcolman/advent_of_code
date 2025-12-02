# %%
import re

def parse_input(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

# %%
def is_naughty_string(string):
    vowels = re.compile("[aeiou]")
    matches = vowels.findall(string)
    if len(matches) < 3: return True
    else:
        double_letter = re.compile(r"(\w)\1")
        matches = double_letter.findall(string)
        if len(matches) == 0: return True
        else:
            bad_strings = ['ab', 'cd', 'pq', 'xy']
            for s in bad_strings:
                pattern = re.compile(s)
                if len(pattern.findall(string)) > 0:
                    return True
    return False

# %%
def how_many_nice_strings(strings):
    total = 0
    for s in strings:
        if not is_naughty_string(s):
            total+= 1
    return total
# %%
print(how_many_nice_strings(parse_input("input.txt")))
# %%
def is_naughty_string_v2(string):
    doubles = r"(\w\w).*\1"
    pattern = re.compile(doubles)
    if len(pattern.findall(string)) == 0: return True
    else:
        cond_str = r"(\w).\1"
        pattern = re.compile(cond_str)
        if len(pattern.findall(string)) == 0: return True
    return False

def how_many_nice_strings_v2(strings):
    total = 0
    for s in strings:
        if not is_naughty_string_v2(s):
            total+= 1
    return total

# %%
print(how_many_nice_strings_v2(parse_input("input.txt")))