# Basic unpacking
coords = (48.8, 2.35)     # Paris: lat, lon
lat, lon = coords
print(lat)    # 48.8
print(lon)    # 2.35
 
# Swap two variables — no temporary variable needed
a, b = 1060, 2076
a, b = b, a
print(a, b)   # 2076 1060
# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
 
*start, last = (1, 2, 3, 4, 5)
print(last)   # 5
print(start)  # [1, 2, 3, 4]
# Unpacking in a for loop — very common pattern
students = [('Alice', 90), ('Bob', 85), ('Carol', 92)]
for name, score in students:
    print(f'{name}: {score}')
# Output:
# Alice: 90
# Bob: 85
# Carol: 92