import io
from collections import deque

def parse_line(line: str) -> tuple[tuple[bool, ...], list[tuple[int, ...]], list[int]]:
    indicator_lights: tuple[bool, ...] = ()
    buttons: list[tuple[int, ...]] = []
    joltages: list[int] = []

    cur_str = line[line.index("[") + 1:line.index("]")]
    indicator_lights = tuple([True if cur == "#" else False for cur in cur_str])
    cur_str = line[line.index("("):line.index("{") - 1]
    for cur in cur_str.split(" "):
        buttons.append(tuple(map(int, cur[1:-1].split(","))))
    cur_str = line[line.index("{") + 1:line.index("}")]
    joltages = [int(cur) for cur in cur_str.split(",")]
    
    return indicator_lights, buttons, joltages

def min_presses(indicator_lights: tuple[bool, ...], buttons: list[tuple[int, ...]]) -> int:
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
        

def part_1(f: io.TextIOWrapper) -> int:
    lines: list[tuple[tuple[bool, ...], list[tuple[int, ...]], list[int]]] = []
    for line in f.readlines():
        lines.append(parse_line(line))
        
    sum_min = 0
    for line in lines:
        cur = min_presses(line[0], line[1])
        sum_min += cur
    return sum_min
    

