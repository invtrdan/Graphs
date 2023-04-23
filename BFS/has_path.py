from collections import *
'''
Given an undirected graph as a list of edges, determine if a path exists between two vertices.
n: number of vertices
edges: 2D list of edges
source
destination
'''

def has_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # What is the input? Is it a graph/edges.
    # In this case, the input is a list of edges.

    # Step 1: Create a helper function that builds a graph from the list of edges.
    def build_graph(edges: list[list[int]]) -> dict:
        # undirected graph
        if not edges: return {}
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0]) # undirected graph
        return graph
    graph = build_graph(edges)

    # Step 2: Check Base Cases
    if not graph: return False
    if source == destination: return True

    # Step 3: Define tracking variables
    Q = deque() # to do the bfs
    visited = set()

    # Step 4: Intake start / first level
    Q.append(source)

    # Step 5: Process Queue
    while Q:
        # Step 6: Get the node (from the Queue) for processing
        node = Q.popleft() # removes from the front

        # Step 7: Process the node
        # Step 7.1: Check if you've already been at that node
        if node in visited: continue
        visited.add(node)
        # Step 7.2: Check if we have solved the problem
        if node == destination: return True

        # Step 8: Intake neighbors for processing
        for neighbor in graph.get(node, []):
            Q.append(neighbor)
    return False


'''
Example 1
   1
  / \ 
 0 - 2
 
'''
edges = [[0,1], [1,2], [2,0]]
source = 0
destination = 2
n = 3
print(has_path(n, edges, source, destination))

'''
Example 2
   0       3
  / \     / \
 1   2   5 - 4

'''
edges = [[0,1], [0,2], [3,5], [5,4], [4,3]]
source = 0
destination = 5
n = 6
print(has_path(n, edges, source, destination))
