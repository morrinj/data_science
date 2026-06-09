fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
 
# Indexing
print(fruits[0])      # 'apple'
print(fruits[-1])     # 'elderberry'
 
# Slicing (returns a new list)
print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[:2])     # ['apple', 'banana']
print(fruits[::2])    # ['apple', 'cherry', 'elderberry']
print(fruits[::-1])   # reversed list
 
# MUTABILITY — unlike tuples, you CAN change elements
fruits[0] = 'avocado'
print(fruits)  # ['avocado', 'banana', 'cherry', 'date', 'elderberry']
 
# Accessing nested list elements
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])   # 6  (row 1, column 2)
