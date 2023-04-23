from tree_node import *
from collections import *

'''
Given the root of a binary tree, return the level order traversal of its nodes' values.
'''

def level_order_traversal(root: TreeNode) -> list:
    # A tree is a graph
    # Step 1: Base Cases
    if not root: return []

    # Step 2: Define tracking variables
    Q = deque()
    result = []
    level_list = []

    # Step 3: Intake start / first level, Terminating condition
    Q.append(root) 
    Q.append(None) # We are done with a level when we hit None

    # Step 4: Process the Queue
    while Q:
        node = Q.popleft()

        # Step 5: Check if the node is None or a Value
        if node: # If the node is not None
            level_list.append(node.val)

            # intake neighbors (children)
            if node.left: Q.append(node.left)
            if node.right: Q.append(node.right)

        else: # If the node is empty (we are at the end of the level)
            result.append(level_list[:]) # append the level list to the result list
            level_list.clear() # clear the level list
            if Q: Q.append(None)

    return result


'''
     3
    / \
   9   20
      /  \
     15   7

root = [3, 9, 20, None, None, 15, 7] # Tree
output = [[3], [9,20], [15,7]]
'''
root = root_from_list([3, 9, 20, None, None, 15, 7]) # Tree
print(level_order_traversal(root))
