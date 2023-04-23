'''
Minimum Distance
Search "Level by Level"

Keep track of how far from the source you are
(what "level" you're on)

when you reach the destination, you'll know how far you've travelled
'''

'''
    1         Level 0 (root node)
   / \
  2   3       Level 1
 / \ / \
4  5 6  7     Level 2

Queue      Path
1          
2,3        1
3,4,5      1,2
4,5,6,7    1,2,3
5,6,7      1,2,3,4
6,7        1,2,3,4,5
7          1,2,3,4,5,6
           1,2,3,4,5,6,7


'''