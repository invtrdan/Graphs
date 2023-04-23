from collections import defaultdict, deque
from tree_node import *

def create_adjacency_list(edges: list[list[str]]) -> dict:
    if not edges: return {}

    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph

edges = [
    ('Danielle', 'Amanda'),
    ('Amanda', 'Katherine'),
    ('Amanda', 'Dana'),
    ('Dana', 'Samantha'),
    ('Samantha', 'Danielle')
]

print(create_adjacency_list(edges))