nums = [3, 1, 4, 1, 5, 9]
 
# append() — add ONE element to the end
nums.append(2)
print(nums)   # [3, 1, 4, 1, 5, 9, 2]
 
# insert(index, value) — insert at a specific position
nums.insert(0, 0)    # insert 0 at index 0
 
# extend() — add all elements from another iterable
nums.extend([6, 5])
# equivalent to: nums += [6, 5]
 
# remove() — remove FIRST occurrence of a value
nums.remove(1)    # removes the first 1
 
# pop(index) — remove AND return element at index
last  = nums.pop()     # removes last element
third = nums.pop(2)    # removes element at index 2
 
# del — delete by index or slice
del nums[0]
del nums[1:3]
 
# clear() — remove all elements
nums.clear()     # nums is now []
