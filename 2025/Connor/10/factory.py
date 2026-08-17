# %%
"""
This module contains functions for formatting machine configurations and solving the LED
button problem using Gaussian elimination.
"""
from pathlib import Path
from itertools import product
import numpy as np


HERE = Path(__file__).parent
MODE = "input"
if MODE == "example":
    file = HERE / "example.txt"
else:
    file = HERE / "input.txt"

with open(file, "r", encoding="utf-8") as f:
    DATA = f.read().strip().splitlines()

# %%
def format_machine_on_off(machine: str):
    """Format the machine string into a numpy array, where the final column is the led goal state, 
        and the other columns are the buttons, where a 1 represents an led flip.
       e.g. [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1)
       -->
       0 0 0 0 1 1 0
       0 1 0 0 0 1 1
       0 0 1 1 1 0 1
       1 1 0 1 0 0 0
       note, that the number of leds and the number of buttons isn't fixed.
       """

    # Split the machine string into parts
    parts = machine.split(" ")
    led_state = parts[0].strip("[]")
    button_states = [tuple(map(int, part.strip("()").split(","))) for part in parts[1:]]

    # Determine the number of LEDs and buttons
    num_leds = len(led_state)
    num_buttons = len(button_states)

    # Create a numpy array to hold the machine configuration
    machine_array = np.zeros((num_leds, num_buttons + 1), dtype=int)

    # Fill in the LED goal state
    for i in range(num_leds):
        if led_state[i] == "#":
            machine_array[i, -1] = 1

    # Fill in the button states
    for j, button in enumerate(button_states):
        for led_index in button:
            machine_array[led_index, j] = 1

    return machine_array

# %%
def gaussian_elimination(matrix: np.ndarray, part_1: bool = True):
    """
    matrix: machine array
    Perform Gaussian elimination on the machine array to find the solution for the LED goal
    state. The last column of the machine array represents the LED goal state, and the other columns
    represent the buttons. Because a repeated press of a button is equivalent to not pressing it at
    all, we can perform the elimination modulo 2. This function returns the reduced matrix, and the
    pivot columns.
    """
    matrix = matrix.copy()
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    num_vars = num_cols - 1
    pivot_row = 0
    pivot_cols = []
    for col in range(num_vars):
        # Find a row at or below pivot row that has a 1 in this column
        swap_row = None
        for row in range(pivot_row, num_rows):
            if (part_1 and matrix[row, col] == 1) or (
                not part_1 and matrix[row, col] != 0
            ):
                swap_row = row
                break

        # No pivot available in this column therefore this variable is free
        if swap_row is None:
            continue

        # Move the pivot into position
        matrix[[pivot_row, swap_row]] = matrix[[swap_row, pivot_row]]
        pivot_cols.append(col)

        # Eliminate the variable from every other row
        for row in range(0, num_rows):
            if row == pivot_row:
                continue
            if matrix[row, col] == 1 and part_1:
                matrix[row] ^= matrix[pivot_row]
            if matrix[row, col] != 0 and not part_1:
                factor = matrix[row, col]
                pivot_value = matrix[pivot_row, col]

                matrix[row] = (
                    pivot_value * matrix[row]
                    - factor * matrix[pivot_row]
                )

        pivot_row += 1

        # We've used all available rows
        if pivot_row == num_rows:
            break

    return matrix, pivot_cols

