t = (1, 2, 3, 2, 4, 2, 5)
 
# count() — how many times a value appears
print(t.count(2))     # 3
 
# index() — position of first occurrence
print(t.index(3))     # 2
print(t.index(2))     # 1  (first occurrence only)
 
# Membership testing
print(3 in t)         # True
print(9 in t)         # False
 
# Concatenation and repetition (creates new tuple)
print((1, 2) + (3, 4))    # (1, 2, 3, 4)
print((1, 2) * 3)         # (1, 2, 1, 2, 1, 2)

