import io
from collections import deque
import numpy as np
import pulp

def parse_line(line: str) -> tuple[tuple[bool, ...], list[set[int]], tuple[int, ...]]:
    indicator_lights: tuple[bool, ...] = ()
    buttons: list[set[int]] = []
    joltages: tuple[int, ...] = ()

    cur_str = line[line.index("[") + 1:line.index("]")]
    indicator_lights = tuple([True if cur == "#" else False for cur in cur_str])
    cur_str = line[line.index("("):line.index("{") - 1]
    for cur in cur_str.split(" "):
        buttons.append(set(map(int, cur[1:-1].split(","))))
    cur_str = line[line.index("{") + 1:line.index("}")]
    joltages = tuple([int(cur) for cur in cur_str.split(",")])
    
    return indicator_lights, buttons, joltages

def min_presses(indicator_lights: tuple[bool, ...], buttons: list[set[int]]) -> int:
        queue: deque[tuple[int, tuple[bool, ...]]] = deque()
        queue.append((0, tuple([False for _ in range(len(indicator_lights))])))
        tried: set[tuple[bool, ...]] = set()
        tried.add(tuple([False for _ in range(len(indicator_lights))]))
        while len(queue) != 0:
            cur_indicators = queue.popleft()
            if cur_indicators[1] == indicator_lights:
                return cur_indicators[0]
            
            for button_combo in buttons:
                new = (cur_indicators[0] + 1, tuple([cur ^ (i in button_combo) for i, cur in enumerate(cur_indicators[1])]))
                if new[1] not in tried:
                    queue.append(new)
                    tried.add(new[1])
        
        # Shouldn't get here...
        raise RuntimeError


def min_presses_2(buttons: list[set[int]], joltages: tuple[int, ...]) -> int:
    # Build a matrix representing the data
    # Each row represents a joltage and each column represents a button. A cell is 1 if the button in that column
    # modifies the joltage in that row
    M = np.zeros((len(joltages), len(buttons)), dtype=int)
    for i, button in enumerate(buttons):
        for joltage in button:
            M[joltage][i] = 1
    
    # This solution uses an integer linear programming (ILP) library called PuLP. Although other solutions exist,
    # like a modified BFS of the solution for part 1, they take a very long time, and unfortunately, using a 3rd party
    # library is the most efficient way as this problem is np-complete
    
    # Define the ILP problem
    problem = pulp.LpProblem("buttons", pulp.LpMinimize)
    
    # Create variables, one for each button combination
    # This represents the number of time each button combo has to be pressed
    variables = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))]
    
    # Set the objective function, the sum of the variables, to the problem
    problem += pulp.lpSum(variables)
    
    # Add the constraints that each row of the matrix (the buttons that add to a specific joltage) need to 
    # add up to the joltage at that index
    for joltage_index in range(len(joltages)):
        problem += pulp.lpSum(M[joltage_index, button_index] * variables[button_index] for button_index in range(len(buttons))) == joltages[joltage_index]
    
    # Finally, solve the problem
    solver = pulp.PULP_CBC_CMD(msg=False) # This just disables all the info messages that appear
    problem.solve(solver)
    
    return sum([int(pulp.value(cur_var)) for cur_var in variables])
    
    

def part_1(f: io.TextIOWrapper) -> int:
    lines: list[tuple[tuple[bool, ...], list[set[int]], tuple[int, ...]]] = []
    for line in f.readlines():
        lines.append(parse_line(line))
        
    sum_min = 0
    for line in lines:
        cur = min_presses(line[0], line[1])
        sum_min += cur
    return sum_min


def part_2(f: io.TextIOWrapper) -> int:
    lines: list[tuple[tuple[bool, ...], list[set[int]], tuple[int, ...]]] = [parse_line(line) for line in f.readlines()]
    sum_min = 0
    for line in lines:
        print(line[1], line[2])
        cur = min_presses_2(line[1], line[2])
        sum_min += cur
    return sum_min
    

