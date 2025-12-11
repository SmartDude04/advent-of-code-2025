import io
from collections import deque


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


def count_paths(adj_list: dict[str, set[str]]) -> int:
    topo_order: list[str] = topological_sort(adj_list)
    
    ways: dict[str, int] = {node:0 for node in adj_list.keys()}
    ways["you"] = 1
    
    for node in topo_order:
        for neighbor in adj_list[node]:
            ways[neighbor] += ways[node]
            
    return ways["out"]

def part_1(f: io.TextIOWrapper) -> int:
    adj_list: dict[str, set[str]] = {}
    nodes_set: set[str] = set()
    
    for line in f.readlines():
        node, edges = (line.split(":")[0], line.strip().split(": ")[1].split(" "))
        adj_list[node] = set(edges)
        nodes_set.update(adj_list[node])
    
    for node in nodes_set:
        if node not in adj_list.keys():
            adj_list[node] = set()
        
    return count_paths(adj_list)