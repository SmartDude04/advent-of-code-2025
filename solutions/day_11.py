import io
from collections import deque

def construct_adj_list(f: io.TextIOWrapper) -> dict[str, set[str]]:
    adj_list: dict[str, set[str]] = {}
    nodes_set: set[str] = set()
    
    for line in f.readlines():
        node, edges = (line.split(":")[0], line.strip().split(": ")[1].split(" "))
        adj_list[node] = set(edges)
        nodes_set.update(adj_list[node])
    
    for node in nodes_set:
        if node not in adj_list.keys():
            adj_list[node] = set()
    return adj_list

def topological_sort(adj_list: dict[str, set[str]]) -> list[str]:
    in_degree: dict[str, int] = {node:0 for node in adj_list.keys()}
    for node, edges in adj_list.items():
        for edge in edges:
            in_degree[edge] += 1
    
    queue: deque[str] = deque()
    for node in adj_list.keys():
        if in_degree[node] == 0:
            queue.append(node)
            
    topological_order: list[str] = []
    while len(queue) != 0:
        cur = queue.popleft()
        topological_order.append(cur)
        
        for edge in adj_list[cur]:
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                queue.append(edge)
    
    return topological_order


def count_paths(adj_list: dict[str, set[str]], from_node: str, to_node: str) -> int:
    topo_order: list[str] = topological_sort(adj_list)
    
    ways: dict[str, int] = {node:0 for node in adj_list.keys()}
    ways[from_node] = 1
    
    for node in topo_order:
        for neighbor in adj_list[node]:
            ways[neighbor] += ways[node]
            
    return ways[to_node]
    

def part_1(f: io.TextIOWrapper) -> int:
    adj_list: dict[str, set[str]] = construct_adj_list(f)        
    return count_paths(adj_list, "you", "out")


def part_2(f: io.TextIOWrapper) -> int:
    adj_list: dict[str, set[str]] = construct_adj_list(f)
    svr_fft = count_paths(adj_list, "svr", "fft")
    fft_dac = count_paths(adj_list, "fft", "dac")
    dac_out = count_paths(adj_list, "dac", "out")
    svr_fft_dac_out = svr_fft * fft_dac * dac_out
    
    svr_dac = count_paths(adj_list, "svr", "dac")
    dac_fft = count_paths(adj_list, "dac", "fft")
    fft_out = count_paths(adj_list, "fft", "out")
    svr_dac_fft_out = svr_dac * dac_fft * fft_out
    
    return svr_dac_fft_out + svr_fft_dac_out