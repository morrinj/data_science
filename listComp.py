# Squares of 0–9
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)
 
# Equivalent for loop (slower, more verbose):
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# With condition: only even squares
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
print(even_squares)
# Transform strings
names = ['alice', 'bob', 'carol']
upper = [name.upper() for name in names]
# ['ALICE', 'BOB', 'CAROL']
print(upper)
# Filter a list
scores = [85, 42, 91, 67, 38, 95]
passing = [s for s in scores if s >= 50]
# [85, 91, 67, 95]
print(passing)
# Conditional expression (ternary) inside comprehension
grades = ['Pass' if s >= 50 else 'Fail' for s in scores]
# ['Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Pass']
print(grades)
 
# Flatten a 2D matrix into a 1D list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [val for row in matrix for val in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
