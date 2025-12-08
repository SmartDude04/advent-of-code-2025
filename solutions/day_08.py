import io
import math
from typing import cast
from collections import deque
from functools import reduce
from operator import mul

def connect_nodes(nodes: list[tuple[int, int, int]]) -> dict[float, tuple[tuple[int, int, int], tuple[int, int, int]]]:
    edges: dict[float, tuple[tuple[int, int, int], tuple[int, int, int]]] = {}
    for i, node1 in enumerate(nodes):
        for node2 in nodes[i + 1:]:
            dist = math.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2 + (node2[2] - node1[2])**2)
            # Adding directly and not to a list is safe as no unique edges are the same distance
            edges[dist] = (node1, node2)
    return edges

def bfs(adj_list: dict[tuple[int, int, int], list[tuple[tuple[int, int, int], float]]], start_node: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    nodes: set[tuple[int, int, int]] = set()
    queue: deque[tuple[int, int, int]] = deque()
    queue.append(start_node)
    while len(queue) != 0:
        cur = queue.popleft()
        for edge in adj_list[cur]:
            if edge[0] not in nodes:
                nodes.add(edge[0])
                queue.append(edge[0])
    return nodes

def n_largest_connected_components(adj_list: dict[tuple[int, int, int], list[tuple[tuple[int, int, int], float]]], n: int) -> int:
    
    visited: set[tuple[int, int, int]] = set()
    components_size: list[int] = []
    for node, edges in adj_list.items():
        if node not in visited:
            bfs_res = bfs(adj_list, node)
            visited |= bfs_res
            components_size.append(len(bfs_res))
    components_size.sort()
    return reduce(mul, components_size[len(components_size) - n:])
        

def part_1(f: io.TextIOWrapper) -> int:
    nodes: list[tuple[int, int, int]] = cast(list[tuple[int, int, int]], [tuple(map(int, line.strip().split(","))) for line in f.readlines()])
    edges = connect_nodes(nodes)
    
    distances: list[float] = list(edges.keys())
    distances.sort()
    
    # Make a graph using the n shortest distances
    adj_list: dict[tuple[int, int, int], list[tuple[tuple[int, int, int], float]]] = {}
    for i in range(1000):
        node1, node2 = edges[distances[i]]
        if node1 not in adj_list.keys():
            adj_list[node1] = []
        if node2 not in adj_list.keys():
            adj_list[node2] = []
        adj_list[node1].append((node2, distances[i]))
        adj_list[node2].append((node1, distances[i]))
    
    return n_largest_connected_components(adj_list, 3)


def part_2(f: io.TextIOWrapper) -> int:
    pass