# %%
def find_minimum_solution(matrix, pivot_cols, part_1=True, max_jolts=0, button_bounds=None):
    """Given a reduced matrix and the pivot columns, find the minimum solution to the system of
    equations. The minimum solution is the one with the fewest number of button presses (i.e., the
    fewest number of 1s in the solution vector).
    """
    num_cols = matrix.shape[1]
    num_vars = num_cols - 1

    free_cols = [
        col
        for col in range(num_vars)
        if col not in pivot_cols
    ]

    min_presses = np.inf
    best_solution = None

    if part_1:
        check_values = product([0,1], repeat=len(free_cols))
    if not part_1:
        ranges = [
            range(button_bounds[col] + 1)
            for col in free_cols
        ]

        check_values = product(*ranges)

    for values in check_values:
        x = np.zeros(num_vars, dtype=int)

        # ------------------
        # Set free variables
        # ------------------

        for free_col, value in zip(free_cols, values):
            x[free_col] = value

        # ---------------------
        # Solve pivot variables
        # ---------------------
        if part_1:
            for row, pivot_col in enumerate(pivot_cols):
                result = matrix[row,-1]

                other_terms = 0

                for col in range(num_vars):
                    if col != pivot_col and matrix[row, col] == 1:
                        other_terms ^= x[col]

                x[pivot_col] = result ^ other_terms
        if not part_1:
            valid_solution = True

            for row, pivot_col in enumerate(pivot_cols):
                result = matrix[row, -1]

                for free_col in free_cols:
                    result -= matrix[row, free_col] * x[free_col]

                pivot_value = matrix[row, pivot_col]

                # Button presses must be whole numbers
                if result % pivot_value != 0:
                    valid_solution = False
                    break

                x[pivot_col] = result // pivot_value

            if not valid_solution:
                continue

        if np.any(x < 0):
            continue
        presses = x.sum()

        if presses < min_presses:
            min_presses = presses
            best_solution = x.copy()

    return min_presses, best_solution

# %%
def get_total_minimum_presses(data, part_1):
    """Given a list of machine strings, find the total minimum number of button presses required to
    achieve the LED goal state for all machines.
    """
    total_min_presses = 0

    for machine in data:
        if part_1:
            machine_str = machine.split(" {")[0]
            machine_array = format_machine_on_off(machine_str)
            max_jolts = 0
        else:
            machine_str = machine.split("] ")[1]
            machine_array = format_machine_joltages(machine_str)
            max_jolts = max([row[-1] for row in machine_array])
        if part_1:
            button_bounds = None
        else:
            button_bounds = get_button_bounds(machine_array)

        reduced_matrix, pivot_cols = gaussian_elimination(machine_array, part_1)

        min_presses, _ = find_minimum_solution(
            reduced_matrix,
            pivot_cols,
            part_1,
            max_jolts,
            button_bounds
        )
        total_min_presses += min_presses

    return total_min_presses
# %%
print("Part 1:", get_total_minimum_presses(DATA, part_1=True))

# %%
def get_button_bounds(matrix):
    num_vars = matrix.shape[1] - 1
    targets = matrix[:, -1]

    bounds = []

    for col in range(num_vars):
        affected_rows = np.where(matrix[:, col] == 1)[0]

        bound = min(targets[row] for row in affected_rows)
        bounds.append(int(bound))

    return bounds
# %%
def format_machine_joltages(machine: str):
    """Format the machine string into a numpy array, where the final column is the joltage goal
    state, and the other columns are the buttons, where a 1 represents an led flip.           
    e.g. (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
           -->
           0 0 0 0 1 1 3
           0 1 0 0 0 1 5
           0 0 1 1 1 0 4
           1 1 0 1 0 0 7
           note, that the number of leds and the number of buttons isn't fixed.
           """
    # Split the machine string into parts
    parts = machine.split(" ")
    button_states = [tuple(map(int, part.strip("()").split(","))) for part in parts[:-1]]
    joltage_goal_state = list(map(int, parts[-1].strip("{}").split(",")))

    # Determine the number of LEDs and buttons
    num_leds = len(joltage_goal_state)
    num_buttons = len(button_states)

    # Create a numpy array to hold the machine configuration
    machine_array = np.zeros((num_leds, num_buttons + 1), dtype=int)

    # Fill in the joltage goal state
    for i in range(num_leds):
        machine_array[i, -1] = joltage_goal_state[i]

    # Fill in the button states
    for j, button in enumerate(button_states):
        for led_index in button:
            machine_array[led_index, j] = 1

    return machine_array


# %%
print("Part 2:", get_total_minimum_presses(DATA, part_1=False))

# %%
