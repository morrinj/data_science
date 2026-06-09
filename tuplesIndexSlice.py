t = (10, 20, 30, 40, 50)
print(t[0])    # 10
# Positive indexing (0-based)
print(t[0])      # 10  — first element
print(t[2])      # 30  — third element
print(t[-1])     # 50  — last element
print(t[-2])     # 40  — second from last
# Slicing
print(t[1:4])   # (20, 30, 40) — from index 1 to 3
print(t[:3])    # (10, 20, 30) — first three
print(t[3:])    # (40, 50) — from index 3 to end
print(t[2:4])   # (30, 40) — from index 2 to 3
print(t[::2])    # (10, 30, 50)  — every 2nd element
print(t[::-1])   # (50, 40, 30, 20, 10)  — reversed
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[1])      # (3, 4)
print(matrix[1][0])   # 3
print(matrix[2][1])   # 6