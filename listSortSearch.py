fruits = ['banana', 'apple', 'cherry', 'apple', 'date']
 
# index() — first position of a value
print(fruits.index('apple'))   # 1
 
# count() — how many times a value appears
print(fruits.count('apple'))   # 2
 
# sort() — sort IN PLACE (modifies the list)
fruits.sort()
print(fruits)   # ['apple', 'apple', 'banana', 'cherry', 'date']
fruits.sort(reverse=True)   # descending
 
# sorted() — returns a NEW sorted list, original unchanged
nums = [5, 2, 8, 1, 9, 3]
sorted_nums = sorted(nums)     # [1, 2, 3, 5, 8, 9]
print(nums)                    # [5, 2, 8, 1, 9, 3] — unchanged
 
# Sort by a custom key
students = [('Bob', 85), ('Alice', 92), ('Carol', 78)]
students.sort(key=lambda s: s[1], reverse=True)
# [('Alice', 92), ('Bob', 85), ('Carol', 78)]
 
# Other useful operations
print(min(nums), max(nums), sum(nums))   # 1 9 28
print(len(nums))                          # 6
