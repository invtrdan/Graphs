edges = [
    ('Danielle', 'Amanda'),
    ('Amanda', 'Katherine'),
    ('Amanda', 'Dana'),
    ('Dana', 'Samantha'),
    ('Samantha', 'Danielle')
]

'''

VERTICES (5 vertices)
   0        1        2      3       4
Danielle Samantha Amanda Katherine Dana    

4 X 4 matrix
   0  1  2  3  4
0  0  0  0  0  0
1  0  0  0  0  0
2  0  0  0  0  0
3  0  0  0  0  0
4  0  0  0  0  0

'''


'''
Construct the set of unique people (nodes)
Time Complexity: O(E)
Space COmplexity: O(V)
'''
people = set()
for src, dst in edges:
   people.add(src)
   people.add(dst)


'''
Generate a unique integer id for each person
Time Complexity: O(V)
Space Complexity: O(V)
'''
ids = {}
curr_id = 0
for person in people:
   ids[person] = curr_id
   curr_id += 1


'''
Count the number of unique people
'''
size = len(people)


'''
Create a size x size 2d matrix of zeroes
'''
graph = [[0 for i in range(size)] for a in range(size)]

