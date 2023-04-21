def create_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
    if not edges: return []

    # Create Vertices from Edges
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    
    # Map vertices to unique integer indexes
    mappings = {}
    index = 0
    for vertex in vertices:
        mappings[vertex] = index
        index += 1

    # Make Matrix of 0s - V X V matrix
    matrix = [[0 for i in range(len(vertices))] for j in range(len(vertices))]

    # Change the matrix edges to 1
    for edge in edges:
        source_index = mappings[edge[0]]
        destination_index = mappings[edge[1]]
        matrix[source_index][destination_index] = 1
    return matrix, mappings

edges = [
    ('Danielle', 'Amanda'),
    ('Amanda', 'Katherine'),
    ('Amanda', 'Dana'),
    ('Dana', 'Samantha'),
    ('Samantha', 'Danielle')
]

print(create_adjacency_matrix(edges))
