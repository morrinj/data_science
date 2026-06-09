# Empty list
empty = []
print(empty)
 
# Homogeneous lists
scores  = [85, 92, 78, 95, 88]
names   = ['Alice', 'Bob', 'Carol', 'Dave']
prices  = [19.99, 34.50, 5.99]
print(scores)
 
# Mixed-type (Python allows this)
record = ['Alice', 30, True, 95.5, None]
 
# Nested list (2D matrix)
matrix = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(matrix)
 
# Create from other sequences
from_range  = list(range(5))      # [0, 1, 2, 3, 4]
from_tuple  = list((1, 2, 3))     # [1, 2, 3]
from_string = list('hello')       # ['h','e','l','l','o']
print(from_range)
print(from_tuple)
print(from_string)