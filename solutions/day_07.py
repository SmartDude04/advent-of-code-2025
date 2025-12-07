import functools
import io

def part_1(f: io.TextIOWrapper) -> int:
    def move_beam(cur_line: int) -> int:
        cur_num_split = 0
        new_beam = [0 for _ in range(len(beam))]
        for i, (cur_beam, cur_manifold) in enumerate(zip(beam, manifold[cur_line])):
            if cur_manifold == "^" and cur_beam == 1:
                cur_num_split += 1
                new_beam[i - 1] = 1
                new_beam[i + 1] = 1
            elif new_beam[i] == 0:
                new_beam[i] = cur_beam
        
        for i, v in enumerate(beam):
            beam[i] = new_beam[i]
        return cur_num_split
            
        
    manifold: list[str] = [line.strip() for line in f.readlines()]
    beam: list[int] = [1 if char == "S" else 0 for char in manifold[0]]
    
    num_split = 0
    for i in range(1, len(manifold)):
        num_split += move_beam(i)
    return num_split


def part_2(f: io.TextIOWrapper) -> int:
    @functools.cache
    def num_timelines(particle_pos: tuple[int, int]) -> int:
        assert manifold[particle_pos[0]][particle_pos[1]] != "^"
        # Base case
        if particle_pos[0] == len(manifold) - 1:
            return 1
        
        # Look at the next position and split if needed
        if manifold[particle_pos[0] + 1][particle_pos[1]] == "^":
            return num_timelines((particle_pos[0] + 1, particle_pos[1] - 1)) + num_timelines((particle_pos[0] + 1, particle_pos[1] + 1))
        else:
            return num_timelines((particle_pos[0] + 1, particle_pos[1]))
    
    manifold: list[str] = [line.strip() for line in f.readlines()]
    start_position: tuple[int, int] = (1, manifold[0].index("S"))
    
    return num_timelines(start_position)
