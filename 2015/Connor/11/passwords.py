"""
Advent of Code 2015 - Day 11
"""
# %%
EXAMPLE_1 = "abcdefgh"
EXAMPLE_2 = "ghijklmn"
TEST_1 = "abcdffaa"
TEST_2 = "ghjaabcc"

INPUT_PASSWORD = "hxbxwxba"
# %%
def increment_password(password: str) -> str:
    """Return the next password in the Advent of Code 2015 password sequence."""
    working_str = list(password[::-1])
    for i, l in enumerate(working_str):
        if l == "z":
            working_str[i] = "a"
            continue
        else:
            working_str[i] = chr(ord(l)+1)
            return ''.join(working_str[::-1])
    return "a" + ''.join(working_str[::-1])

# %%
def flag_1(password: str) -> bool:
    """Return whether the password contains a straight of three consecutive letters."""
    for i in range(5):
        if (ord(password[i]) + 1 == ord(password[i+1])) & \
           (ord(password[i+1]) + 1 == ord(password[i+2])):
            return True
    return False

def flag_2(password: str) -> bool:
    """Return whether the password does not contain forbidden letters."""
    return ("i" not in password) & ("o" not in password) & ("l" not in password)

def flag_3(password: str) -> bool:
    """Return whether the password contains two different non-overlapping pairs."""
    first_pair = None
    i = 0

    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            current_pair = password[i]
            if first_pair is None:
                first_pair = current_pair
            elif current_pair != first_pair:
                return True
            i += 2
            continue
        i += 1
    return False

def is_valid_password(password: str) -> bool:
    """Return whether the password satisfies all Advent of Code 2015 rules."""
    return flag_1(password) & flag_2(password) & flag_3(password)


# %%
def get_next_valid_password(password: str) -> str:
    """Return the next valid password in the sequence."""
    while not is_valid_password(password):
        password = increment_password(password)
    return password
# %%
assert TEST_1 == get_next_valid_password(EXAMPLE_1)
assert TEST_2 == get_next_valid_password(EXAMPLE_2)

# %%
print("=== Part 1 ===")
print(get_next_valid_password(INPUT_PASSWORD))
# %%
print("=== Part 2 ===")
print(get_next_valid_password(increment_password(get_next_valid_password(INPUT_PASSWORD))))
