def square(x): return x**2
square_l = lambda x: x**2
 
print(square(5))    # 25
print(square_l(5))  # 25
 
# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 4))   # 7
 
# Most common use: key in sorted()
students = [('Alice', 92), ('Bob', 85), ('Carol', 78), ('Dave', 95)]
 
# Sort by score descending
by_score = sorted(students, key=lambda s: s[1], reverse=True)
# [('Dave', 95), ('Alice', 92), ('Bob', 85), ('Carol', 78)]
 
# With map() — apply function to every element
scores = [85, 92, 78, 95]
scaled = list(map(lambda s: round(s * 0.9, 1), scores))
# [76.5, 82.8, 70.2, 85.5]
 
# With filter() — keep elements where function returns True
passing = list(filter(lambda s: s >= 80, scores))
