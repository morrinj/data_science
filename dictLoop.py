grades = {'Alice': 90, 'Bob': 85, 'Carol': 92, 'Dave': 78}
 
# Iterate over KEYS (default)
for name in grades:          # same as: for name in grades.keys()
    print(name)
 
# Iterate over VALUES
for score in grades.values():
    print(score)
average = sum(grades.values()) / len(grades)   # 86.25
 
# Iterate over KEY-VALUE PAIRS — most common
for name, score in grades.items():
    print(f'{name}: {score}')
 
# Convert to lists
print(list(grades.keys()))    # ['Alice', 'Bob', 'Carol', 'Dave']
print(list(grades.values())) # [90, 85, 92, 78]
 
# setdefault() — get value, or set default if key missing
grades.setdefault('Eve', 0)  # adds Eve:0 only if Eve not present
 
# Merge two dicts (Python 3.9+)
extra = {'Frank': 88}
merged = grades | extra
print(merged)  # {'Alice': 90, 'Bob': 85, 'Carol': 92, 'Dave': 78, 'Eve': 0, 'Frank': 88}