# Map each number to its square
squares = {x: x**2 for x in range(6)}
# {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)
 
# Invert a dictionary (swap keys and values)
original = {'a': 1, 'b': 2, 'c': 3}
inverted  = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
print(inverted)
 
# Filter: keep only passing students
grades = {'Alice': 90, 'Bob': 45, 'Carol': 82, 'Dave': 35}
passing = {name: s for name, s in grades.items() if s >= 50}
# {'Alice': 90, 'Carol': 82}
print(passing)
 
# Normalise scores to 0–1 scale
top = max(grades.values())    # 90
normalised = {n: round(s/top, 3) for n, s in grades.items()}
# {'Alice': 1.0, 'Bob': 0.5, 'Carol': 0.911, 'Dave': 0.389}
print(normalised)
