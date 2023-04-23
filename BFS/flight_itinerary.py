from collections import *

'''
Write a function that takes:
- A list of tuples called flights
    - Each tuple is a (src,dst) city pair representing a one-way flight
- A home city (string)
- A vacation city (string)

And returns:
- A list containing all the cities along the shortest path from home to vacation
'''

def shortest_flights(flights: list[tuple], home: str, vacation: str) -> list[str]:
    def make_graph(flghts: list[tuple]) -> dict:  # makes a graph from the edges
        # Base Case
        if not flights: return {}

        # Directed Graph
        graph = defaultdict(set)
        for src, dst in flights: graph[src].add(dst)
        return graph
    # 1. Make Graph
    graph = make_graph(flights)
    print(graph)

    # 2. Base Cases
    if not graph: return []
    if home == vacation: return [home]

    # 3. Create tracking variables
    Q = deque()
    visited = set()

    # 4. Intake starting position of the first level
    # In shortest path, we also want to intake the shortest path.
    Q.append((home,[])) # home, path (how we got to the node)

    # 5. Process the Queue
    while Q:
        # 6. Get the node for processing
        src, path = Q.popleft()
        # Check if you've been there before
        if src in visited: continue
        visited.add(src)
        # Check of you have solved the problem
        if src == vacation: 
            path.append(vacation) # push
            return path
        # Process Neighbors
        path.append(src)
        for neighbor in graph.get(src, []):
            Q.append((neighbor,path[:]))
    return []


flights = {
    ('Detroit', 'Seattle'),
    ('Seattle', 'Portland'),
    ('Seattle', 'Vancouver'),
    ('Portland', 'Los Angeles'),
    ('Los Angeles', 'Las Vegas'),
    ('Los Angeles', 'San Francisco'),
    ('Vancouver', 'Las Vegas'),
    ('Vancouver', 'Toronto')
}
home = 'Detroit'
vacation = 'Portland'
print(shortest_flights(flights, home, vacation))




